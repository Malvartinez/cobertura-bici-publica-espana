# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 87263.40 / 75949.20 / 20496.40 | 87263.40 / 75949.20 / 20496.40 | 0.0000 |
| 100 | 172725.86 / 7552.89 / 3430.25 | 172725.86 / 7552.89 / 3430.25 | 0.0000 |
| 400 | 182917.23 / 618.76 / 173.01 | 182917.23 / 618.76 / 173.01 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 87263.4 vs 87263, amarillo 75949.2 vs 75949, rojo 20496.4 vs 20496.
- Candidatos: 7912; pares candidato-edificio a <= 500 m: 569041.
