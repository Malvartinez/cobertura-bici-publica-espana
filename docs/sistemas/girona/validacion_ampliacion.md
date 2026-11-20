# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 56239.97 / 35588.73 / 16523.29 | 56239.97 / 35588.73 / 16523.29 | 0.0000 |
| 100 | 106397.54 / 1681.60 / 272.85 | 106397.54 / 1681.60 / 272.85 | 0.0000 |
| 200 | 108105.42 / 204.41 / 42.17 | 108105.42 / 204.41 / 42.17 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 56240.0 vs 56240, amarillo 35588.7 vs 35589, rojo 16523.3 vs 16523.
- Candidatos: 3915; pares candidato-edificio a <= 500 m: 415756.
