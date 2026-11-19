# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 470.98 / 1002.24 / 3339.78 | 470.98 / 1002.24 / 3339.78 | 0.0000 |
| 30 | 4693.80 / 113.37 / 5.83 | 4693.80 / 113.37 / 5.83 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 471.0 vs 471, amarillo 1002.2 vs 1002, rojo 3339.8 vs 3340.
- Candidatos: 629; pares candidato-edificio a <= 500 m: 88286.
