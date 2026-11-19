# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 55944.09 / 79380.05 / 39757.86 | 55944.09 / 79380.05 / 39757.86 | 0.0000 |
| 100 | 164657.76 / 9470.44 / 953.80 | 164657.76 / 9470.44 / 953.80 | 0.0000 |
| 200 | 174266.34 / 764.71 / 50.95 | 174266.34 / 764.71 / 50.95 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 55944.1 vs 55944, amarillo 79380.0 vs 79380, rojo 39757.9 vs 39758.
- Candidatos: 5644; pares candidato-edificio a <= 500 m: 579405.
