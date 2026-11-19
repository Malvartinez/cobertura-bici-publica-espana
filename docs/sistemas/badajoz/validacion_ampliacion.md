# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 24836.14 / 52790.99 / 73242.87 | 24836.14 / 52790.99 / 73242.87 | 0.0000 |
| 100 | 126148.73 / 15837.14 / 8884.13 | 126148.73 / 15837.14 / 8884.13 | 0.0000 |
| 400 | 147190.16 / 2333.61 / 1346.23 | 147190.16 / 2333.61 / 1346.23 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 24836.1 vs 24836, amarillo 52791.0 vs 52791, rojo 73242.9 vs 73243.
- Candidatos: 8930; pares candidato-edificio a <= 500 m: 900450.
