# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 39405.28 / 82338.81 / 53337.90 | 39405.28 / 82338.81 / 53337.90 | 0.0000 |
| 100 | 152307.97 / 20380.51 / 2393.52 | 152307.97 / 20380.51 / 2393.52 | 0.0000 |
| 200 | 172054.49 / 2806.02 / 221.50 | 172054.49 / 2806.02 / 221.50 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 39405.3 vs 39405, amarillo 82338.8 vs 82339, rojo 53337.9 vs 53338.
- Candidatos: 5644; pares candidato-edificio a <= 500 m: 556757.
