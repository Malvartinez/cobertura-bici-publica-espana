# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 88666.68 / 136740.20 / 45852.11 | 88666.68 / 136740.20 / 45852.11 | 0.0000 |
| 100 | 241685.79 / 14574.23 / 14998.98 | 241685.79 / 14574.23 / 14998.98 | 0.0000 |
| 400 | 263721.72 / 5990.55 / 1546.73 | 263721.72 / 5990.55 / 1546.73 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 88666.7 vs 88667, amarillo 136740.2 vs 136740, rojo 45852.1 vs 45852.
- Candidatos: 8772; pares candidato-edificio a <= 500 m: 797832.
