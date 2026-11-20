"""Ejecuta el pipeline de uno o varios sistemas: python pipeline/run_all.py rivas valencia | --todos
Al final regenera la pagina matriz (09_matriz.py)."""
import subprocess, sys, os, json, time
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(D)
TODOS = [s["id"] for s in json.load(open(os.path.join(R, "sistemas.json"), encoding="utf-8"))["sistemas"]]
args = sys.argv[1:]
desde = next((a.split("=",1)[1] for a in args if a.startswith("--desde=")), None)
sis = TODOS if (not args or "--todos" in args) else [a for a in args if not a.startswith("-")]
PASOS = ["01_estaciones", "01_ine", "01_limites", "01_catastro", "01_osm", "01_direcciones", "02_preparacion", "03_reparto_poblacion",
         "04_distancias", "05_agregados", "06_exportar_web", "07_ranking_bases", "08_ampliacion"]
fallos = []
for s in sis:
    os.makedirs(os.path.join(R, "logs"), exist_ok=True)
    with open(os.path.join(R, "logs", s + ".log"), "w", encoding="utf-8") as log:
        pasos = PASOS[PASOS.index(desde):] if desde else PASOS
        if "04_distancias" in pasos:  # las distancias cambian: la cobertura cacheada de la ampliacion ya no vale
            from pathlib import Path
            pr = Path(R) / "data" / s / "processed"
            for f in list(pr.glob("ampliacion_cobertura_*.npz")) + [pr / "ampliacion_resultado.pkl"]:
                if f.exists(): f.unlink()
        for p in pasos:
            t0 = time.time(); print(f"== {s} · {p}", flush=True)
            r = subprocess.run([sys.executable, os.path.join(D, p + ".py")], cwd=R, env={**os.environ, "SISTEMA": s},
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            log.write(f"== {p} ({round(time.time() - t0)} s)\n{r.stdout}\n"); log.flush()
            if r.returncode:
                print(r.stdout[-2500:]); fallos.append((s, p)); break
subprocess.run([sys.executable, os.path.join(D, "09_matriz.py")], cwd=R)
print("fallos:", fallos or "ninguno")
sys.exit(1 if fallos else 0)
