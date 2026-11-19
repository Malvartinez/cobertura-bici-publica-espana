# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 349373.53 / 247557.03 / 91783.44 | 349373.53 / 247557.03 / 91783.44 | 0.0000 |
| 100 | 561225.41 / 122171.56 / 5317.03 | 561225.41 / 122171.56 / 5317.03 | 0.0000 |
| 500 | 687386.87 / 1095.45 / 231.68 | 687386.87 / 1095.45 / 231.68 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 349373.5 vs 349374, amarillo 247557.0 vs 247557, rojo 91783.4 vs 91783.
- Candidatos: 12965; pares candidato-edificio a <= 500 m: 2545800.
