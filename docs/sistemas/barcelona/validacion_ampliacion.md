# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 1269832.16 / 393504.46 / 49910.38 | 1269832.16 / 393504.46 / 49910.38 | 0.0000 |
| 100 | 1561262.79 / 140042.43 / 11941.77 | 1561262.79 / 140042.43 / 11941.77 | 0.0000 |
| 500 | 1711682.92 / 1441.27 / 122.81 | 1711682.92 / 1441.27 / 122.81 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 1269832.2 vs 1269832, amarillo 393504.5 vs 393504, rojo 49910.4 vs 49910.
- Candidatos: 18453; pares candidato-edificio a <= 500 m: 2134714.
