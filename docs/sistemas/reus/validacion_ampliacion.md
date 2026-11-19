# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 36161.01 / 54218.18 / 21531.81 | 36161.01 / 54218.18 / 21531.81 | 0.0000 |
| 100 | 109077.42 / 1324.68 / 1508.90 | 109077.42 / 1324.68 / 1508.90 | 0.0000 |
| 200 | 110570.29 / 977.37 / 363.34 | 110570.29 / 977.37 / 363.34 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 36161.0 vs 36161, amarillo 54218.2 vs 54218, rojo 21531.8 vs 21532.
- Candidatos: 3284; pares candidato-edificio a <= 500 m: 387447.
