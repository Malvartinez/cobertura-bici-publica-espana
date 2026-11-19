# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 19056.40 / 37313.52 / 19545.08 | 19056.40 / 37313.52 / 19545.08 | 0.0000 |
| 100 | 74167.70 / 1545.29 / 202.01 | 74167.70 / 1545.29 / 202.01 | 0.0000 |
| 100 | 74167.70 / 1545.29 / 202.01 | 74167.70 / 1545.29 / 202.01 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 19056.4 vs 19056, amarillo 37313.5 vs 37314, rojo 19545.1 vs 19545.
- Candidatos: 1807; pares candidato-edificio a <= 500 m: 201748.
