# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 34680.57 / 12322.43 / 0.00 | 34680.57 / 12322.43 / 0.00 | 0.0000 |
| 14 | 47003.00 / 0.00 / 0.00 | 47003.00 / 0.00 / 0.00 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 34680.6 vs 34681, amarillo 12322.4 vs 12322, rojo 0.0 vs 0.
- Candidatos: 515; pares candidato-edificio a <= 500 m: 48281.
