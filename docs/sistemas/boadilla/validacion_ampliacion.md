# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 27435.57 / 23485.94 / 15397.49 | 27435.57 / 23485.94 / 15397.49 | 0.0000 |
| 100 | 59790.00 / 5860.00 / 669.00 | 59790.00 / 5860.00 / 669.00 | 0.0000 |
| 100 | 59790.00 / 5860.00 / 669.00 | 59790.00 / 5860.00 / 669.00 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 27435.6 vs 27436, amarillo 23485.9 vs 23486, rojo 15397.5 vs 15397.
- Candidatos: 3440; pares candidato-edificio a <= 500 m: 199629.
