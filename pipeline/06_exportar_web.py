import geopandas as gpd, pandas as pd, json, os, datetime
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import P, W, CFG, SIS, leer_barrios
from _pmtiles import escribir

def dump(gdf, path, dec=5):
    g = gdf.to_crs(4326).copy()
    if len(g): g["geometry"] = g.geometry.set_precision(10 ** -dec)
    d = json.loads(g.to_json(drop_id=True, na="null", show_bbox=False)) if len(g) else {"type": "FeatureCollection", "features": []}
    json.dump(d, open(path, "w", encoding="utf-8"), separators=(",", ":"), ensure_ascii=False)
ag = json.load(open(P + "agregados.json", encoding="utf-8"))
CORTES = escribir(P, W + "edificios.pmtiles")
dnames = {d["cod"]: d["nombre"] for d in ag["distritos"]}
FL = ["pob", "pob_v", "pob_a", "pob_r", "pct_v", "pct_a", "pct_r"]
def poly(g, key, rows, tol, extra=()):
    g = g.copy(); g["cod"] = g[key]
    if len(g) == 0: return g
    if "nombre" not in g: g["nombre"] = None
    df = pd.DataFrame(rows, columns=["cod"] + FL).set_index("cod")[FL]
    g = g.join(df, on="cod")
    for c in FL: g[c] = g[c].fillna(0.0) if "pct" in c else g[c].fillna(0).astype(int)
    if "distrito" in extra: g["distrito"] = g.cod_distrito.map(dnames)
    g = g[["cod", "nombre"] + list(extra) + FL + ["geometry"]].copy()
    if len(g): g["geometry"] = g.geometry.simplify(tol, preserve_topology=True)
    return g
dump(poly(gpd.read_file(P + "secciones.gpkg"), "cusec", ag["secciones"], 5), W + "secciones.geojson")
bar = leer_barrios()
dump(poly(bar, "cod_barrio", ag["barrios"], 10, ("cod_distrito", "distrito")), W + "barrios.geojson")
dump(poly(gpd.read_file(P + "distritos.gpkg"), "cod_distrito", ag["distritos"], 10), W + "distritos.geojson")
dump(gpd.read_file(P + "bases.gpkg", layer="bases")[["base_id", "nombre", "geometry"]], W + "bases.geojson")  # 07 lo reescribe con el ranking
strip = lambda o: {k: v for k, v in o.items() if not k.startswith(("a_", "m_"))}
json.dump({"ciudad": strip(ag["ciudad"]), "distritos": [strip(x) for x in ag["distritos"]], "barrios": [strip(x) for x in ag["barrios"]]},
          open(W + "agregados.json", "w", encoding="utf-8"), separators=(",", ":"), ensure_ascii=False)
m = lambda f: json.load(open(P + f, encoding="utf-8"))
est, lim, ine, cat, osm = m("meta_estaciones.json"), m("meta_limites.json"), m("meta_ine.json"), m("meta_catastro.json"), m("meta_osm.json")
hoy = datetime.date.today().isoformat()
fu = [{"nombre": f"{CFG['sistema']}: estaciones ({est['fuente']})", "url": est["url"], "fecha_descarga": est["fecha_descarga"], "referencia": est["fecha_descarga"]},
      {"nombre": "Distritos: " + lim["fuente_distritos"] + (("; barrios: " + lim["fuente_barrios"]) if lim["fuente_barrios"] else ""),
       "url": lim["url"] or ine["cartografia_url"], "fecha_descarga": lim["fecha_descarga"], "referencia": "vigente en la descarga"},
      {"nombre": "INE, cartografía de secciones censales", "url": ine["cartografia_url"], "fecha_descarga": ine["fecha_descarga"], "referencia": str(ine["cartografia_anio"])},
      {"nombre": ine["poblacion_fuente"], "url": ine["poblacion_url"], "fecha_descarga": ine["fecha_descarga"], "referencia": ine["poblacion_anio_referencia"][0]},
      {"nombre": cat["fuente"], "url": cat["url"], "fecha_descarga": cat["fecha_descarga"], "referencia": (cat["fecha_datos"] or "")[:10]},
      {"nombre": "OpenStreetMap (red peatonal), extracto de download.openstreetmap.fr", "url": "https://www.openstreetmap.org", "fecha_descarga": osm["fecha_descarga"], "referencia": (osm.get("fecha_datos") or "")[:10]}]
mu = gpd.read_file(P + "municipio.gpkg").to_crs(4326)
c = mu.geometry.iloc[0].centroid
# encuadre inicial: zona con edificios habitados (el termino puede incluir islas o monte lejanos, p. ej. Columbretes)
ep = gpd.read_parquet(P + "edificios_poblacion.parquet"); ep = ep[ep.poblacion > 0].to_crs(4326)
if len(ep):  # 99 % central de los edificios habitados (descarta diseminados lejanos)
    xs, ys = ep.geometry.x, ep.geometry.y
    bx = [round(float(v), 5) for v in (xs.quantile(.005), ys.quantile(.005), xs.quantile(.995), ys.quantile(.995))]
else:
    bx = [round(float(v), 5) for v in mu.total_bounds]
niveles = ["secciones"] + (["barrios"] if len(bar) else []) + ["distritos"]
json.dump({"generado": hoy, "sistema": CFG["sistema"], "ciudad": CFG["ciudad"], "id": SIS, "centro": [round(c.x, 5), round(c.y, 5)], "bbox": bx,
           "niveles": niveles, "cortes_poblacion_edificio": CORTES, "parametros": {"umbral_verde": 250, "umbral_amarillo": 500, "corte": 1500}, "fuentes": fu},
          open(W + "metadata.json", "w", encoding="utf-8"), separators=(",", ":"), ensure_ascii=False)
# pagina del sistema a partir de la plantilla comun
tpl = open("web/app/sistema.html", encoding="utf-8").read()
for k, v in {"{{SISTEMA}}": CFG["sistema"], "{{CIUDAD}}": CFG["ciudad"]}.items(): tpl = tpl.replace(k, v)
open(f"web/{SIS}/index.html", "w", encoding="utf-8").write(tpl)
for n in sorted(os.listdir(W)): print(n, round(os.path.getsize(W + n) / 1e6, 2), "MB")
