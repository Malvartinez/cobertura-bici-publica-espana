# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 162538.74 / 79247.32 / 9490.94 | 162538.74 / 79247.32 / 9490.94 | 0.0000 |
| 100 | 248687.21 / 2150.92 / 438.87 | 248687.21 / 2150.92 / 438.87 | 0.0000 |
| 262 | 251260.76 / 14.85 / 1.39 | 251260.76 / 14.85 / 1.39 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 162538.7 vs 162539, amarillo 79247.3 vs 79247, rojo 9490.9 vs 9491.
- Candidatos: 5183; pares candidato-edificio a <= 500 m: 542926.
