# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 174701.37 / 30008.99 / 40864.64 | 174701.37 / 30008.99 / 40864.64 | 0.0000 |
| 100 | 219655.66 / 6653.51 / 19265.83 | 219655.66 / 6653.51 / 19265.83 | 0.0000 |
| 400 | 229199.21 / 9447.09 / 6928.70 | 229199.21 / 9447.09 / 6928.70 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 174701.4 vs 174701, amarillo 30009.0 vs 30009, rojo 40864.6 vs 40865.
- Candidatos: 12963; pares candidato-edificio a <= 500 m: 429242.
