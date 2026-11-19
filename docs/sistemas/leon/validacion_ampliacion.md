# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 42241.00 / 70440.42 / 11409.58 | 42241.00 / 70440.42 / 11409.58 | 0.0000 |
| 100 | 119668.13 / 4124.70 / 298.16 | 119668.13 / 4124.70 / 298.16 | 0.0000 |
| 246 | 124067.30 / 23.70 / 0.00 | 124067.30 / 23.70 / 0.00 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 42241.0 vs 42241, amarillo 70440.4 vs 70440, rojo 11409.6 vs 11410.
- Candidatos: 3816; pares candidato-edificio a <= 500 m: 490051.
