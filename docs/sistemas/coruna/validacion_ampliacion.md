# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 151598.63 / 89979.69 / 9698.67 | 151598.63 / 89979.69 / 9698.67 | 0.0000 |
| 100 | 247696.04 / 2974.20 / 606.76 | 247696.04 / 2974.20 / 606.76 | 0.0000 |
| 272 | 251265.74 / 11.26 / 0.00 | 251265.74 / 11.26 / 0.00 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 151598.6 vs 151599, amarillo 89979.7 vs 89980, rojo 9698.7 vs 9699.
- Candidatos: 5183; pares candidato-edificio a <= 500 m: 575206.
