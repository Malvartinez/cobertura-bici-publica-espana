# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 60914.46 / 31294.37 / 16143.18 | 60914.46 / 31294.37 / 16143.18 | 0.0000 |
| 100 | 106851.63 / 1235.61 / 264.76 | 106851.63 / 1235.61 / 264.76 | 0.0000 |
| 200 | 108166.51 / 153.21 / 32.28 | 108166.51 / 153.21 / 32.28 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 60914.5 vs 60914, amarillo 31294.4 vs 31294, rojo 16143.2 vs 16143.
- Candidatos: 3915; pares candidato-edificio a <= 500 m: 406751.
