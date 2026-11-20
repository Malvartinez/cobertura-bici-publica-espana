# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 61746.13 / 89712.12 / 23609.75 | 61746.13 / 89712.12 / 23609.75 | 0.0000 |
| 100 | 167658.50 / 2999.78 / 4409.73 | 167658.50 / 2999.78 / 4409.73 | 0.0000 |
| 400 | 173757.95 / 1011.77 / 298.29 | 173757.95 / 1011.77 / 298.29 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 61746.1 vs 61746, amarillo 89712.1 vs 89712, rojo 23609.7 vs 23610.
- Candidatos: 9159; pares candidato-edificio a <= 500 m: 614416.
