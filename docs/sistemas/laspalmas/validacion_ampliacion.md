# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 60449.57 / 104474.69 / 219098.74 | 60449.57 / 104474.69 / 219098.74 | 0.0000 |
| 100 | 248906.78 / 97480.87 / 37635.35 | 248906.78 / 97480.87 / 37635.35 | 0.0000 |
| 400 | 368510.74 / 12873.96 / 2638.30 | 368510.74 / 12873.96 / 2638.30 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 60449.6 vs 60450, amarillo 104474.7 vs 104475, rojo 219098.7 vs 219099.
- Candidatos: 8519; pares candidato-edificio a <= 500 m: 1732342.
