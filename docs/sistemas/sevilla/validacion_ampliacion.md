# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 319064.70 / 268398.95 / 101250.35 | 319064.70 / 268398.95 / 101250.35 | 0.0000 |
| 100 | 529229.03 / 152846.31 / 6638.66 | 529229.03 / 152846.31 / 6638.66 | 0.0000 |
| 500 | 687246.86 / 1174.10 / 293.04 | 687246.86 / 1174.10 / 293.04 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 319064.7 vs 319065, amarillo 268399.0 vs 268399, rojo 101250.3 vs 101250.
- Candidatos: 12965; pares candidato-edificio a <= 500 m: 2571684.
