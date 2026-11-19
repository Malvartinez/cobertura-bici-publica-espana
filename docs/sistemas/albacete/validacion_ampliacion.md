# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 65791.87 / 87078.24 / 22197.88 | 65791.87 / 87078.24 / 22197.88 | 0.0000 |
| 100 | 168014.14 / 3100.55 / 3953.31 | 168014.14 / 3100.55 / 3953.31 | 0.0000 |
| 400 | 173726.82 / 1022.40 / 318.78 | 173726.82 / 1022.40 / 318.78 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 65791.9 vs 65792, amarillo 87078.2 vs 87078, rojo 22197.9 vs 22198.
- Candidatos: 9159; pares candidato-edificio a <= 500 m: 614750.
