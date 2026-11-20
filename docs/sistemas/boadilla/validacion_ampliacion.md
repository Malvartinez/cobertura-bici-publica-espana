# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 21909.72 / 25759.03 / 18650.25 | 21909.72 / 25759.03 / 18650.25 | 0.0000 |
| 100 | 59445.00 / 6413.74 / 460.26 | 59445.00 / 6413.74 / 460.26 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 21909.7 vs 21910, amarillo 25759.0 vs 25759, rojo 18650.2 vs 18650.
- Candidatos: 3440; pares candidato-edificio a <= 500 m: 205466.
