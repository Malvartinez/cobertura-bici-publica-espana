import geopandas as gpd, pandas as pd
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import P, W, D as DOCS, EPSG, CFG, leer_barrios, asignar_zonas
e=gpd.read_file(P+"edificios.gpkg",layer="edificios")
r=e[(e.uso=="1_residential")&(e.n_viviendas>0)][["edif_id","n_viviendas","geometry"]].copy()
r["geometry"]=r.geometry.representative_point()  # siempre dentro del poligono
print("residenciales:",len(r))
sec=gpd.read_file(P+"secciones.gpkg",layer="secciones")[["cusec","geometry"]]
def asignar(pts,pol,cols):
    j=gpd.sjoin(pts,pol,predicate="within",how="left").drop(columns="index_right")
    j=j[~j.index.duplicated()]
    miss=j[cols[0]].isna()
    if miss.any():
        n=gpd.sjoin_nearest(pts.loc[miss[miss].index],pol,how="left").drop(columns="index_right")
        n=n[~n.index.duplicated()]
        for c in cols: j.loc[n.index,c]=n[c]
    return j,miss
r,m_sec=asignar(r[["edif_id","n_viviendas","geometry"]],sec,["cusec"])
r["asignacion"]=m_sec.map({True:"cercana",False:"dentro"})
z=asignar_zonas(r[["geometry"]])
r["cod_barrio"]=z["cod_barrio"]; r["cod_distrito"]=z["cod_distrito"]
print("fuera de seccion -> cercana:",int(m_sec.sum()),"| fuera de distrito -> cercano:",z.get("cod_distrito_fuera"),"| fuera de barrio:",z.get("cod_barrio_fuera"))
r=r[["edif_id","n_viviendas","cusec","cod_barrio","cod_distrito","asignacion","geometry"]]
r.to_parquet(P+"edificios_residenciales.parquet")
print("guardado",len(r))
