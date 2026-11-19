# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 1113183.21 / 544173.95 / 55889.84 | 1113183.21 / 544173.95 / 55889.84 | 0.0000 |
| 100 | 1447151.50 / 251143.45 / 14952.05 | 1447151.50 / 251143.45 / 14952.05 | 0.0000 |
| 500 | 1703644.91 / 9056.93 / 545.16 | 1703644.91 / 9056.93 / 545.16 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 1113183.2 vs 1113183, amarillo 544174.0 vs 544174, rojo 55889.8 vs 55890.
- Candidatos: 18453; pares candidato-edificio a <= 500 m: 2381375.
