# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 57465.98 / 57819.95 / 8805.07 | 57465.98 / 57819.95 / 8805.07 | 0.0000 |
| 100 | 122426.21 / 1511.73 / 153.07 | 122426.21 / 1511.73 / 153.07 | 0.0000 |
| 213 | 124068.92 / 22.08 / 0.00 | 124068.92 / 22.08 / 0.00 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 57466.0 vs 57466, amarillo 57820.0 vs 57820, rojo 8805.1 vs 8805.
- Candidatos: 3816; pares candidato-edificio a <= 500 m: 484773.
