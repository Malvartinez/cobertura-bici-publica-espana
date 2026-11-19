# Cobertura de la bici pública en España

Calcula, para los sistemas de bicicleta pública de las grandes ciudades españolas, qué población vive a menos de
250 m (verde), entre 250 y 500 m (amarillo) o a más de 500 m (rojo) andando de la estación más cercana. Las
distancias se miden sobre la red peatonal real, no en línea recta. Una página matriz compara todos los sistemas y
enlaza a la web de cada uno, con mapa, rankings de zonas y estaciones y un simulador de ampliación.

Web: https://malvartinez.github.io/cobertura-bici-publica-espana/

Amplía a todo el país los análisis de [Madrid](https://github.com/Malvartinez/cobertura-poblacion-bicimad) y
[Barcelona](https://github.com/Malvartinez/cobertura-poblacion-bicing), con el mismo método.

## Sistemas incluidos

23 sistemas con estaciones fijas de capitales de provincia y municipios de más de 100.000 habitantes, más
BiciNRivas: BiciMAD (Madrid), Bicing (Barcelona), Bizi (Zaragoza), Valenbisi (València), Sevici (Sevilla), Bicielx
(Elche), Bicipalma (Palma), BIKI (Valladolid), BiciCoruña (A Coruña), Dbizi (Donostia), Bilbaobizi (Bilbao),
Sítycleta (Las Palmas de Gran Canaria), Bicicas (Castelló), nextbike (León), Gijón Bici, TUeBICI (Santander),
Girocleta (Girona), BiciLog (Logroño), AlbaBici (Albacete), BiBa (Badajoz), Ganxeta (Reus), MugiBIKE
(Vitoria-Gasteiz) y BiciNRivas (Rivas-Vaciamadrid).

Quedan fuera los sistemas metropolitanos, los que no tienen estaciones, Pamplona (suspendido), Málaga (en
licitación), Murcia y Burgos. Detalle en [`docs/decisiones.md`](docs/decisiones.md).

## Qué ofrece la web

- **Página matriz**: tabla ordenable con población, estaciones, habitantes por estación, reparto verde/amarillo/rojo
  y estaciones nuevas necesarias para llegar al 80 % de la población a menos de 250 m.
- **Página de cada sistema**: coropleta por sección censal, barrio o distrito; edificios del Catastro coloreados por
  nivel a partir de zoom 14; ranking de zonas y de estaciones; simulador de ampliación; tabla descargable en CSV.

## Fuentes

- **Estaciones**: feeds GBFS oficiales (`station_information`) o, si el operador no publica uno, la API de CityBikes.
- **Población**: INE, Censo anual de población 2025 por sección censal (servicio ArcGIS de Esri España) y cartografía
  de secciones censales 2025.
- **Edificios**: Catastro INSPIRE Buildings (DG del Catastro). En Bilbao, Donostia y Vitoria, los catastros forales de
  Bizkaia, Gipuzkoa y Álava.
- **Zonas**: barrios oficiales del ayuntamiento cuando se han podido descargar (Madrid, Barcelona, Zaragoza, València y
  Sevilla); en el resto, distritos censales del INE.
- **Red peatonal**: OpenStreetMap, extractos de download.openstreetmap.fr con el filtro `network_type="walk"` de OSMnx.
- **Mapa base**: CARTO.

## Método

1. Reparto de la población de cada sección censal entre sus edificios residenciales, proporcional al número de
   viviendas (la suma cuadra exactamente con el censo).
2. Acceso de cada edificio a la red por su mejor punto: la arista más cercana a su punto interior o cualquier nodo a
   30 m o menos de su huella, sumando la distancia hasta el borde (mismo criterio que BicinRivas). Cada estación se
   engancha al nodo más cercano, sumando esa distancia.
3. Dijkstra multiorigen desde todas las estaciones, con corte a 1.500 m.
4. Agregados por municipio, distrito, barrio y sección; ranking de estaciones (Dijkstra desde cada una, corte 500 m).
5. Ampliación: algoritmo voraz con evaluación perezosa (CELF) sobre los nodos de la red (uno por celda de 50 m),
   maximizando la mejora ponderada por persona (rojo→amarillo +1, amarillo→verde +1, rojo→verde +2).

Las validaciones de cada sistema (distancias frente a rutas individuales y ampliación recalculada desde cero) están en
`docs/sistemas/<id>/`.

## Cómo reproducir

```bash
pip install -r requirements.txt
python pipeline/run_all.py --todos
```

Hace falta `osmium-tool` en el `PATH` (`apt install osmium-tool`). Para un solo sistema:
`python pipeline/run_all.py valencia`; para retomar desde un paso: `--desde=04_distancias`. Al final se regenera
`web/sistemas.json`, que alimenta la página matriz.

Para añadir un sistema basta con una entrada nueva en `sistemas.json` (código INE, código catastral, fuente de
estaciones, extracto OSM, fuente de límites, EPSG del huso UTM y máximo del simulador).

Para ver la web en local hace falta un servidor que admita peticiones `Range` (las usa PMTiles); por ejemplo,
`npx http-server web -p 8000`.

## Estructura del repositorio

```
sistemas.json     configuración de cada sistema
pipeline/         scripts numerados (01 descargas, 02–08 cálculo, 09 matriz); comun.py lee el sistema activo
web/index.html    página matriz (lee web/sistemas.json)
web/app/          aplicación común de cada sistema (app.js, styles.css, plantilla sistema.html)
web/<id>/         página y datos de cada sistema
docs/             decisiones y validaciones por sistema
data/             descargas y capas intermedias (no versionado)
```

## Despliegue

GitHub Actions (`.github/workflows/pages.yml`) publica `web/` en GitHub Pages en cada push a `main` que toque `web/`.

## Limitaciones

- Los porcentajes dependen del término municipal completo: los municipios con mucho suelo rural o de monte (Zaragoza,
  Badajoz, Albacete, Vitoria…) tienen población dispersa lejos de cualquier estación.
- La distancia no considera la pendiente.
- En los catastros forales, residencial = edificio con viviendas (no publican el uso de forma homogénea).
- La ampliación es un ejercicio de máxima cobertura residencial: no considera viabilidad, demanda, topografía ni coste.

## Licencia y atribución

- Datos de los operadores, ayuntamientos, INE, Catastro y diputaciones forales: citar la fuente y respetar sus
  condiciones de reutilización.
- Red peatonal: © colaboradores de OpenStreetMap, bajo licencia ODbL. Mapa base © CARTO.
