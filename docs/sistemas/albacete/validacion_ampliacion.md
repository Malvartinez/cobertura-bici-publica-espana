# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 49993.61 / 96849.34 / 28225.05 | 49993.61 / 96849.34 / 28225.05 | 0.0000 |
| 100 | 163388.92 / 6730.41 / 4948.67 | 163388.92 / 6730.41 / 4948.67 | 0.0000 |
| 200 | 170978.00 / 2118.69 / 1971.30 | 170978.00 / 2118.69 / 1971.30 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 49993.6 vs 49994, amarillo 96849.3 vs 96849, rojo 28225.0 vs 28225.
- Candidatos: 9159; pares candidato-edificio a <= 500 m: 615747.
