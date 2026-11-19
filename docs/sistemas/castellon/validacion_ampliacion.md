# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 109321.46 / 55484.24 / 18903.30 | 109321.46 / 55484.24 / 18903.30 | 0.0000 |
| 100 | 176259.23 / 4890.06 / 2559.71 | 176259.23 / 4890.06 / 2559.71 | 0.0000 |
| 400 | 183126.95 / 460.54 / 121.51 | 183126.95 / 460.54 / 121.51 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 109321.5 vs 109321, amarillo 55484.2 vs 55484, rojo 18903.3 vs 18903.
- Candidatos: 7912; pares candidato-edificio a <= 500 m: 551410.
