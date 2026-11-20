# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 103283.70 / 61745.51 / 18679.79 | 103283.70 / 61745.51 / 18679.79 | 0.0000 |
| 100 | 175927.95 / 5273.26 / 2507.79 | 175927.95 / 5273.26 / 2507.79 | 0.0000 |
| 400 | 183177.40 / 416.96 / 114.64 | 183177.40 / 416.96 / 114.64 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 103283.7 vs 103284, amarillo 61745.5 vs 61746, rojo 18679.8 vs 18680.
- Candidatos: 7912; pares candidato-edificio a <= 500 m: 555891.
