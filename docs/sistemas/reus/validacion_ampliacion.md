# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 45515.35 / 47003.97 / 19391.68 | 45515.35 / 47003.97 / 19391.68 | 0.0000 |
| 100 | 109534.99 / 1171.38 / 1204.63 | 109534.99 / 1171.38 / 1204.63 | 0.0000 |
| 200 | 110763.35 / 879.72 / 267.93 | 110763.35 / 879.72 / 267.93 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 45515.3 vs 45515, amarillo 47004.0 vs 47004, rojo 19391.7 vs 19392.
- Candidatos: 3284; pares candidato-edificio a <= 500 m: 382677.
