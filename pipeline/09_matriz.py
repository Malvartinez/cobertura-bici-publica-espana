"""09 - Resumen comparativo de todos los sistemas ya calculados -> web/sistemas.json (lo lee la pagina matriz)."""
import json, os, datetime
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; os.chdir(ROOT)
cfg = json.load(open("sistemas.json", encoding="utf-8"))["sistemas"]
out = []
for s in cfg:
    w = Path("web") / s["id"] / "data"; p = Path("data") / s["id"] / "processed"
    if not (w / "agregados.json").exists() or not (w / "metadata.json").exists(): continue
    ag = json.load(open(w / "agregados.json", encoding="utf-8"))["ciudad"]
    md = json.load(open(w / "metadata.json", encoding="utf-8"))
    nb = len(json.load(open(w / "bases.geojson", encoding="utf-8"))["features"])
    ine = json.load(open(p / "meta_ine.json", encoding="utf-8")) if (p / "meta_ine.json").exists() else {}
    lim = json.load(open(p / "meta_limites.json", encoding="utf-8")) if (p / "meta_limites.json").exists() else {}
    cat = json.load(open(p / "meta_catastro.json", encoding="utf-8")) if (p / "meta_catastro.json").exists() else {}
    k80 = k90 = None
    if (w / "ampliacion_curva.json").exists():
        c = json.load(open(w / "ampliacion_curva.json", encoding="utf-8"))
        f = [v / c["total"] for v in c["v"]]
        k80 = next((k for k, x in enumerate(f) if x >= .8), None); k90 = next((k for k, x in enumerate(f) if x >= .9), None)
    area = ine.get("area_km2")
    out.append({"id": s["id"], "sistema": s["sistema"], "ciudad": s["ciudad"], "estaciones": nb, "poblacion": ag["pob"],
                "pob_v": ag["pob_v"], "pob_a": ag["pob_a"], "pob_r": ag["pob_r"], "pct_v": ag["pct_v"], "pct_a": ag["pct_a"], "pct_r": ag["pct_r"],
                "area_km2": area, "hab_por_estacion": round(ag["pob"] / nb) if nb else None,
                "estaciones_km2": round(nb / area, 2) if area and nb else None, "est_10k": round(1e4 * nb / ag["pob"], 2) if ag["pob"] else None,
                "nuevas_80": k80, "nuevas_90": k90, "kmax": s["kmax"], "centro": md.get("centro"),
                "barrios_oficiales": bool(lim.get("fuente_barrios")), "zonas": lim.get("fuente_barrios") or lim.get("fuente_distritos"),
                "catastro": "foral" if cat.get("tipo") in ("bizkaia", "araba", "gipuzkoa") else "nacional", "generado": md.get("generado")})
out.sort(key=lambda x: -x["poblacion"])
json.dump({"generado": datetime.date.today().isoformat(), "sistemas": out}, open("web/sistemas.json", "w", encoding="utf-8"),
          ensure_ascii=False, separators=(",", ":"))
print("matriz:", len(out), "sistemas")

# tabla de resultados en docs/resultados.md
f1 = lambda x: f"{x:.1f}".replace(".", ",") + " %"
mil = lambda x: f"{x:,}".replace(",", ".")
filas = sorted(out, key=lambda x: -x["pct_v"])
md = ["# Resultados", "", f"Datos generados el {datetime.date.today().isoformat()}. Población: INE, Censo anual de población a 1 de enero de 2025.",
      "Distancia andando por la red peatonal a la estación más cercana. Ordenado por % de población a menos de 250 m.", "",
      "| Ciudad | Sistema | Población | Estaciones | Hab./estación | < 250 m | 250–500 m | > 500 m | Nuevas para 80 % |",
      "|---|---|---:|---:|---:|---:|---:|---:|---:|"]
for r in filas:
    md.append(f"| {r['ciudad']} | {r['sistema']} | {mil(r['poblacion'])} | {r['estaciones']} | {mil(r['hab_por_estacion'])} | {f1(r['pct_v'])} | "
              f"{f1(r['pct_a'])} | {f1(r['pct_r'])} | {r['nuevas_80'] if r['nuevas_80'] is not None else '—'} |")
P_ = sum(r["poblacion"] for r in out); V_ = sum(r["pob_v"] for r in out); R_ = sum(r["pob_r"] for r in out)
md += ["", f"Conjunto: {mil(P_)} habitantes en {len(out)} municipios; {f1(100 * V_ / P_)} a menos de 250 m y {f1(100 * R_ / P_)} a más de 500 m.", ""]
open("docs/resultados.md", "w", encoding="utf-8").write("\n".join(md))
