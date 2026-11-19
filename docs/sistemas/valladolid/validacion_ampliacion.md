# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 129430.20 / 139871.86 / 32495.94 | 129430.20 / 139871.86 / 32495.94 | 0.0000 |
| 100 | 257452.99 / 39409.93 / 4935.08 | 257452.99 / 39409.93 / 4935.08 | 0.0000 |
| 200 | 291410.29 / 8862.48 / 1525.22 | 291410.29 / 8862.48 / 1525.22 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 129430.2 vs 129430, amarillo 139871.9 vs 139872, rojo 32495.9 vs 32496.
- Candidatos: 7988; pares candidato-edificio a <= 500 m: 553882.
