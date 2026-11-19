# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 159792.58 / 43942.73 / 41839.69 | 159792.58 / 43942.73 / 41839.69 | 0.0000 |
| 100 | 217504.25 / 7098.94 / 20971.81 | 217504.25 / 7098.94 / 20971.81 | 0.0000 |
| 400 | 227910.40 / 9914.80 / 7749.80 | 227910.40 / 9914.80 / 7749.80 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 159792.6 vs 159793, amarillo 43942.7 vs 43943, rojo 41839.7 vs 41840.
- Candidatos: 12963; pares candidato-edificio a <= 500 m: 448523.
