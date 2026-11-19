# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 43821.16 / 88101.23 / 19758.62 | 43821.16 / 88101.23 / 19758.62 | 0.0000 |
| 100 | 147301.85 / 3610.20 / 768.95 | 147301.85 / 3610.20 / 768.95 | 0.0000 |
| 200 | 151158.67 / 394.65 / 127.69 | 151158.67 / 394.65 / 127.69 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 43821.2 vs 43821, amarillo 88101.2 vs 88101, rojo 19758.6 vs 19759.
- Candidatos: 4077; pares candidato-edificio a <= 500 m: 267584.
