# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 514004.31 / 287546.07 / 40007.62 | 514004.31 / 287546.07 / 40007.62 | 0.0000 |
| 100 | 707700.15 / 124005.44 / 9852.41 | 707700.15 / 124005.44 / 9852.41 | 0.0000 |
| 500 | 839292.84 / 1703.28 / 561.88 | 839292.84 / 1703.28 / 561.88 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 514004.3 vs 514004, amarillo 287546.1 vs 287546, rojo 40007.6 vs 40008.
- Candidatos: 13836; pares candidato-edificio a <= 500 m: 1033228.
