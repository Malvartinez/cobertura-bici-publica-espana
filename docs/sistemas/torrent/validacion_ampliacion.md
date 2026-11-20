# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 45213.09 / 29481.80 / 16658.11 | 45213.09 / 29481.80 / 16658.11 | 0.0000 |
| 100 | 86529.42 / 3761.89 / 1061.69 | 86529.42 / 3761.89 / 1061.69 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 45213.1 vs 45213, amarillo 29481.8 vs 29482, rojo 16658.1 vs 16658.
- Candidatos: 4635; pares candidato-edificio a <= 500 m: 365102.
