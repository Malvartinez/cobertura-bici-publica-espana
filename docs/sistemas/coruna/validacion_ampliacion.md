# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 131993.86 / 108573.65 / 10709.49 | 131993.86 / 108573.65 / 10709.49 | 0.0000 |
| 100 | 245067.92 / 5031.26 / 1177.82 | 245067.92 / 5031.26 / 1177.82 | 0.0000 |
| 301 | 251260.76 / 14.85 / 1.39 | 251260.76 / 14.85 / 1.39 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 131993.9 vs 131994, amarillo 108573.7 vs 108574, rojo 10709.5 vs 10709.
- Candidatos: 5183; pares candidato-edificio a <= 500 m: 602860.
