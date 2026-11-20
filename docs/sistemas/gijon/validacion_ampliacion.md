# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 106592.49 / 122842.84 / 41823.67 | 106592.49 / 122842.84 / 41823.67 | 0.0000 |
| 100 | 247185.81 / 10918.04 / 13155.16 | 247185.81 / 10918.04 / 13155.16 | 0.0000 |
| 400 | 264944.44 / 5127.81 / 1186.75 | 264944.44 / 5127.81 / 1186.75 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 106592.5 vs 106592, amarillo 122842.8 vs 122843, rojo 41823.7 vs 41824.
- Candidatos: 8772; pares candidato-edificio a <= 500 m: 800139.
