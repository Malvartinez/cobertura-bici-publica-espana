# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 49354.61 / 43673.26 / 18883.13 | 49354.61 / 43673.26 / 18883.13 | 0.0000 |
| 100 | 109523.38 / 1198.90 / 1188.72 | 109523.38 / 1198.90 / 1188.72 | 0.0000 |
| 200 | 110695.89 / 898.89 / 316.23 | 110695.89 / 898.89 / 316.23 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 49354.6 vs 49355, amarillo 43673.3 vs 43673, rojo 18883.1 vs 18883.
- Candidatos: 3284; pares candidato-edificio a <= 500 m: 372375.
