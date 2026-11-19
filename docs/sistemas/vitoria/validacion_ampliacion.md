# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 20898.48 / 60782.59 / 178720.93 | 20898.48 / 60782.59 / 178720.93 | 0.0000 |
| 100 | 222249.82 / 31442.60 / 6709.58 | 222249.82 / 31442.60 / 6709.58 | 0.0000 |
| 200 | 253487.33 / 4665.17 / 2249.50 | 253487.33 / 4665.17 / 2249.50 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 20898.5 vs 20898, amarillo 60782.6 vs 60783, rojo 178720.9 vs 178721.
- Candidatos: 10324; pares candidato-edificio a <= 500 m: 1069522.
