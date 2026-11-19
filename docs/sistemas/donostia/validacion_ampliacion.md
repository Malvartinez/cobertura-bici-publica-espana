# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 107279.97 / 58623.19 / 23603.83 | 107279.97 / 58623.19 / 23603.83 | 0.0000 |
| 100 | 175140.82 / 11911.51 / 2454.68 | 175140.82 / 11911.51 / 2454.68 | 0.0000 |
| 200 | 186081.97 / 2567.34 / 857.69 | 186081.97 / 2567.34 / 857.69 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 107280.0 vs 107280, amarillo 58623.2 vs 58623, rojo 23603.8 vs 23604.
- Candidatos: 5205; pares candidato-edificio a <= 500 m: 331089.
