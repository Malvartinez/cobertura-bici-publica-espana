# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 162300.88 / 173891.58 / 107003.54 | 162300.88 / 173891.58 / 107003.54 | 0.0000 |
| 100 | 365462.54 / 60411.63 / 17321.83 | 365462.54 / 60411.63 / 17321.83 | 0.0000 |
| 400 | 437547.86 / 4476.97 / 1171.17 | 437547.86 / 4476.97 / 1171.17 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 162300.9 vs 162301, amarillo 173891.6 vs 173892, rojo 107003.5 vs 107004.
- Candidatos: 11113; pares candidato-edificio a <= 500 m: 1533632.
