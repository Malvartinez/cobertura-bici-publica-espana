# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 40085.73 / 52441.05 / 10716.22 | 40085.73 / 52441.05 / 10716.22 | 0.0000 |
| 100 | 100597.88 / 2583.05 / 62.07 | 100597.88 / 2583.05 / 62.07 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 40085.7 vs 40086, amarillo 52441.1 vs 52441, rojo 10716.2 vs 10716.
- Candidatos: 3188; pares candidato-edificio a <= 500 m: 454124.
