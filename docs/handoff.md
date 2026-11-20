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

## Método de acceso vigente (`pipeline/_acceso.py`, RADIO = 30)
- Opciones de cada edificio:
  - los dos extremos de la arista más cercana a su punto interior;
  - todos los nodos a ≤ 30 m de la huella, sumando la distancia del nodo al borde.
- La distancia es el mínimo; `minimo(vals, ini)` usa `np.minimum.reduceat`.
- La estación se engancha al nodo más cercano y se suma ese tramo.
- Usado por 04, 07 y 08.
- Resultados < 250 m: Zaragoza 75,7 %, Barcelona 74,1 %, València 73,9 %, Madrid 44,1 %, Rivas 43,6 %.

## Mejoras abiertas
1. **Acceso por dirección catastral** (propuesta del usuario, 2026-11-20), en curso:
   - Catastro INSPIRE Addresses (AD): ATOM `INSPIRE/addresses/{pr}/ES.SDGC.ad.atom_{pr}.xml` (comprobar), puntos de portal con nombre de vía y referencia a la parcela o edificio (comprobar los campos).
   - Enlace al edificio: la referencia catastral (14 caracteres) del `localId`.
   - Emparejar el nombre de la vía con el `name` de OSM, normalizado.
   - Acceso = proyección del punto de portal sobre la arista de esa calle, más el desfase. Varias direcciones: mínimo. Sin dirección o sin emparejamiento: método de borde.
   - Forales: comprobar si publican AD.
   - Medir antes/después en las 34 ciudades; actualizar la metodología y `docs/decisiones.md`; preguntar si se aplica también a los repos de Madrid y Barcelona.
   - **Hallazgos del prototipo en Zaragoza (2026-11-20)**:
     - Feed confirmado: entrada `50900-ZARAGOZA addresses` → `INSPIRE/Addresses/50/50900-ZARAGOZA/A.ES.SDGC.AD.50900.zip` (74 MB, GML en **ISO-8859-1**).
     - 50.606 direcciones: 33.895 `specification=Entrance` (portal sobre la fachada) y 16.711 `Parcel`.
     - `localId` = `50.900.<via>.<numero>.<refcat14>`; el nombre de la vía está en `AD:ThoroughfareName` (`CL ABANTO, MARTIN DE`, a veces con sufijo de barrio `(JSL)`).
     - El 81 % de los edificios residenciales tiene portal (88 % de la población). Distancia del portal a la huella: mediana 0 m, p90 2,7 m.
     - Solo el 39 % de las aristas OSM tiene nombre (aceras y sendas sin nombre). La arista más cercana al portal ya es su calle en el 65 % de los casos; emparejar por nombre solo corrige esquinas (2,4 %) y apenas cambia el resultado.
     - Zaragoza < 250 m: 75,7 % con el método de borde → 71,2 % solo con portal.
     - Problema detectado: el Catastro da una sola dirección por parcela, así que las manzanas cerradas y los conjuntos grandes quedan con un único portal aunque tengan varios.
     - Viviendas por portal: p50 4, p95 36. Regla híbrida: portal si ≤ 40 viviendas por portal, borde si no → 73,4 % (30 → 73,9 %; 60 → 72,6 %).
     - Forales: Bizkaia (`ES.BFA.AD.<mun>.zip`) y Gipuzkoa (`ES.GFA.AD.zip`) existen; Álava, sin localizar (la ruta AD análoga da 404).
     - Scripts del prototipo (fuera del repo, en el scratchpad de la sesión): `parse_ad.py` (regex sobre el GML), `proto.py` (comparación) y `plot.py`.
   - Pendiente: la decisión del usuario sobre la regla (híbrida con umbral o solo portal) antes de integrarla (01_direcciones, nombres de arista y `_acceso.py`) y recalcular los 34 sistemas.
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
