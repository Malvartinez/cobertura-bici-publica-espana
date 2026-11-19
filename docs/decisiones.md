# Decisiones

Ampliación a los sistemas de bicicleta pública de las grandes ciudades españolas de
[cobertura-poblacion-bicimad](https://github.com/Malvartinez/cobertura-poblacion-bicimad) y
[cobertura-poblacion-bicing](https://github.com/Malvartinez/cobertura-poblacion-bicing). El método es el mismo
(umbrales 250/500 m, corte 1.500 m, reparto por viviendas, Dijkstra multiorigen, ranking con solapes, ampliación
CELF); aquí se anotan las decisiones propias de la versión multisistema. Formato: qué y por qué.

## Alcance

- Sistemas con estaciones fijas de capitales de provincia y municipios de más de 100.000 habitantes, más BiciNRivas por petición expresa — criterio acordado con el usuario («solo los grandes»).
- Inventario de partida: CityBikes (77 redes en España, noviembre de 2026), contrastado con prensa y webs municipales.
- Fuera: sistemas metropolitanos (AMBici, MIBISI, Bizkaibizi), salvo que la parte fuera del municipio sea mínima (BiciMAD); sistemas sin estaciones (Dott en Murcia, Tarragona e Ibiza); Pamplona (servicio suspendido desde el 13-2-2026, el nuevo está previsto para 2027); Málaga (MálagaBici en licitación); Murcia (MUyBICI retiró las estaciones); Burgos (solo 2 estaciones en CityBikes).
- Vitoria-Gasteiz se incluye pese a tener solo 12 estaciones (MugiBIKE, desde diciembre de 2025): es el sistema municipal vigente.

## Estructura

- Un solo repositorio y una sola web: la página matriz en la raíz y cada sistema en `web/<id>/`, con la aplicación común en `web/app/` — mantener un único código; el tamaño estimado (~150–200 MB) está muy por debajo de los límites de GitHub (1 GB recomendado por repositorio y por sitio de Pages, 100 MB por fichero).
- Configuración por sistema en `sistemas.json`; los scripts leen el sistema activo de la variable `SISTEMA` (`pipeline/comun.py`).
- Madrid y Barcelona se regeneran aquí con el mismo código y la misma fecha de datos; sus repositorios originales se mantienen y enlazan a este.

## Fuentes

- Estaciones: feed GBFS oficial (`station_information`) cuando el operador lo publica (Madrid, Barcelona, Zaragoza, Valencia, Sevilla, A Coruña, Bilbao, Donostia, Vitoria, Rivas); si no, la API de CityBikes. Se excluyen estaciones virtuales.
- Población: INE, Censo anual de población 2025 por sección censal (servicio ArcGIS de Esri España) y cartografía de secciones 2025. El área de análisis es el término municipal = unión de sus secciones censales.
- Edificios: Catastro INSPIRE Buildings de la DG del Catastro. País Vasco: catastros forales (Bizkaia por municipio, Araba y Gipuzkoa por provincia, recortando el municipio por punto interior). En los forales se considera residencial todo edificio con viviendas, porque no publican el uso de forma homogénea; los tres publican `numberOfDwellings`.
- Red peatonal: extractos de `download.openstreetmap.fr` (autonómicos o provinciales), recortados con `osmium extract` al municipio + 1 km y filtrados con el mismo criterio que OSMnx usa para `network_type="walk"` — Overpass y Geofabrik cortan la conexión desde el entorno de cálculo.
- Vías cortadas por el borde del extracto (frontera con Portugal en Badajoz): se parten en tramos de nodos presentes, nunca se unen huecos.
- Zonas: barrios oficiales cuando se han podido descargar (Madrid, Barcelona, Zaragoza); en el resto, distritos censales del INE con el nombre «Distrito N» y sin nivel de barrio. Se intentó con Valencia (el dominio de Opendatasoft ya no existe y el portal CKAN rechaza la conexión), Sevilla, Bilbao, Donostia, Vitoria y Palma, sin una descarga accesible.
- Zaragoza: el nivel de barrio son las juntas municipales y vecinales (29), con nombres capitalizados.

## Método

- Cortes de sombreado de edificios fijos para todas las ciudades (3, 8, 22 y 43 hab.) — con cuantiles por ciudad salían cortes repetidos en ciudades de vivienda unifamiliar (Rivas: todos 3) y la leyenda no era comparable.
- Simulador de ampliación con un máximo por sistema (`kmax` en `sistemas.json`): 1.000 en Madrid, 500 en las ciudades grandes, 400 en las medianas que no llegan al 80 % con 200, y 100–200 en las pequeñas.
- Indicador comparativo «nuevas para 80 %»: primera k de la curva del simulador con al menos el 80 % de la población a menos de 250 m.

## Incidencias de datos

- Catastro corta conexiones de forma intermitente: todas las descargas tienen reintentos y se comprueba que el ZIP sea válido.
- Los feeds ATOM provinciales del Catastro pueden venir en Latin-1 (A Coruña, Logroño, con «Ñ» en la ruta): se decodifican como tal antes de extraer la URL.

## Web

- `.gitignore` anclado a la raíz (`/data/`) — el patrón `data/` excluía también `web/<sistema>/data/` y la primera publicación salió sin datos en las 23 páginas.
- Encuadre inicial del mapa = 99 % central de los edificios habitados, no el término municipal — Castellón (islas Columbretes), Palma (Cabrera) y los municipios con mucho diseminado rural arrancaban demasiado alejados.
- Si la vista guardada en la URL (`#zoom/lat/lon`) cae fuera de la ciudad, se descarta — una recarga durante el arranque del mapa podía dejar `#8/0/0` y el mapa en blanco en las recargas siguientes.
