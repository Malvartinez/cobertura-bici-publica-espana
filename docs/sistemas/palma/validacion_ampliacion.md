# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 131045.25 / 194817.03 / 117333.72 | 131045.25 / 194817.03 / 117333.72 | 0.0000 |
| 100 | 335221.62 / 85742.20 / 22232.19 | 335221.62 / 85742.20 / 22232.19 | 0.0000 |
| 200 | 398487.72 / 36619.94 / 8088.33 | 398487.72 / 36619.94 / 8088.33 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 131045.2 vs 131045, amarillo 194817.0 vs 194817, rojo 117333.7 vs 117334.
- Candidatos: 11113; pares candidato-edificio a <= 500 m: 1531717.
