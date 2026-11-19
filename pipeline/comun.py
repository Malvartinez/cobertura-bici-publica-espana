"""Configuracion comun: sistema activo (variable SISTEMA o primer argumento), rutas y utilidades."""
import json, os, sys, time
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
SISTEMAS = {s["id"]: s for s in json.load(open(ROOT / "sistemas.json", encoding="utf-8"))["sistemas"]}
SIS = os.environ.get("SISTEMA") or (sys.argv[1] if len(sys.argv) > 1 else None)
if SIS not in SISTEMAS:
    raise SystemExit(f"Indica un sistema (SISTEMA=...): {', '.join(SISTEMAS)}")
CFG = SISTEMAS[SIS]
EPSG = CFG["epsg"]; CRS = f"EPSG:{EPSG}"
P = f"data/{SIS}/processed/"; W = f"web/{SIS}/data/"; D = f"docs/sistemas/{SIS}/"
RAW = ROOT / "data" / SIS / "raw"; COMUN = ROOT / "data" / "_comun"
for p in (P, W, D): Path(p).mkdir(parents=True, exist_ok=True)
RAW.mkdir(parents=True, exist_ok=True); COMUN.mkdir(parents=True, exist_ok=True)

def get(url, intentos=6, stream_to=None, **kw):
    """GET con reintentos (algunos servidores cortan conexiones de forma intermitente)."""
    for i in range(intentos):
        try:
            if stream_to:
                tmp = Path(str(stream_to) + ".part")
                with requests.get(url, stream=True, timeout=900, **kw) as r:
                    r.raise_for_status()
                    with open(tmp, "wb") as f:
                        for c in r.iter_content(1 << 20): f.write(c)
                os.replace(tmp, stream_to); return stream_to
            r = requests.get(url, timeout=300, **kw); r.raise_for_status(); return r
        except Exception as e:
            if i == intentos - 1: raise
            print("reintento", i + 1, url, repr(e)[:120], flush=True); time.sleep(5 * (i + 1))

def vacio(path):
    import geopandas as gpd
    return (not Path(path).exists()) or len(gpd.read_file(path)) == 0

def leer_barrios():
    """Barrios oficiales o GeoDataFrame vacio si la ciudad no tiene ese nivel."""
    import geopandas as gpd
    f = Path(P + "barrios.gpkg")
    if f.exists(): return gpd.read_file(f)
    return gpd.GeoDataFrame({"cod_barrio": [], "nombre": [], "cod_distrito": []}, geometry=[], crs=CRS)

def asignar_zonas(pts):
    """cod_distrito y cod_barrio de cada punto (dentro; si cae fuera, el poligono mas cercano)."""
    import geopandas as gpd
    out = {}
    for nivel, pol in (("cod_distrito", gpd.read_file(P + "distritos.gpkg")), ("cod_barrio", leer_barrios())):
        if len(pol) == 0: out[nivel] = None; continue
        pol = pol[[nivel, "geometry"]]
        j = gpd.sjoin(pts[["geometry"]], pol, predicate="within", how="left"); j = j[~j.index.duplicated()][nivel]
        miss = j.isna()
        if miss.any():
            n = gpd.sjoin_nearest(pts.loc[miss[miss].index, ["geometry"]], pol, how="left"); n = n[~n.index.duplicated()]
            j.loc[n.index] = n[nivel]
        out[nivel] = j; out[nivel + "_fuera"] = int(miss.sum())
    return out
