# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 587430.72 / 215343.07 / 38784.22 | 587430.72 / 215343.07 / 38784.22 | 0.0000 |
| 100 | 759881.05 / 74338.63 / 7338.32 | 759881.05 / 74338.63 / 7338.32 | 0.0000 |
| 500 | 840487.16 / 874.20 / 196.65 | 840487.16 / 874.20 / 196.65 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 587430.7 vs 587431, amarillo 215343.1 vs 215343, rojo 38784.2 vs 38784.
- Candidatos: 13836; pares candidato-edificio a <= 500 m: 944695.
