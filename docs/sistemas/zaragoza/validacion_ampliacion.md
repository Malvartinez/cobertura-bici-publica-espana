# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 529367.07 / 134433.79 / 35206.14 | 529367.07 / 134433.79 / 35206.14 | 0.0000 |
| 100 | 655204.36 / 34006.62 / 9796.02 | 655204.36 / 34006.62 / 9796.02 | 0.0000 |
| 500 | 696269.69 / 2136.92 / 600.39 | 696269.69 / 2136.92 / 600.39 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 529367.1 vs 529367, amarillo 134433.8 vs 134434, rojo 35206.1 vs 35206.
- Candidatos: 19027; pares candidato-edificio a <= 500 m: 703343.
