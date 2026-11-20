"""10 - Figuras de la página de metodología: un caso real paso a paso (no lo ejecuta run_all).
Uso: SISTEMA=zaragoza python pipeline/10_figuras_metodologia.py [edif_id]
Escribe web/metodologia/paso*.png y web/metodologia/caso.json con las cifras del caso."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd, geopandas as gpd, scipy.sparse as sp, shapely
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from scipy.sparse.csgraph import dijkstra
from scipy.spatial import cKDTree
from shapely import STRtree
from comun import P, SIS, CFG
from _acceso import accesos, RADIO

EDIF = sys.argv[1] if len(sys.argv) > 1 else "6674803XM7167D"
OUT = "web/metodologia/"; os.makedirs(OUT, exist_ok=True)
# colores de la web
VERDE, AMAR, ROJO, AZUL, ROSA = "#2fa35a", "#f0b90b", "#e0443a", "#2D8EFF", "#ff4fd8"
TX, TX2, TX3, RED, EDIFC, FONDO = "#1A1C20", "#5A6069", "#8A9099", "#C9CDD3", "#E3E6EA", "#FFFFFF"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.titlesize": 15, "axes.titleweight": "bold",
                     "axes.titlelocation": "left", "text.color": TX, "figure.facecolor": FONDO, "axes.facecolor": FONDO})

# --- datos ---
nod = pd.read_parquet(P + "red_nodos.parquet"); ed = gpd.read_file(P + "red_aristas.gpkg")
bas = gpd.read_file(P + "bases.gpkg").reset_index(drop=True)
bld = gpd.read_parquet(P + "edificios_distancias.parquet").reset_index(drop=True)
fp = gpd.read_file(P + "edificios.gpkg")[["edif_id", "uso", "n_viviendas", "geometry"]].drop_duplicates("edif_id").set_index("edif_id")
sec = gpd.read_file(P + "secciones.gpkg"); pob = pd.read_parquet(P + "poblacion_secciones.parquet").set_index("cusec")
N = len(nod); idx = pd.Series(np.arange(N), index=nod.node_id.values); nx_, ny_ = nod.x.values, nod.y.values
U = idx[ed.u.values].values; V = idx[ed.v.values].values; L = np.maximum(ed.length.values.astype(float), 1e-6)
sd, sn = cKDTree(np.c_[nx_, ny_]).query(np.c_[bas.geometry.x, bas.geometry.y])
ob, on, oo, ini, dp = accesos(P, bld, ed, U, V, L, nx_, ny_)
i = int(np.flatnonzero(bld.edif_id.values == EDIF)[0]); b = bld.iloc[i]
huella = fp.loc[EDIF].geometry; pint = b.geometry
k0, k1 = ini[i], (ini[i + 1] if i + 1 < len(ini) else len(ob))
opc_n, opc_o = on[k0:k1], oo[k0:k1]; es_borde = np.arange(k1 - k0) >= 2
j = int(np.flatnonzero(bas.base_id.astype(str).values == str(b.base_id))[0]); est = bas.iloc[j]
G = sp.coo_matrix((L, (U, V)), shape=(N, N)).tocsr()
Dj, pred = dijkstra(G, directed=False, indices=sn[j], return_predecessors=True, limit=3000)
tot = sd[j] + Dj[opc_n] + opc_o
kb = int(np.argmin(tot)); kint = int(np.argmin(tot[:2]))
def camino(n):
    c = [n]
    while c[-1] != sn[j] and pred[c[-1]] >= 0: c.append(pred[c[-1]])
    return np.array(c)
cam_b, cam_i = camino(opc_n[kb]), camino(opc_n[kint])
d_fin, d_int = float(tot[kb]), float(tot[kint]); recta = float(huella.distance(est.geometry)); recta_pi = float(pint.distance(est.geometry))
nivel = lambda d: ("verde", VERDE) if d < 250 else (("amarillo", AMAR) if d <= 500 else ("rojo", ROJO))
# reparto de población en la sección
cs = b.cusec; secg = sec.set_index("cusec").loc[cs].geometry
res_sec = bld[bld.cusec == cs]; viv_sec = int(res_sec.n_viviendas.sum()); pob_sec = int(pob.loc[cs, "poblacion"])
caso = dict(sistema=CFG["sistema"], ciudad=CFG["ciudad"], edificio=EDIF, viviendas=int(b.n_viviendas), poblacion=round(float(b.poblacion), 1),
            seccion=cs, viviendas_seccion=viv_sec, poblacion_seccion=pob_sec, edificios_seccion=int(len(res_sec)), area_m2=round(huella.area),
            estacion=str(est.nombre), enganche_estacion_m=round(float(sd[j]), 1), d_perp_m=round(float(dp[i]), 1),
            opciones=int(k1 - k0), opciones_borde=int(es_borde.sum()), recta_m=round(recta), recta_punto_interior_m=round(recta_pi),
            red_punto_interior_m=round(d_int), red_mejor_acceso_m=round(d_fin), desfase_mejor_m=round(float(opc_o[kb]), 1),
            nivel_punto_interior=nivel(d_int)[0], nivel=nivel(d_fin)[0], distancia_web=round(float(b.distancia)))
json.dump(caso, open(OUT + "caso.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(caso)

# --- utilidades de dibujo ---
def lienzo(cx, cy, r, titulo, sub=None, w=10, h=7.2):
    f, ax = plt.subplots(figsize=(w, h), dpi=150)
    ax.set_xlim(cx - r * w / h, cx + r * w / h); ax.set_ylim(cy - r, cy + r); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(titulo, pad=14 if not sub else 26)
    if sub: ax.text(0, 1.012, sub, transform=ax.transAxes, color=TX2, fontsize=10.5, va="bottom")
    return f, ax
def fondo(ax, red=True, edif=True, bbox=None):
    if edif:
        e = fp.cx[bbox[0]:bbox[2], bbox[1]:bbox[3]] if bbox else fp
        e.plot(ax=ax, color=EDIFC, edgecolor="#D5D9DE", linewidth=.3, zorder=1)
    if red:
        r = ed.cx[bbox[0]:bbox[2], bbox[1]:bbox[3]] if bbox else ed
        r.plot(ax=ax, color=RED, linewidth=.9, zorder=2)
def escala(ax, m):
    x0, x1 = ax.get_xlim(); y0, y1 = ax.get_ylim(); px, py = x0 + (x1 - x0) * .04, y0 + (y1 - y0) * .05
    ax.plot([px, px + m], [py, py], color=TX, lw=2.2, solid_capstyle="butt", zorder=20)
    ax.text(px + m / 2, py + (y1 - y0) * .015, f"{m} m", ha="center", va="bottom", fontsize=9.5, color=TX, zorder=20)
FUENTE_EST = "GBFS" if CFG["estaciones"]["tipo"] == "gbfs" else "CityBikes"
def pie(f, txt=f"{CFG['ciudad']} · Catastro, INE (censo 2025), OpenStreetMap, {CFG['sistema']} ({FUENTE_EST})"):
    f.text(.012, .012, txt, fontsize=8.5, color=TX3)
def guardar(f, n):
    f.savefig(OUT + n, dpi=150, facecolor=FONDO); plt.close(f); print("ok", n)
def rotulo(ax, x, y, t, dx=0, dy=0, ha="left", color=TX, size=10, peso="normal", flecha=True):
    ax.annotate(t, (x, y), xytext=(x + dx, y + dy), ha=ha, va="center", fontsize=size, color=color, fontweight=peso, zorder=30,
                bbox=dict(boxstyle="round,pad=.3", fc="white", ec="#D5D9DE", lw=.6),
                arrowprops=dict(arrowstyle="-", color=TX2, lw=.8) if flecha and (dx or dy) else None)
def pts(arr): return nx_[arr], ny_[arr]
hx, hy = huella.centroid.x, huella.centroid.y
ex, ey = est.geometry.x, est.geometry.y
mx, my = (hx + ex) / 2, (hy + ey) / 2; R0 = max(abs(hx - ex), abs(hy - ey)) * .75 + 120

# 1. el caso
f, ax = lienzo(mx, my, R0, "El caso: una manzana residencial y su estación más cercana",
               f"Edificio {EDIF} ({caso['viviendas']} viviendas) y la estación «{caso['estacion'].title()}» de {CFG['sistema']}")
bb = (mx - 2 * R0, my - R0, mx + 2 * R0, my + R0); fondo(ax, bbox=bb)
gpd.GeoSeries([huella]).plot(ax=ax, color=VERDE, edgecolor=TX, linewidth=1, zorder=5)
ax.scatter([ex], [ey], s=110, color=AZUL, edgecolor="white", linewidth=1.6, zorder=12)
ax.plot([hx, ex], [hy, ey], color=TX2, lw=1.2, ls=(0, (4, 3)), zorder=6)
rotulo(ax, hx, hy + (huella.bounds[3] - hy), "El edificio del ejemplo", dx=0, dy=R0 * .18, ha="center", peso="bold", flecha=False)
rotulo(ax, ex, ey, f"Estación «{caso['estacion'].title()}»", dx=0, dy=-R0 * .16, ha="center", peso="bold", flecha=False)
rotulo(ax, mx, my, f"{caso['recta_m']} m en línea recta", dx=0, dy=-R0 * .1, ha="center", color=TX2, flecha=False)
ax.legend(handles=[Patch(color=EDIFC, label="Edificios (Catastro)"), Line2D([], [], color=RED, lw=1.5, label="Red peatonal (OpenStreetMap)"),
                   Line2D([], [], marker="o", ls="", color=AZUL, markersize=9, label="Estación de bici pública")],
          loc="upper right", frameon=True, framealpha=.95, edgecolor="#D5D9DE", fontsize=9.5)
escala(ax, 100); pie(f); guardar(f, "paso0_caso.png")

# 2. reparto de población
_rb = gpd.GeoSeries(fp.reindex(res_sec.edif_id).geometry.dropna().values, crs=fp.crs).total_bounds
sb = huella.buffer(170).bounds  # entorno del edificio del ejemplo (la sección puede ser muy extensa)
scx, scy = (sb[0] + sb[2]) / 2, (sb[1] + sb[3]) / 2; sr = (sb[3] - sb[1]) * .5
f, ax = lienzo(scx, scy, sr, "Paso 1 · Cuántas personas viven en el edificio",
               f"La población de la sección censal {cs} se reparte entre sus edificios según su número de viviendas")
fondo(ax, red=False, bbox=(scx - 2 * sr, scy - sr, scx + 2 * sr, scy + sr))
r = res_sec.copy(); r["geometry"] = fp.reindex(r.edif_id).geometry.values; r = gpd.GeoDataFrame(r, geometry="geometry", crs=fp.crs)
r = r[r.geometry.notna()]
r.plot(ax=ax, column="n_viviendas", cmap="Greens", vmin=0, vmax=max(r.n_viviendas.max(), 1) * 1.15, edgecolor="#7d8a80", linewidth=.4, zorder=3)
gpd.GeoSeries([secg]).plot(ax=ax, facecolor="none", edgecolor=TX, linewidth=1.6, linestyle="--", zorder=4)
gpd.GeoSeries([huella]).plot(ax=ax, facecolor="none", edgecolor=TX, linewidth=2.2, zorder=6)
cuenta = (f"Sección {cs}: {pob_sec:,} habitantes (censo 2025)\n{viv_sec:,} viviendas en {len(res_sec)} edificios residenciales\n\n"
          f"Este edificio: {caso['viviendas']} viviendas\n{caso['viviendas']} / {viv_sec:,} × {pob_sec:,} = {caso['poblacion']:.0f} personas").replace(",", ".")
ax.text(.015, .97, cuenta, transform=ax.transAxes, va="top", fontsize=10.5, color=TX, zorder=30,
        bbox=dict(boxstyle="round,pad=.6", fc="white", ec="#D5D9DE", lw=.8))
ax.legend(handles=[Line2D([], [], color=TX, lw=1.6, ls="--", label="Límite de la sección censal (INE)"),
                   Patch(facecolor="#9dd09f", edgecolor="#7d8a80", label="Edificio residencial (más oscuro = más viviendas)"),
                   Patch(facecolor="none", edgecolor=TX, lw=2, label="Edificio del ejemplo")], loc="lower right", framealpha=.95, edgecolor="#D5D9DE", fontsize=9.5)
escala(ax, 100); pie(f); guardar(f, "paso1_poblacion.png")

# 3. puntos de acceso
hb = huella.bounds; ar = max(hb[2] - hb[0], hb[3] - hb[1]) * .5 + RADIO + 25
f, ax = lienzo(hx, hy, ar, "Paso 2 · Por dónde se entra a la red peatonal",
               f"Vale cualquier punto de la red a {RADIO:.0f} m o menos de la fachada (y, de respaldo, la calle más cercana al punto interior)")
fondo(ax, bbox=(hx - 2 * ar, hy - ar, hx + 2 * ar, hy + ar))
gpd.GeoSeries([huella.buffer(RADIO)]).plot(ax=ax, facecolor="#2fa35a14", edgecolor=VERDE, linewidth=1, linestyle="--", zorder=3)
gpd.GeoSeries([huella]).plot(ax=ax, color="#BFE3C8", edgecolor=TX, linewidth=1.2, zorder=5)
# enganche del punto interior: arista mas cercana y proyeccion
eg = STRtree(ed.geometry.values).nearest(pint); ln = ed.geometry.values[eg]; proy = ln.interpolate(ln.project(pint))
gpd.GeoSeries([ln]).plot(ax=ax, color=TX2, linewidth=2.6, zorder=6)
ax.plot([pint.x, proy.x], [pint.y, proy.y], color=TX2, lw=1.2, ls=":", zorder=7)
ax.scatter([pint.x], [pint.y], s=55, marker="X", color=TX, zorder=12)
xs, ys = pts(opc_n[:2]); ax.scatter(xs, ys, s=46, color="white", edgecolor=TX, linewidth=1.4, zorder=11)
xb, yb = pts(opc_n[es_borde]); ax.scatter(xb, yb, s=46, color=VERDE, edgecolor="white", linewidth=1, zorder=11)
ax.scatter([nx_[opc_n[kb]]], [ny_[opc_n[kb]]], s=190, facecolor="none", edgecolor=TX, linewidth=1.6, zorder=12)
rotulo(ax, nx_[opc_n[kb]], ny_[opc_n[kb]], f"El que acabará siendo el mejor: a {opc_o[kb]:.0f} m de la fachada", dx=-ar * .05, dy=ar * .5, ha="center")
rotulo(ax, pint.x, pint.y, f"Punto interior: a {caso['d_perp_m']:.0f} m de la calle más cercana", dx=hx - pint.x, dy=huella.bounds[1] - pint.y - ar * .1, ha="center")
ax.text(.015, .97, f"{caso['opciones_borde']} puntos de la red a 30 m o menos de la fachada\n(a cada uno se le suma su distancia hasta el borde)\n+ 2 de respaldo: los extremos de la calle más cercana\nal punto interior", transform=ax.transAxes, va="top", fontsize=9.8, zorder=30,
        bbox=dict(boxstyle="round,pad=.5", fc="white", ec="#D5D9DE", lw=.8))
ax.legend(handles=[Patch(facecolor="#BFE3C8", edgecolor=TX, label="Huella del edificio"),
                   Patch(facecolor="#2fa35a14", edgecolor=VERDE, ls="--", label=f"Franja de {RADIO:.0f} m alrededor de la fachada"),
                   Line2D([], [], marker="o", ls="", markerfacecolor=VERDE, markeredgecolor="white", markersize=8, label="Acceso por la fachada (+ metros hasta el borde)"),
                   Line2D([], [], marker="X", ls="", color=TX, markersize=8, label="Punto interior del edificio"),
                   Line2D([], [], color=TX2, lw=2.6, label="Calle más cercana al punto interior"),
                   Line2D([], [], marker="o", ls="", markerfacecolor="white", markeredgecolor=TX, markersize=8, label="Extremos de esa calle (accesos de respaldo)")],
          loc="lower right", framealpha=.95, edgecolor="#D5D9DE", fontsize=8.8)
escala(ax, 25); pie(f); guardar(f, "paso2_accesos.png")

# 4. enganche de la estación
er = 60
f, ax = lienzo(ex, ey, er, "Paso 3 · La estación se engancha a la red",
               "Se busca el nodo de la red más cercano a la estación y se suma esa distancia")
fondo(ax, bbox=(ex - 2 * er, ey - er, ex + 2 * er, ey + er))
ax.plot([ex, nx_[sn[j]]], [ey, ny_[sn[j]]], color=AZUL, lw=1.6, ls=(0, (3, 2)), zorder=8)
ax.scatter([nx_[sn[j]]], [ny_[sn[j]]], s=46, color="white", edgecolor=AZUL, linewidth=1.6, zorder=11)
ax.scatter([ex], [ey], s=150, color=AZUL, edgecolor="white", linewidth=1.8, zorder=12)
rotulo(ax, ex, ey, f"Estación «{caso['estacion'].title()}»", dx=er * .12, dy=-er * .14, peso="bold")
rotulo(ax, nx_[sn[j]], ny_[sn[j]], f"Nodo de la red más cercano: a {caso['enganche_estacion_m']:.0f} m", dx=-er * .12, dy=er * .16, ha="right")
escala(ax, 10); pie(f); guardar(f, "paso3_estacion.png")

# 5. camino mas corto
f, ax = lienzo(mx, my, R0, "Paso 4 · El camino más corto por la red peatonal",
               "Se calcula el recorrido mínimo desde la estación hasta cada acceso del edificio y se queda el mejor")
fondo(ax, bbox=bb)
gpd.GeoSeries([huella]).plot(ax=ax, color="#BFE3C8", edgecolor=TX, linewidth=1, zorder=5)
xi, yi = pts(cam_i); ax.plot(xi, yi, color=AMAR, lw=3.2, zorder=7, solid_capstyle="round")
xm, ym = pts(cam_b); ax.plot(xm, ym, color=VERDE, lw=3.6, zorder=8, solid_capstyle="round")
ax.plot([pint.x, nx_[opc_n[kint]]], [pint.y, ny_[opc_n[kint]]], color=AMAR, lw=1.4, ls=":", zorder=7)
ax.scatter([nx_[opc_n[kb]]], [ny_[opc_n[kb]]], s=50, color=VERDE, edgecolor="white", zorder=11)
ax.scatter([pint.x], [pint.y], s=50, marker="X", color=TX, zorder=12)
ax.scatter([ex], [ey], s=110, color=AZUL, edgecolor="white", linewidth=1.6, zorder=12)
rotulo(ax, xm[len(xm) // 2], ym[len(ym) // 2], f"Mejor acceso: {caso['red_mejor_acceso_m']} m", dx=R0 * .12, dy=R0 * .12, color=TX, peso="bold")
_solo = [k for k in range(len(cam_i)) if cam_i[k] not in set(cam_b)] or [0]; _k = _solo[len(_solo) // 2]
rotulo(ax, xi[_k], yi[_k], f"Desde el punto interior: {caso['red_punto_interior_m']} m", dx=-R0 * .05, dy=-R0 * .22, ha="center")
ax.legend(handles=[Line2D([], [], color=VERDE, lw=3.6, label="Recorrido hasta el mejor acceso por la fachada"),
                   Line2D([], [], color=AMAR, lw=3.2, label="Recorrido si solo se usara el punto interior"),
                   Line2D([], [], marker="o", ls="", color=AZUL, markersize=9, label="Estación")],
          loc="lower right", framealpha=.95, edgecolor="#D5D9DE", fontsize=9.5)
escala(ax, 100); pie(f); guardar(f, "paso4_camino.png")

# 6. resultado
f, ax = plt.subplots(figsize=(10, 4.6), dpi=150); ax.axis("off")
ax.set_title("Paso 5 · La distancia del edificio y su nivel", pad=14)
filas = [("En línea recta (no se usa)", caso["recta_m"], TX3), ("Por la red, desde el punto interior", caso["red_punto_interior_m"], AMAR),
         ("Por la red, desde el mejor acceso (la que se usa)", caso["red_mejor_acceso_m"], VERDE)]
mxd = max(720, max(v for _, v, _ in filas) * 1.15)
for k, (t, v, c) in enumerate(filas):
    y = 2 - k
    ax.barh(y, v, height=.42, color=c, zorder=3); ax.text(-8, y, t, ha="right", va="center", fontsize=10.5)
    ax.text(v + 8, y, f"{v} m", va="center", fontsize=10.5, fontweight="bold" if k == 2 else "normal")
for x, t in ((250, "250 m"), (500, "500 m")):
    ax.axvline(x, color=TX2, lw=1, ls="--", zorder=2); ax.text(x, 2.62, t, ha="center", fontsize=9.5, color=TX2)
ax.axvspan(0, 250, color=VERDE, alpha=.08, zorder=1); ax.axvspan(250, 500, color=AMAR, alpha=.1, zorder=1); ax.axvspan(500, mxd, color=ROJO, alpha=.07, zorder=1)
ax.text(125, -.75, "verde: menos de 250 m", ha="center", fontsize=9.5, color=TX2); ax.text(375, -.75, "amarillo: 250–500 m", ha="center", fontsize=9.5, color=TX2)
ax.text((500 + mxd) / 2, -.75, "rojo: más de 500 m", ha="center", fontsize=9.5, color=TX2)
ax.set_xlim(-330, mxd); ax.set_ylim(-1.05, 2.85)
pie(f, f"Se suman: {caso['enganche_estacion_m']:.0f} m de la estación a la red + recorrido por la red + {caso['desfase_mejor_m']:.0f} m del punto de la red a la fachada")
guardar(f, "paso5_resultado.png")
