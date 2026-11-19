# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 15825.83 / 59137.14 / 185439.03 | 15825.83 / 59137.14 / 185439.03 | 0.0000 |
| 100 | 207993.70 / 44634.41 / 7773.88 | 207993.70 / 44634.41 / 7773.88 | 0.0000 |
| 200 | 250661.36 / 6848.81 / 2891.83 | 250661.36 / 6848.81 / 2891.83 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 15825.8 vs 15826, amarillo 59137.1 vs 59137, rojo 185439.0 vs 185439.
- Candidatos: 10324; pares candidato-edificio a <= 500 m: 1010788.
