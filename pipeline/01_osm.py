"""01 - Red peatonal OSM del municipio (+1 km). Overpass y Geofabrik no son accesibles de forma fiable desde el
entorno de calculo: se parte del extracto regional/provincial de download.openstreetmap.fr, se recorta con osmium
y se aplica el mismo filtro que OSMnx usa para network_type="walk"."""
import json, re, time, gc, subprocess, datetime as dt
from xml.sax.saxutils import quoteattr as q
import osmnx as ox, networkx as nx, geopandas as gpd, pandas as pd, osmium
from shapely.geometry import LineString
from comun import CFG, P, RAW, COMUN, EPSG, get

f_nod, f_ari, f_meta = P + "red_nodos.parquet", P + "red_aristas.gpkg", P + "meta_osm.json"
ox.settings.log_console = False
ox.settings.useful_tags_way = ["highway", "name"]
def log(m): print(time.strftime("%H:%M:%S"), m, flush=True)

URL_PBF = f"https://download.openstreetmap.fr/extracts/{CFG['osm']}-latest.osm.pbf"
REG = COMUN / "osm" / (CFG["osm"].replace("/", "_") + ".osm.pbf"); REG.parent.mkdir(parents=True, exist_ok=True)
if not REG.exists(): get(URL_PBF, stream_to=REG)
fecha_osm = osmium.io.Reader(str(REG)).header().get("osmosis_replication_timestamp")
g = gpd.read_file(P + "municipio.gpkg").to_crs(EPSG)
poly = gpd.GeoSeries([g.geometry.union_all().buffer(1000)], crs=EPSG).to_crs(4326).iloc[0]
x0, y0, x1, y1 = gpd.GeoSeries([poly.buffer(0.01)], crs=4326).total_bounds
(RAW / "osm").mkdir(exist_ok=True); PBF = RAW / "osm" / "recorte.osm.pbf"; XML = RAW / "osm" / "red_walk.osm"
subprocess.run(["osmium", "extract", "-b", f"{x0},{y0},{x1},{y1}", "-s", "complete_ways", "-O", "-o", str(PBF), str(REG)], check=True)

NEG = {"area": "yes", "access": "private",
       "highway": "abandoned|bus_guideway|construction|cycleway|motor|no|planned|platform|proposed|raceway|razed|rest_area|services",
       "foot": "no", "service": "private", "sidewalk": "separate", "sidewalk:both": "separate",
       "sidewalk:left": "separate", "sidewalk:right": "separate"}
NEG = {k: re.compile(v) for k, v in NEG.items()}  # semantica Overpass "!~": la clave falta o no casa
def ok(t): return "highway" in t and not any(k in t and rx.search(t[k]) for k, rx in NEG.items())

t0 = time.time(); ways, need = [], set()
for w in osmium.FileProcessor(str(PBF), osmium.osm.WAY):
    t = dict(w.tags)
    if ok(t):
        refs = [n.ref for n in w.nodes]
        ways.append((w.id, refs, {k: t[k] for k in ("highway", "name", "oneway") if k in t})); need.update(refs)
with open(XML, "w", encoding="utf-8") as fh:
    fh.write("<?xml version='1.0' encoding='UTF-8'?>\n<osm version='0.6'>\n")
    hay = set()
    for n in osmium.FileProcessor(str(PBF), osmium.osm.NODE):
        if n.id in need and n.location.valid():
            fh.write(f"<node id='{n.id}' lat='{n.location.lat:.7f}' lon='{n.location.lon:.7f}'/>\n"); hay.add(n.id)
    nid = -1
    for wid, refs, t in ways:
        # vias cortadas por el borde del extracto: se parten en tramos de nodos presentes (nunca se unen huecos)
        tramos, cur = [], []
        for r in refs:
            if r in hay: cur.append(r)
            else:
                if len(cur) > 1: tramos.append(cur)
                cur = []
        if len(cur) > 1: tramos.append(cur)
        for i, tr in enumerate(tramos):
            w_id = wid if len(tramos) == 1 and len(tr) == len(refs) else nid
            if w_id == nid: nid -= 1
            fh.write(f"<way id='{w_id}'>" + "".join(f"<nd ref='{r}'/>" for r in tr) +
                     "".join(f"<tag k={q(k)} v={q(v)}/>" for k, v in t.items()) + "</way>\n")
    fh.write("</osm>\n")
log("xml peatonal: %d vias, %d nodos" % (len(ways), len(need))); del ways, need; gc.collect()
G = ox.graph_from_xml(XML, bidirectional=True, simplify=False, retain_all=True)
G = ox.truncate.truncate_graph_polygon(G, poly, truncate_by_edge=True)
G = ox.simplify_graph(G)
log("grafo construido: %d nodos" % len(G))
G = G.subgraph(max(nx.weakly_connected_components(G), key=len)).copy()
G = ox.project_graph(G, to_crs=f"EPSG:{EPSG}"); gc.collect()
nodes, edges = ox.graph_to_gdfs(G)
edges = edges.reset_index(); xy = nodes[["x", "y"]]
geoms = edges.geometry.copy(); miss = geoms.isna()
if miss.any():
    geoms[miss] = [LineString([(xy.at[u, "x"], xy.at[u, "y"]), (xy.at[v, "x"], xy.at[v, "y"])]) for u, v in zip(edges.u[miss], edges.v[miss])]
edges["geometry"] = geoms
edges["a"] = edges[["u", "v"]].min(axis=1); edges["b"] = edges[["u", "v"]].max(axis=1)
edges = edges[edges.a != edges.b].sort_values("length").drop_duplicates(["a", "b"])
edges = edges.assign(u=edges.a.astype("int64"), v=edges.b.astype("int64"))
ar = gpd.GeoDataFrame(edges[["u", "v", "length"]].astype({"length": float}), geometry=edges.geometry.values, crs=EPSG)
ids = set(ar.u) | set(ar.v)
nd = pd.DataFrame({"node_id": nodes.index.astype("int64"), "x": nodes.x.astype(float).values, "y": nodes.y.astype(float).values})
nd = nd[nd.node_id.isin(ids)].reset_index(drop=True)
nd.to_parquet(f_nod, index=False); ar.to_file(f_ari, layer="aristas", driver="GPKG")
meta = dict(fecha_descarga=dt.date.today().isoformat(), fuente=URL_PBF, fecha_datos=fecha_osm, nodos=len(nd), aristas=len(ar),
            longitud_total_km=round(float(ar.length.sum()) / 1000, 1))
json.dump(meta, open(f_meta, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(meta, "segundos:", round(time.time() - t0))
