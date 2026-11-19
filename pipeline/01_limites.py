"""01 - Distritos y barrios. Fuente oficial del ayuntamiento cuando se ha localizado (tipo en sistemas.json);
si no, distritos censales del INE ("Distrito N") y sin nivel de barrio."""
import io, json, zipfile, datetime as dt
import pandas as pd, geopandas as gpd
from shapely import wkt
from pathlib import Path
from comun import CFG, P, RAW, CRS, get

L = CFG["limites"]; T = L["tipo"]; RL = RAW / "limites"; RL.mkdir(exist_ok=True)
fuente, url_fuente = None, None
cod = lambda s, n=2: pd.Series(s).astype(str).str.replace(r"\.0$", "", regex=True).str.strip().str.zfill(n).values

def zipshp(url, name):
    d = RL / name
    if not list(d.rglob("*.shp")):
        d.mkdir(exist_ok=True); zipfile.ZipFile(io.BytesIO(get(url).content)).extractall(d)
    return gpd.read_file(next(d.rglob("*.shp"))).to_crs(CRS)

def descarga(url, name):
    f = RL / name
    if not f.exists(): f.write_bytes(get(url).content)
    return gpd.read_file(f).to_crs(CRS)

dis = bar = None
if T == "madrid":
    B = "https://geoportal.madrid.es/fsdescargas/IDEAM_WBGEOPORTAL/LIMITES_ADMINISTRATIVOS/"
    d, b = zipshp(B + "Distritos/Distritos.zip", "distritos"), zipshp(B + "Barrios/Barrios.zip", "barrios")
    dis = gpd.GeoDataFrame({"cod_distrito": cod(d.COD_DIS_TX), "nombre": d.NOMBRE.values}, geometry=d.geometry.values, crs=CRS)
    bar = gpd.GeoDataFrame({"cod_barrio": cod(b.COD_BAR, 3), "nombre": b.NOMBRE.values, "cod_distrito": cod(b.COD_DIS_TX)}, geometry=b.geometry.values, crs=CRS)
    fuente, url_fuente = "Geoportal del Ayuntamiento de Madrid", "https://geoportal.madrid.es"
elif T == "barcelona":
    API = "https://opendata-ajuntament.barcelona.cat/data/api/action/datastore_search"
    def recurso(rid, name):
        f = RL / f"{name}.json"
        if not f.exists():
            recs, off = [], 0
            while True:
                r = get(API, params={"resource_id": rid, "limit": 100, "offset": off}).json()["result"]["records"]
                recs += r; off += len(r)
                if len(r) < 100: break
            f.write_text(json.dumps(recs, ensure_ascii=False), encoding="utf-8")
        df = pd.DataFrame(json.loads(f.read_text(encoding="utf-8"))).rename(columns=str.lower)
        return gpd.GeoDataFrame(df, geometry=df.geometria_etrs89.map(wkt.loads), crs="EPSG:25831").to_crs(CRS)
    d, b = recurso("576bc645-9481-4bc4-b8bf-f5972c20df3f", "districtes"), recurso("b21fa550-56ea-4f4c-9adc-b8009381896e", "barris")
    dis = gpd.GeoDataFrame({"cod_distrito": cod(d.codi_districte), "nombre": d.nom_districte.values}, geometry=d.geometry.values, crs=CRS)
    bar = gpd.GeoDataFrame({"cod_barrio": cod(b.codi_barri), "nombre": b.nom_barri.values, "cod_distrito": cod(b.codi_districte)}, geometry=b.geometry.values, crs=CRS)
    fuente, url_fuente = "Open Data BCN (20170706-districtes-barris)", "https://opendata-ajuntament.barcelona.cat/data/es/dataset/20170706-districtes-barris"
elif T == "capas":
    # capas genericas: {"distritos": {...}, "barrios": {...}} con url, formato (zipshp|geo) y nombres de campos
    def capa(c, nivel):
        g = zipshp(c["url"], nivel) if c.get("formato") == "zipshp" else descarga(c["url"], nivel + "." + c.get("ext", "geojson"))
        if c.get("filtro"): g = g.query(c["filtro"])
        return g
    if "distritos" in L:
        c = L["distritos"]; d = capa(c, "distritos")
        dis = gpd.GeoDataFrame({"cod_distrito": cod(d[c["cod"]]), "nombre": d[c["nombre"]].astype(str).str.strip().values}, geometry=d.geometry.values, crs=CRS)
    if "barrios" in L:
        c = L["barrios"]; b = capa(c, "barrios")
        nom = b[c["nombre"]].astype(str).str.strip()
        if c.get("capitalizar"): nom = nom.str.title().str.replace(r"(?<!^)\b(De|Del|La|Las|Los|El|Y)\b", lambda m: m.group(1).lower(), regex=True)
        bar = gpd.GeoDataFrame({"cod_barrio": cod(b[c["cod"]], c.get("ancho", 3)), "nombre": nom.values,
                                "cod_distrito": cod(b[c["distrito"]]) if c.get("distrito") else None}, geometry=b.geometry.values, crs=CRS)
    fuente, url_fuente = L["fuente"], L["url_fuente"]

if dis is None:  # distritos censales del INE
    d = gpd.read_file(P + "distritos_ine.gpkg")
    dis = gpd.GeoDataFrame({"cod_distrito": d.cod_distrito.values, "nombre": ["Distrito " + str(int(c)) for c in d.cod_distrito]}, geometry=d.geometry.values, crs=CRS)
    fuente_d = "INE, distritos censales 2025"
else:
    fuente_d = fuente
dis = dis.dissolve("cod_distrito", aggfunc="first").reset_index()[["cod_distrito", "nombre", "geometry"]].sort_values("cod_distrito").reset_index(drop=True)
dis.to_file(P + "distritos.gpkg", layer="distritos", driver="GPKG")
Path(P + "barrios.gpkg").unlink(missing_ok=True)
if bar is not None:
    bar = bar.dissolve("cod_barrio", aggfunc="first").reset_index()
    if bar.cod_distrito.isna().any():  # barrio -> distrito por punto representativo
        pt = gpd.GeoDataFrame(geometry=bar.geometry.representative_point(), crs=CRS)
        j = gpd.sjoin_nearest(pt, dis[["cod_distrito", "geometry"]], how="left")
        j = j[~j.index.duplicated()]
        bar["cod_distrito"] = bar.cod_distrito.fillna(j.cod_distrito)
    bar = bar[["cod_barrio", "nombre", "cod_distrito", "geometry"]].sort_values("cod_barrio").reset_index(drop=True)
    bar.to_file(P + "barrios.gpkg", layer="barrios", driver="GPKG")
muni = gpd.read_file(P + "municipio.gpkg").geometry.iloc[0]
cob = lambda g: round(100 * g.geometry.union_all().intersection(muni).area / muni.area, 1)
meta = {"fuente_distritos": fuente_d, "fuente_barrios": fuente if bar is not None else None, "url": url_fuente,
        "fecha_descarga": dt.date.today().isoformat(), "n_distritos": len(dis), "n_barrios": 0 if bar is None else len(bar),
        "cobertura_distritos_pct": cob(dis), "cobertura_barrios_pct": None if bar is None else cob(bar)}
json.dump(meta, open(P + "meta_limites.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(meta)
