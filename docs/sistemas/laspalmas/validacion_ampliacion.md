# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 86765.55 / 95145.02 / 202112.43 | 86765.55 / 95145.02 / 202112.43 | 0.0000 |
| 100 | 284018.23 / 72373.92 / 27630.84 | 284018.23 / 72373.92 / 27630.84 | 0.0000 |
| 400 | 374664.33 / 7872.57 / 1486.09 | 374664.33 / 7872.57 / 1486.09 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 86765.5 vs 86766, amarillo 95145.0 vs 95145, rojo 202112.4 vs 202112.
- Candidatos: 8519; pares candidato-edificio a <= 500 m: 1783188.
