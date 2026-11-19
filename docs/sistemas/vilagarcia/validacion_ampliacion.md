# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 14928.89 / 10428.37 / 12617.74 | 14928.89 / 10428.37 / 12617.74 | 0.0000 |
| 50 | 30972.61 / 5575.93 / 1426.46 | 30972.61 / 5575.93 / 1426.46 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 14928.9 vs 14929, amarillo 10428.4 vs 10428, rojo 12617.7 vs 12618.
- Candidatos: 3463; pares candidato-edificio a <= 500 m: 322952.
