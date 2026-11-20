# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 55048.85 / 83716.41 / 12915.74 | 55048.85 / 83716.41 / 12915.74 | 0.0000 |
| 100 | 150104.71 / 978.72 / 597.57 | 150104.71 / 978.72 / 597.57 | 0.0000 |
| 200 | 151388.35 / 186.41 / 106.25 | 151388.35 / 186.41 / 106.25 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 55048.8 vs 55049, amarillo 83716.4 vs 83716, rojo 12915.7 vs 12916.
- Candidatos: 4077; pares candidato-edificio a <= 500 m: 268251.
