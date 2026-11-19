"""01 - Estaciones del sistema: feed GBFS oficial (station_information) o, si el operador no lo publica, CityBikes."""
import json, datetime as dt
import pandas as pd, geopandas as gpd
from comun import CFG, P, RAW, CRS, get

HOY = dt.date.today().isoformat()
src = CFG["estaciones"]
url = src["url"] if src["tipo"] == "gbfs" else f"https://api.citybik.es/v2/networks/{src['id']}?fields=stations"
existentes = sorted(RAW.glob("estaciones_*.json"))
raw_f = existentes[-1] if existentes else RAW / f"estaciones_{HOY}.json"
if not existentes: raw_f.write_bytes(get(url).content)
fecha = raw_f.stem.split("_")[-1]
d = json.loads(raw_f.read_text(encoding="utf-8"))
if src["tipo"] == "gbfs":
    st = pd.DataFrame(d["data"]["stations"])
    if "is_virtual_station" in st: st = st[st.is_virtual_station != True]
    st = pd.DataFrame({"base_id": st.station_id.astype(str), "nombre": st.name.astype(str).str.strip(), "lat": st.lat, "lon": st.lon})
else:
    st = pd.DataFrame(d["network"]["stations"])
    st = pd.DataFrame({"base_id": st.id.astype(str), "nombre": st.name.astype(str).str.strip(), "lat": st.latitude, "lon": st.longitude})
st = st.dropna(subset=["lat", "lon"]); st = st[(st.lat != 0) & (st.lon != 0)].drop_duplicates("base_id")
bases = gpd.GeoDataFrame(st[["base_id", "nombre"]], geometry=gpd.points_from_xy(st.lon, st.lat), crs="EPSG:4326").to_crs(CRS)
bases = bases.drop_duplicates(subset=["nombre", "geometry"]).reset_index(drop=True)
bases.to_file(P + "bases.gpkg", layer="bases", driver="GPKG")
json.dump({"fuente": "GBFS station_information" if src["tipo"] == "gbfs" else "CityBikes API", "url": url,
           "fecha_descarga": fecha, "n": len(bases)}, open(P + "meta_estaciones.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("estaciones:", len(bases), "fuente:", url)
