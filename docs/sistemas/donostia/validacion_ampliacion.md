# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 93955.46 / 69909.71 / 25641.83 | 93955.46 / 69909.71 / 25641.83 | 0.0000 |
| 100 | 168494.86 / 17800.30 / 3211.83 | 168494.86 / 17800.30 / 3211.83 | 0.0000 |
| 200 | 184235.80 / 4026.44 / 1244.76 | 184235.80 / 4026.44 / 1244.76 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 93955.5 vs 93955, amarillo 69909.7 vs 69910, rojo 25641.8 vs 25642.
- Candidatos: 5205; pares candidato-edificio a <= 500 m: 339266.
