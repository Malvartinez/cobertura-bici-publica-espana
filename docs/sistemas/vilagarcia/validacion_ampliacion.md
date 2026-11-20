# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 13427.79 / 11800.67 / 12746.54 | 13427.79 / 11800.67 / 12746.54 | 0.0000 |
| 50 | 30531.55 / 5918.25 / 1525.20 | 30531.55 / 5918.25 / 1525.20 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 13427.8 vs 13428, amarillo 11800.7 vs 11801, rojo 12746.5 vs 12747.
- Candidatos: 3463; pares candidato-edificio a <= 500 m: 327815.
