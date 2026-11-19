# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 282846.46 / 295552.42 / 110315.11 | 282846.46 / 295552.42 / 110315.11 | 0.0000 |
| 100 | 487760.67 / 192760.88 / 8192.45 | 487760.67 / 192760.88 / 8192.45 | 0.0000 |
| 500 | 684546.95 / 3546.91 / 620.13 | 684546.95 / 3546.91 / 620.13 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 282846.5 vs 282846, amarillo 295552.4 vs 295552, rojo 110315.1 vs 110315.
- Candidatos: 12965; pares candidato-edificio a <= 500 m: 2585986.
