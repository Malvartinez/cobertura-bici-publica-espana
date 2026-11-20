# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 161255.37 / 116718.11 / 23824.52 | 161255.37 / 116718.11 / 23824.52 | 0.0000 |
| 100 | 278014.13 / 20715.22 / 3068.65 | 278014.13 / 20715.22 / 3068.65 | 0.0000 |
| 400 | 301612.02 / 147.67 / 38.31 | 301612.02 / 147.67 / 38.31 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 161255.4 vs 161255, amarillo 116718.1 vs 116718, rojo 23824.5 vs 23825.
- Candidatos: 7988; pares candidato-edificio a <= 500 m: 547300.
