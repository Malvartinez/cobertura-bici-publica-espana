# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 122012.40 / 196496.08 / 32466.52 | 122012.40 / 196496.08 / 32466.52 | 0.0000 |
| 100 | 317503.68 / 30858.90 / 2612.42 | 317503.68 / 30858.90 / 2612.42 | 0.0000 |
| 200 | 346887.84 / 3279.68 / 807.48 | 346887.84 / 3279.68 / 807.48 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 122012.4 vs 122012, amarillo 196496.1 vs 196496, rojo 32466.5 vs 32467.
- Candidatos: 4667; pares candidato-edificio a <= 500 m: 537489.
