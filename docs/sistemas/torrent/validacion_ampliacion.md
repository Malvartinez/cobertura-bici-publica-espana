# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 47098.49 / 27719.58 / 16534.93 | 47098.49 / 27719.58 / 16534.93 | 0.0000 |
| 100 | 86341.98 / 3818.62 / 1192.40 | 86341.98 / 3818.62 / 1192.40 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 47098.5 vs 47098, amarillo 27719.6 vs 27720, rojo 16534.9 vs 16535.
- Candidatos: 4635; pares candidato-edificio a <= 500 m: 359441.
