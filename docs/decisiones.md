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
- Zonas: barrios oficiales cuando se han podido descargar (Madrid, Barcelona, Zaragoza, València y Sevilla); en el resto, distritos censales del INE con el nombre «Distrito N» y sin nivel de barrio. En Bilbao, Donostia, Vitoria y Palma no se encontró una descarga accesible.
- València: distritos (19) y barrios (87) del servidor ArcGIS del geoportal municipal (`OPENDATA/UrbanismoEInfraestructuras`, capas 225 y 224), localizados a través de datos.gob.es (su API exige una cabecera de navegador). El antiguo dominio de Opendatasoft ya no existe.
- Sevilla: barrios (110) de la IDE Sevilla (Gerencia de Urbanismo, CC BY 4.0, junio de 2024), publicados en ArcGIS (`Barrios_de_Sevilla`). Los distritos (11) se construyen uniendo sus barrios, con el código y el nombre oficiales que trae cada barrio; la capa de distritos del mismo organismo usa otros identificadores.
- Nombres en mayúsculas en origen (Zaragoza, València, Sevilla): se capitalizan, con artículos y preposiciones en minúscula salvo al inicio o tras guion, y la ele geminada valenciana (l·l). Se respetan las tildes que falten en origen.
- Zaragoza: el nivel de barrio son las juntas municipales y vecinales (29), con nombres capitalizados.

## Método

- Cortes de sombreado de edificios fijos para todas las ciudades (3, 8, 22 y 43 hab.) — con cuantiles por ciudad salían cortes repetidos en ciudades de vivienda unifamiliar (Rivas: todos 3) y la leyenda no era comparable.
- Simulador de ampliación con un máximo por sistema (`kmax` en `sistemas.json`): 1.000 en Madrid, 500 en las ciudades grandes, 400 en las medianas que no llegan al 80 % con 200, y 100–200 en las pequeñas.
- Indicador comparativo «nuevas para 80 %»: primera k de la curva del simulador con al menos el 80 % de la población a menos de 250 m.

## Incidencias de datos

- Catastro corta conexiones de forma intermitente: todas las descargas tienen reintentos y se comprueba que el ZIP sea válido.
- Los feeds ATOM provinciales del Catastro pueden venir en Latin-1 (A Coruña, Logroño, con «Ñ» en la ruta): se decodifican como tal antes de extraer la URL.

## Distancia desde el borde del edificio (2026-11-19)

- La distancia de cada edificio es la de su mejor punto de acceso: los dos extremos de la arista más cercana a su punto interior o cualquier nodo de la red a ≤ 30 m de su huella, sumando la distancia del nodo al borde (`pipeline/_acceso.py`, usado por 04, 07 y 08). Es el criterio del proyecto BicinRivas (ADR-0126) — con el punto interior, en las manzanas grandes el enganche caía en la calle de atrás y el resultado era claramente pesimista (Rivas 28,3 % frente al 51,4 % de BicinRivas). Es algo optimista: supone que el portal da a la calle más favorable.
- Se sigue sumando el tramo de la estación al nodo más cercano de la red (BicinRivas no lo suma): son metros que se andan. Con el nuevo criterio Rivas queda en 43,6 %; la diferencia restante con BicinRivas se debe a ese tramo (~3 puntos) y a la red OSM (otra descarga y fecha; BicinRivas mide hasta nodos y no hasta el punto exacto de la arista).
- Los repositorios de Madrid y Barcelona se actualizan con el mismo criterio.

## Web

- `.gitignore` anclado a la raíz (`/data/`) — el patrón `data/` excluía también `web/<sistema>/data/` y la primera publicación salió sin datos en las 23 páginas.
- Encuadre inicial del mapa = 99 % central de los edificios habitados, no el término municipal — Castellón (islas Columbretes), Palma (Cabrera) y los municipios con mucho diseminado rural arrancaban demasiado alejados.
- Si la vista guardada en la URL (`#zoom/lat/lon`) cae fuera de la ciudad, se descarta — una recarga durante el arranque del mapa podía dejar `#8/0/0` y el mapa en blanco en las recargas siguientes.
- Móvil (≤ 800 px): la página se desplaza con normalidad, con el mapa arriba (58 % de la altura visible) y el panel completo debajo, con las pestañas fijas — con alto fijo de pantalla el panel quedaba en un 45 % sin poder desplazarse y la barra del navegador tapaba el final. Al pulsar «Simular ampliación» se baja al simulador; al tocar una zona, estación o propuesta se sube al mapa.
- Botón destacado «Simula una ampliación del sistema» en la barra superior, en el rosa de las estaciones propuestas; con el simulador abierto pasa a «Volver al análisis».
