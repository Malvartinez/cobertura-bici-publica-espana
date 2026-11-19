# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 58151.46 / 81930.94 / 11598.61 | 58151.46 / 81930.94 / 11598.61 | 0.0000 |
| 100 | 150393.36 / 720.94 / 566.71 | 150393.36 / 720.94 / 566.71 | 0.0000 |
| 200 | 151428.88 / 148.25 / 103.87 | 151428.88 / 148.25 / 103.87 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 58151.5 vs 58151, amarillo 81930.9 vs 81931, rojo 11598.6 vs 11599.
- Candidatos: 4077; pares candidato-edificio a <= 500 m: 269706.
