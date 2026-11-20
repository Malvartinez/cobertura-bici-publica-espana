# Handoff — cobertura-bici-publica-espana

## Qué es
Cobertura peatonal de estaciones de bici pública en 34 sistemas municipales españoles.
- Web: https://malvartinez.github.io/cobertura-bici-publica-espana/
- Repos hermanos: cobertura-poblacion-bicimad y cobertura-poblacion-bicing (enlazan aquí; tienen su propio `_acceso.py`).

## Cómo se ejecuta
- Entorno: `.venv` en la raíz (geopandas, osmnx 2.x, pyosmium, scipy, matplotlib). Requiere osmium-tool.
- `python pipeline/run_all.py <ids> | --todos [--desde=PASO]`
  - logs en `logs/<id>.log`;
  - borra las cachés de ampliación si se ejecuta 04;
  - al final ejecuta 09_matriz.
- Sistema activo en la variable `SISTEMA` (`pipeline/comun.py`: P, W, D, RAW, COMUN, EPSG, CRS, `get()` con reintentos y `stream_to`).
- Figuras de metodología (manual): `SISTEMA=zaragoza python pipeline/10_figuras_metodologia.py [edif_id]` (por defecto 6674803XM7167D).
- `data/` (raw/processed por sistema, más `_comun`) no está en git.
- Despliegue: push a main → Pages (workflow en dos jobs, carpeta `web/`).

## Pasos
- **01_*** — descargas:
  - `01_estaciones` (GBFS o CityBikes);
  - `01_ine` (secciones y censo 2025, municipio.gpkg);
  - `01_limites` (madrid | barcelona | ine | capas | secciones_zonas);
  - `01_catastro` (nacional ATOM o foral);
  - `01_osm` (extracto → filtro walk → grafo).
- **02/03** — población por edificio (reparto por viviendas de la sección).
- **04_distancias** — Dijkstra multiorigen desde las estaciones (cutoff 1600) y mejor acceso por edificio (`_acceso.py`); validación con networkx.
- **05** — agregados por zona.
- **06_exportar_web** — metadata, bbox por cuantiles, `web/<id>/index.html` desde `web/app/sistema.html`.
- **07_ranking_bases** — ranking de estaciones con solapes.
- **08_ampliacion** — CELF, `kmax` en sistemas.json; valida con k = 0, min(100, K) y K.
- **09_matriz** — `web/sistemas.json` y `docs/resultados.md`.

## Método de acceso vigente (`pipeline/_acceso.py`, desde 2026-11-20)
- **Con portal** (Catastro INSPIRE Addresses, `Entrance`, paso `01_direcciones` → `portales.parquet` con la arista de acceso de cada portal): opciones = los dos extremos de la arista de cada portal (desfase = portal-arista + tramo). Sustituyen a las de borde.
- **Sin portal** (y forales): método de borde, RADIO = 30 — extremos de la arista más cercana al punto interior + nodos a ≤ 30 m de la huella con su distancia al borde.
- La distancia es el mínimo; `minimo(vals, ini)` usa `np.minimum.reduceat`. `accesos(..., portales=False)` da el método de borde (lo usa 10_figuras para comparar).
- La estación se engancha al nodo más cercano y se suma ese tramo. Usado por 04, 07 y 08.
- Resultados < 250 m: Zaragoza 71,0 %, Barcelona 72,8 %, València 69,8 %, Madrid 40,3 %, Rivas 38,8 % (tabla completa antes/después en `docs/decisiones.md`).

## Mejoras abiertas
1. **Acceso por portal catastral**: hecho el 2026-11-20 (solo portal, decisión del usuario) en los tres repos cobertura-*. Pendiente en **BicinRivas**: spec `docs/specs/acceso-portal-catastral.md` en borrador (rama `claude/loving-meitner-94biex`), a falta de aprobación; allí no hay datos en este entorno y su CLAUDE.md exige spec antes de cambiar una cifra publicada. En Rivas, el 92 % de los edificios residenciales (97 % de la población) tiene portal.
2. **Enganche de la estación** al punto exacto de la arista en vez de al nodo (mediana 7–9 m; > 25 m en 214 de 3.212 estaciones). Propuesto, no aprobado.
3. **Barrios pendientes**: Donostia, Vitoria, Bilbao y A Coruña (servidores inaccesibles desde el entorno; basta añadir una capa `capas` en sistemas.json).

## Trampas conocidas
- Overpass y Geofabrik bloqueados: usar download.openstreetmap.fr.
- datos.gob.es necesita User-Agent de navegador.
- El feed ATOM del Catastro puede venir en Latin-1; Gijón está en la gerencia 52 ("52024-GIJON"); el Catastro corta conexiones (reintentos y comprobar que el ZIP es válido).
- En 04/07/08, `D` es la matriz de distancias: importar las rutas de docs como `DOCS`.
- `.gitignore` anclado: `/data/`.
- No borrar con `rm -rf` fuera de la carpeta del proyecto (bloqueado por seguridad).

## Convenciones
- Español en todo.
- Decisiones en `docs/decisiones.md` (qué y por qué).
- Commits con user Claude / noreply@anthropic.com y las líneas `Co-Authored-By` y `Claude-Session`.
- Push solo a main de los repos cobertura-*.
- Sin PR salvo petición.
- No exponer datos personales del usuario.
