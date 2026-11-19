"""01 - Edificios (huella, uso y numero de viviendas). Catastro INSPIRE Buildings de la DG del Catastro y, en
Pais Vasco, los catastros forales (Bizkaia por municipio; Araba y Gipuzkoa por provincia)."""
import datetime as dt, json, re, zipfile, html
import geopandas as gpd, pandas as pd, pyogrio
from comun import CFG, P, RAW, COMUN, CRS, get

C = CFG["catastro"]; T = C["tipo"]; RC = RAW / "catastro"; RC.mkdir(exist_ok=True)
fecha_datos = None
if T == "nacional":
    num = C["codigo"][:5]; pr = num[:2]  # pr = gerencia territorial (52 Gijón, 53 Jerez, 54 Vigo)
    FEED = f"https://www.catastro.hacienda.gob.es/INSPIRE/buildings/{pr}/ES.SDGC.bu.atom_{pr}.xml"
    raw = get(FEED).content
    try: feed = raw.decode("utf-8")
    except UnicodeDecodeError: feed = raw.decode("latin-1")
    ent = [e for e in feed.split("<entry>") if re.search(rf"<title>\s*{num}-", e)]
    if ent:
        m = re.search(r'rel="enclosure"[^>]*href="([^"]+)"', ent[0]) or re.search(r'href="([^"]+\.zip)"', ent[0])
        URL = html.unescape(m.group(1))
        m = re.search(r"<updated>([^<]+)</updated>", ent[0]); fecha_datos = m.group(1) if m else None
    else:  # feed incompleto (el servidor corta a veces): ruta directa con el codigo de sistemas.json
        print("aviso:", num, "no aparece en el feed; se usa la ruta directa")
        URL = f"https://www.catastro.hacienda.gob.es/INSPIRE/Buildings/{pr}/{C['codigo']}/A.ES.SDGC.BU.{num}.zip"
    ZIP = RC / f"A.ES.SDGC.BU.{num}.zip"; GML = f"A.ES.SDGC.BU.{num}.building.gml"
    if ZIP.exists() and not zipfile.is_zipfile(ZIP): ZIP.unlink()
    if not ZIP.exists():
        get(URL, stream_to=ZIP)
        if not zipfile.is_zipfile(ZIP): raise SystemExit(f"La descarga no es un ZIP: {URL}")
    if not (RC / GML).exists(): zipfile.ZipFile(ZIP).extract(GML, RC)
    g = gpd.read_file(RC / GML, engine="pyogrio", columns=["localId", "currentUse", "numberOfDwellings", "numberOfBuildingUnits"])
    uso = g["currentUse"].astype("string").astype(object)
    fuente = f"Catastro INSPIRE Buildings (DG del Catastro), municipio {C['codigo']}"
else:
    if T == "bizkaia":
        URL = f"https://apli.bizkaia.eus/apps/Danok/INSPIRE/ES.BFA.BU.{C['mun']}.zip"; ZIP = RC / f"ES.BFA.BU.{C['mun']}.zip"
        if not ZIP.exists(): get(URL, stream_to=ZIP)
        if not (RC / "ES.BFA.BU.gml").exists(): zipfile.ZipFile(ZIP).extract("ES.BFA.BU.gml", RC)
        src, kw = RC / "ES.BFA.BU.gml", {}
        fuente = f"Catastro de Bizkaia, INSPIRE Buildings (Diputación Foral de Bizkaia), municipio 48{C['mun']}"
    elif T == "araba":
        URL = "https://geo.araba.eus/deskargak/INSPIRE/BU/GML/3042/BU_3042_GML.zip"; ZIP = COMUN / "foral" / "araba.zip"
        if not ZIP.exists(): get(URL, stream_to=ZIP)
        name = f"ES.AFA.BU.{C['mun']}_3042.gml"
        if not (RC / name).exists(): zipfile.ZipFile(ZIP).extract(name, RC)
        src, kw = RC / name, {}
        fuente = "Catastro de Álava, INSPIRE Buildings (Diputación Foral de Álava)"
    elif T == "gipuzkoa":
        URL = "https://b5m.gipuzkoa.eus/inspire/download/GML/ES.GFA.BU.zip"; ZIP = COMUN / "foral" / "gipuzkoa.zip"
        src = COMUN / "foral" / "gipuzkoa" / "ES.GFA.BU.gml"
        if not src.exists():
            if not ZIP.exists(): get(URL, stream_to=ZIP)
            zipfile.ZipFile(ZIP).extract("ES.GFA.BU.gml", src.parent)
        muni = gpd.read_file(P + "municipio.gpkg").to_crs(3042)
        kw = {"bbox": tuple(muni.buffer(200).total_bounds)}
        fuente = "Catastro de Gipuzkoa, INSPIRE Buildings (Diputación Foral de Gipuzkoa, b5m)"
    g = pyogrio.read_dataframe(src, columns=["localId", "numberOfDwellings"], **kw)
    if T == "gipuzkoa":  # fichero provincial: se conservan los edificios cuyo punto interior cae en el municipio
        mu = gpd.read_file(P + "municipio.gpkg").to_crs(g.crs).geometry.iloc[0]
        g = g[g.geometry.representative_point().within(mu.buffer(5))]
    n = pd.to_numeric(g["numberOfDwellings"], errors="coerce").fillna(0)
    # los catastros forales no exponen el uso de forma homogenea: residencial = edificio con viviendas
    uso = pd.Series(["1_residential" if v > 0 else None for v in n], index=g.index, dtype=object)
    g["numberOfBuildingUnits"] = 0
    fecha_datos = dt.date.fromtimestamp(src.stat().st_mtime).isoformat()
g = g.to_crs(CRS)
ok = (g.geometry.notna() & ~g.geometry.is_empty).values
g, uso = g[ok], uso[ok]
out = gpd.GeoDataFrame({"edif_id": g["localId"].astype(str).values, "uso": uso.values,
    "n_viviendas": pd.to_numeric(g["numberOfDwellings"], errors="coerce").fillna(0).astype(int).values,
    "n_unidades": pd.to_numeric(g["numberOfBuildingUnits"], errors="coerce").fillna(0).astype(int).values},
    geometry=g.geometry.values, crs=CRS)
out = out[~out.edif_id.duplicated()]
out.to_file(P + "edificios.gpkg", layer="edificios", driver="GPKG")
json.dump({"fuente": fuente, "url": URL, "fecha_datos": fecha_datos, "fecha_descarga": dt.date.today().isoformat(),
           "crs": CRS, "n_edificios": len(out), "tipo": T}, open(P + "meta_catastro.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("edificios", len(out), "| residenciales con viviendas", int(((out.uso == "1_residential") & (out.n_viviendas > 0)).sum()),
      "| viviendas", int(out.n_viviendas.sum()))
