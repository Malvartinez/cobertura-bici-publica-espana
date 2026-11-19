# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 391.57 / 832.54 / 8782.89 | 391.57 / 832.54 / 8782.89 | 0.0000 |
| 30 | 7008.25 / 1081.66 / 1917.10 | 7008.25 / 1081.66 / 1917.10 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 391.6 vs 392, amarillo 832.5 vs 833, rojo 8782.9 vs 8783.
- Candidatos: 1461; pares candidato-edificio a <= 500 m: 84590.
