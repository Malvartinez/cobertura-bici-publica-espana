# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 1177814.39 / 1803368.77 / 496313.84 | 1177814.39 / 1803368.77 / 496313.84 | 0.0000 |
| 100 | 1567734.83 / 1673900.62 / 235861.55 | 1567734.83 / 1673900.62 / 235861.55 | 0.0000 |
| 1000 | 3136207.88 / 329599.97 / 11689.15 | 3136207.88 / 329599.97 / 11689.15 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 1177814.4 vs 1177814, amarillo 1803368.8 vs 1803369, rojo 496313.8 vs 496314.
- Candidatos: 58623; pares candidato-edificio a <= 500 m: 6467076.
