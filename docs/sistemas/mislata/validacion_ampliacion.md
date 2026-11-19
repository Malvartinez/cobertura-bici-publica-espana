# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 36080.25 / 10922.75 / 0.00 | 36080.25 / 10922.75 / 0.00 | 0.0000 |
| 15 | 47003.00 / 0.00 / 0.00 | 47003.00 / 0.00 / 0.00 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 36080.3 vs 36080, amarillo 10922.7 vs 10923, rojo 0.0 vs 0.
- Candidatos: 515; pares candidato-edificio a <= 500 m: 44206.
