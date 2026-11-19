"""01 - Secciones censales (cartografia INE 2025) y poblacion por seccion (Censo anual 2025, servicio de Esri Espana)."""
import json, zipfile, datetime, pyogrio, pandas as pd, geopandas as gpd
from comun import CFG, P, RAW, COMUN, CRS, get

MUN = CFG["ine"]
URL_CART = "https://www.ine.es/prodyser/cartografia/seccionado_2025.zip"
URL_POB = "https://services1.arcgis.com/nCKYwcSONQTkPA4K/arcgis/rest/services/SeccionCensal25Continua_Spain/FeatureServer/0/query"
URL_ITEM = "https://www.arcgis.com/home/item.html?id=304cb4fe00f14ebca73e762ba2e02d7e"
zpath = COMUN / "seccionado_2025.zip"
if not zpath.exists(): get(URL_CART, stream_to=zpath)
ext = COMUN / "seccionado_2025"
if not ext.exists(): zipfile.ZipFile(zpath).extractall(ext)
shp = next(ext.rglob("SECC_CE_*.shp"))
g = pyogrio.read_dataframe(shp, where=f"CUMUN='{MUN}'").to_crs(CRS)
sec = gpd.GeoDataFrame({"cusec": g.CUSEC.astype(str), "cod_distrito": g.CDIS.astype(str).str.zfill(2),
                        "cod_seccion": g.CSEC.astype(str).str.zfill(3)}, geometry=g.geometry.values, crs=CRS)
sec.to_file(P + "secciones.gpkg", layer="secciones", driver="GPKG")
muni = gpd.GeoDataFrame({"nombre": [g.NMUN.iloc[0]]}, geometry=[sec.geometry.union_all()], crs=CRS)
muni.to_file(P + "municipio.gpkg", layer="municipio", driver="GPKG")
dis = sec.dissolve("cod_distrito").reset_index()[["cod_distrito", "geometry"]]
dis.to_file(P + "distritos_ine.gpkg", layer="distritos", driver="GPKG")

jpath = RAW / f"censo2025_seccion_{MUN}.json"
if not jpath.exists():
    feats, off = [], 0
    while True:
        r = get(URL_POB, params={"where": f"Cod_MUN='{MUN}'", "outFields": "*", "returnGeometry": "false",
                                 "f": "json", "resultOffset": off, "resultRecordCount": 2000, "orderByFields": "Codigo"}).json()
        f = r["features"]; feats += f; off += len(f)
        if not f or not r.get("exceededTransferLimit"): break
    jpath.write_text(json.dumps(feats, ensure_ascii=False), encoding="utf-8")
df = pd.DataFrame([x["attributes"] for x in json.loads(jpath.read_text(encoding="utf-8"))])
ed = lambda a: [f"De_{i}_a_{i+4}_años" for i in range(a[0], a[1], 5)]
c1564 = ed((15, 65)); c65 = ed((65, 100)) + ["De_100_y_mas_años"]
pob = pd.DataFrame({"cusec": df.Codigo.astype(str), "poblacion": df.Total.astype(int),
                    "pob_15_64": df[c1564].sum(axis=1).astype(int), "pob_65": df[c65].sum(axis=1).astype(int)}).drop_duplicates("cusec")
pob.to_parquet(P + "poblacion_secciones.parquet", index=False)
a, b = set(pob.cusec), set(sec.cusec)
print(f"{muni.nombre.iloc[0]}: secciones={len(sec)} distritos INE={len(dis)} poblacion={pob.poblacion.sum()} "
      f"pob sin cartografia={len(a-b)} cartografia sin pob={len(b-a)} area km2={muni.area.iloc[0]/1e6:.1f}")
assert not (a - b), "secciones con poblacion sin cartografia"
json.dump({"cartografia_url": URL_CART, "cartografia_anio": 2025, "poblacion_url": URL_ITEM,
           "poblacion_fuente": "INE, Censo anual de población 2025 por sección censal (servicio de Esri España)",
           "poblacion_anio_referencia": ["1 ene 2025"], "n_secciones": len(sec), "poblacion_total": int(pob.poblacion.sum()),
           "municipio": muni.nombre.iloc[0], "area_km2": round(muni.area.iloc[0] / 1e6, 1),
           "fecha_descarga": datetime.date.today().isoformat()}, open(P + "meta_ine.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
