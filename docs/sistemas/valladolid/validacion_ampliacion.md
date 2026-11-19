# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 168313.65 / 110290.23 / 23194.12 | 168313.65 / 110290.23 / 23194.12 | 0.0000 |
| 100 | 280351.19 / 18678.04 / 2768.76 | 280351.19 / 18678.04 / 2768.76 | 0.0000 |
| 400 | 301549.37 / 207.96 / 40.66 | 301549.37 / 207.96 / 40.66 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 168313.7 vs 168314, amarillo 110290.2 vs 110290, rojo 23194.1 vs 23194.
- Candidatos: 7988; pares candidato-edificio a <= 500 m: 538160.
