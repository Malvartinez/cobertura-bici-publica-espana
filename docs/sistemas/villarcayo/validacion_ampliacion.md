# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 165.56 / 595.18 / 3321.27 | 165.56 / 595.18 / 3321.27 | 0.0000 |
| 30 | 3731.87 / 229.28 / 120.85 | 3731.87 / 229.28 / 120.85 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 165.6 vs 166, amarillo 595.2 vs 595, rojo 3321.3 vs 3321.
- Candidatos: 2827; pares candidato-edificio a <= 500 m: 88333.
