# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 1247491.95 / 413793.16 / 51961.88 | 1247491.95 / 413793.16 / 51961.88 | 0.0000 |
| 100 | 1548524.23 / 152937.07 / 11785.70 | 1548524.23 / 152937.07 / 11785.70 | 0.0000 |
| 500 | 1711283.85 / 1813.20 / 149.95 | 1711283.85 / 1813.20 / 149.95 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 1247492.0 vs 1247492, amarillo 413793.2 vs 413793, rojo 51961.9 vs 51962.
- Candidatos: 18453; pares candidato-edificio a <= 500 m: 2190254.
