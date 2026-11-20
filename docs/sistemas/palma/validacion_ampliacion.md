# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 159706.79 / 176076.54 / 107412.67 | 159706.79 / 176076.54 / 107412.67 | 0.0000 |
| 100 | 361668.18 / 64655.51 / 16872.31 | 361668.18 / 64655.51 / 16872.31 | 0.0000 |
| 400 | 437883.74 / 4298.92 / 1013.34 | 437883.74 / 4298.92 / 1013.34 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 159706.8 vs 159707, amarillo 176076.5 vs 176077, rojo 107412.7 vs 107413.
- Candidatos: 11113; pares candidato-edificio a <= 500 m: 1540337.
