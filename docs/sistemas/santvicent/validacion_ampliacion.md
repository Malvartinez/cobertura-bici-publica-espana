# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 20241.48 / 20968.01 / 19218.51 | 20241.48 / 20968.01 / 19218.51 | 0.0000 |
| 50 | 52731.34 / 4500.94 / 3195.73 | 52731.34 / 4500.94 / 3195.73 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 20241.5 vs 20241, amarillo 20968.0 vs 20968, rojo 19218.5 vs 19219.
- Candidatos: 2494; pares candidato-edificio a <= 500 m: 276780.
