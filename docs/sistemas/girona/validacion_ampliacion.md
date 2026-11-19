# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 50136.68 / 40150.15 / 18065.17 | 50136.68 / 40150.15 / 18065.17 | 0.0000 |
| 100 | 105448.24 / 2399.45 / 504.31 | 105448.24 / 2399.45 / 504.31 | 0.0000 |
| 200 | 107977.37 / 303.46 / 71.17 | 107977.37 / 303.46 / 71.17 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 50136.7 vs 50137, amarillo 40150.2 vs 40150, rojo 18065.2 vs 18065.
- Candidatos: 3915; pares candidato-edificio a <= 500 m: 417227.
