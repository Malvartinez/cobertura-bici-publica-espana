# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 178715.43 / 26264.44 / 40595.12 | 178715.43 / 26264.44 / 40595.12 | 0.0000 |
| 100 | 220035.72 / 6229.59 / 19309.70 | 220035.72 / 6229.59 / 19309.70 | 0.0000 |
| 400 | 229059.68 / 9698.81 / 6816.51 | 229059.68 / 9698.81 / 6816.51 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 178715.4 vs 178715, amarillo 26264.4 vs 26264, rojo 40595.1 vs 40595.
- Candidatos: 12963; pares candidato-edificio a <= 500 m: 419382.
