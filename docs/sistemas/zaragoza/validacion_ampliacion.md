# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 496429.71 / 166945.46 / 35631.83 | 496429.71 / 166945.46 / 35631.83 | 0.0000 |
| 100 | 640024.82 / 48167.17 / 10815.01 | 640024.82 / 48167.17 / 10815.01 | 0.0000 |
| 500 | 695814.34 / 2464.18 / 728.48 | 695814.34 / 2464.18 / 728.48 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 496429.7 vs 496430, amarillo 166945.5 vs 166945, rojo 35631.8 vs 35632.
- Candidatos: 19027; pares candidato-edificio a <= 500 m: 747527.
