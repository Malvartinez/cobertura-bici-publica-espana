# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 621506.81 / 182379.82 / 37671.36 | 621506.81 / 182379.82 / 37671.36 | 0.0000 |
| 100 | 781276.61 / 53521.95 / 6759.44 | 781276.61 / 53521.95 / 6759.44 | 0.0000 |
| 500 | 840892.48 / 541.03 / 124.49 | 840892.48 / 541.03 / 124.49 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 621506.8 vs 621507, amarillo 182379.8 vs 182380, rojo 37671.4 vs 37671.
- Candidatos: 13836; pares candidato-edificio a <= 500 m: 892572.
