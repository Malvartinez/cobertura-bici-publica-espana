# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 150.64 / 676.50 / 3254.85 | 150.64 / 676.50 / 3254.85 | 0.0000 |
| 30 | 3703.88 / 252.75 / 125.37 | 3703.88 / 252.75 / 125.37 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 150.6 vs 151, amarillo 676.5 vs 677, rojo 3254.9 vs 3255.
- Candidatos: 2827; pares candidato-edificio a <= 500 m: 89866.
