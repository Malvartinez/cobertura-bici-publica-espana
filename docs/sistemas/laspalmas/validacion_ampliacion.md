# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 78360.63 / 95977.05 / 209685.32 | 78360.63 / 95977.05 / 209685.32 | 0.0000 |
| 100 | 272509.74 / 79416.97 / 32096.30 | 272509.74 / 79416.97 / 32096.30 | 0.0000 |
| 400 | 372885.77 / 9303.31 / 1833.92 | 372885.77 / 9303.31 / 1833.92 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 78360.6 vs 78361, amarillo 95977.0 vs 95977, rojo 209685.3 vs 209685.
- Candidatos: 8519; pares candidato-edificio a <= 500 m: 1752675.
