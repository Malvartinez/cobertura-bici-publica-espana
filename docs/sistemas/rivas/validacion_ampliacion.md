# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 45039.56 / 47808.40 / 10395.04 | 45039.56 / 47808.40 / 10395.04 | 0.0000 |
| 100 | 100877.67 / 2340.30 / 25.03 | 100877.67 / 2340.30 / 25.03 | 0.0000 |
| 100 | 100877.67 / 2340.30 / 25.03 | 100877.67 / 2340.30 / 25.03 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 45039.6 vs 45040, amarillo 47808.4 vs 47808, rojo 10395.0 vs 10395.
- Candidatos: 3188; pares candidato-edificio a <= 500 m: 450812.
