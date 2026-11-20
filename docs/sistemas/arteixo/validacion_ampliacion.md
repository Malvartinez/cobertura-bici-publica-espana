# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 5974.45 / 10519.71 / 17894.84 | 5974.45 / 10519.71 / 17894.84 | 0.0000 |
| 50 | 28227.56 / 3452.89 / 2708.55 | 28227.56 / 3452.89 / 2708.55 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 5974.5 vs 5974, amarillo 10519.7 vs 10520, rojo 17894.8 vs 17895.
- Candidatos: 2963; pares candidato-edificio a <= 500 m: 160912.
