# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 422789.02 / 237647.71 / 38570.28 | 422789.02 / 237647.71 / 38570.28 | 0.0000 |
| 100 | 598219.47 / 84746.39 / 16041.14 | 598219.47 / 84746.39 / 16041.14 | 0.0000 |
| 500 | 694451.09 / 3173.76 / 1382.16 | 694451.09 / 3173.76 / 1382.16 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 422789.0 vs 422789, amarillo 237647.7 vs 237648, rojo 38570.3 vs 38570.
- Candidatos: 19027; pares candidato-edificio a <= 500 m: 802356.
