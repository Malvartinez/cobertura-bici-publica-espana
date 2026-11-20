# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 50007.20 / 82147.58 / 42927.22 | 50007.20 / 82147.58 / 42927.22 | 0.0000 |
| 100 | 161991.28 / 12011.69 / 1079.03 | 161991.28 / 12011.69 / 1079.03 | 0.0000 |
| 200 | 173937.94 / 1076.81 / 67.25 | 173937.94 / 1076.81 / 67.25 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 50007.2 vs 50007, amarillo 82147.6 vs 82148, rojo 42927.2 vs 42927.
- Candidatos: 5644; pares candidato-edificio a <= 500 m: 572853.
