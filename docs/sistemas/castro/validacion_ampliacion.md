# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 10147.76 / 13592.48 / 9651.76 | 10147.76 / 13592.48 / 9651.76 | 0.0000 |
| 50 | 31710.86 / 1371.44 / 309.70 | 31710.86 / 1371.44 / 309.70 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 10147.8 vs 10148, amarillo 13592.5 vs 13592, rojo 9651.8 vs 9652.
- Candidatos: 2562; pares candidato-edificio a <= 500 m: 77287.
