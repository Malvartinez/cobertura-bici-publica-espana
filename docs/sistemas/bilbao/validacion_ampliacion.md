# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 147859.19 / 179139.83 / 23975.97 | 147859.19 / 179139.83 / 23975.97 | 0.0000 |
| 100 | 331934.58 / 17575.31 / 1465.10 | 331934.58 / 17575.31 / 1465.10 | 0.0000 |
| 200 | 349701.82 / 920.83 / 352.35 | 349701.82 / 920.83 / 352.35 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 147859.2 vs 147859, amarillo 179139.8 vs 179140, rojo 23976.0 vs 23976.
- Candidatos: 4667; pares candidato-edificio a <= 500 m: 524382.
