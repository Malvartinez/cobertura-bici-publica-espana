# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 445.40 / 947.00 / 3420.60 | 445.40 / 947.00 / 3420.60 | 0.0000 |
| 30 | 4671.63 / 139.43 / 1.94 | 4671.63 / 139.43 / 1.94 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 445.4 vs 445, amarillo 947.0 vs 947, rojo 3420.6 vs 3421.
- Candidatos: 629; pares candidato-edificio a <= 500 m: 87872.
