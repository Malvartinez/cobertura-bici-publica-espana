# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 52315.98 / 62252.85 / 9522.17 | 52315.98 / 62252.85 / 9522.17 | 0.0000 |
| 100 | 121844.67 / 2094.35 / 151.98 | 121844.67 / 2094.35 / 151.98 | 0.0000 |
| 227 | 124069.05 / 21.95 / 0.00 | 124069.05 / 21.95 / 0.00 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 52316.0 vs 52316, amarillo 62252.9 vs 62253, rojo 9522.2 vs 9522.
- Candidatos: 3816; pares candidato-edificio a <= 500 m: 489395.
