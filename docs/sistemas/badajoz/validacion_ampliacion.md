# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 32096.15 / 53269.99 / 65503.85 | 32096.15 / 53269.99 / 65503.85 | 0.0000 |
| 100 | 134182.19 / 9381.31 / 7306.50 | 134182.19 / 9381.31 / 7306.50 | 0.0000 |
| 400 | 147639.85 / 2043.36 / 1186.80 | 147639.85 / 2043.36 / 1186.80 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 32096.2 vs 32096, amarillo 53270.0 vs 53270, rojo 65503.9 vs 65504.
- Candidatos: 8930; pares candidato-edificio a <= 500 m: 937243.
