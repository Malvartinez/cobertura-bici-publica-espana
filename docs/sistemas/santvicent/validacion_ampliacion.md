# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 18670.16 / 22142.80 / 19615.04 | 18670.16 / 22142.80 / 19615.04 | 0.0000 |
| 50 | 52924.89 / 4209.72 / 3293.38 | 52924.89 / 4209.72 / 3293.38 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 18670.2 vs 18670, amarillo 22142.8 vs 22143, rojo 19615.0 vs 19615.
- Candidatos: 2494; pares candidato-edificio a <= 500 m: 282501.
