# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 6426.07 / 10386.06 / 17576.87 | 6426.07 / 10386.06 / 17576.87 | 0.0000 |
| 50 | 28271.19 / 3483.18 / 2634.62 | 28271.19 / 3483.18 / 2634.62 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 6426.1 vs 6426, amarillo 10386.1 vs 10386, rojo 17576.9 vs 17577.
- Candidatos: 2963; pares candidato-edificio a <= 500 m: 162742.
