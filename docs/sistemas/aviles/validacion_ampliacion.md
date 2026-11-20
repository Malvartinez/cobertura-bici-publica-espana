# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 16740.68 / 38377.21 / 20797.12 | 16740.68 / 38377.21 / 20797.12 | 0.0000 |
| 100 | 74129.47 / 1578.41 / 207.12 | 74129.47 / 1578.41 / 207.12 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 16740.7 vs 16741, amarillo 38377.2 vs 38377, rojo 20797.1 vs 20797.
- Candidatos: 1807; pares candidato-edificio a <= 500 m: 201918.
