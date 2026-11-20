# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 390.27 / 805.17 / 8811.56 | 390.27 / 805.17 / 8811.56 | 0.0000 |
| 30 | 6986.00 / 1070.13 / 1950.87 | 6986.00 / 1070.13 / 1950.87 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 390.3 vs 390, amarillo 805.2 vs 805, rojo 8811.6 vs 8812.
- Candidatos: 1461; pares candidato-edificio a <= 500 m: 84500.
