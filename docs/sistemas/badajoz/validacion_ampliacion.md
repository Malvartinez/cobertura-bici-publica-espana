# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 27727.38 / 54258.86 / 68883.75 | 27727.38 / 54258.86 / 68883.75 | 0.0000 |
| 100 | 130450.67 / 12802.07 / 7617.26 | 130450.67 / 12802.07 / 7617.26 | 0.0000 |
| 400 | 147938.32 / 1734.04 / 1197.64 | 147938.32 / 1734.04 / 1197.64 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 27727.4 vs 27727, amarillo 54258.9 vs 54259, rojo 68883.8 vs 68884.
- Candidatos: 8930; pares candidato-edificio a <= 500 m: 923680.
