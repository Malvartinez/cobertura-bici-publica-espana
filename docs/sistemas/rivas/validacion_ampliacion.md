# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 29207.82 / 59694.53 / 14340.65 | 29207.82 / 59694.53 / 14340.65 | 0.0000 |
| 100 | 97957.14 / 5260.83 / 25.03 | 97957.14 / 5260.83 / 25.03 | 0.0000 |
| 100 | 97957.14 / 5260.83 / 25.03 | 97957.14 / 5260.83 / 25.03 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 29207.8 vs 29208, amarillo 59694.5 vs 59695, rojo 14340.6 vs 14341.
- Candidatos: 3188; pares candidato-edificio a <= 500 m: 446119.
