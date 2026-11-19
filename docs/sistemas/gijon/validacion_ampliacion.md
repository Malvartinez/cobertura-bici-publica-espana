# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 118742.35 / 112351.56 / 40165.09 | 118742.35 / 112351.56 / 40165.09 | 0.0000 |
| 100 | 250115.10 / 8538.26 / 12605.64 | 250115.10 / 8538.26 / 12605.64 | 0.0000 |
| 400 | 264730.83 / 5424.11 / 1104.06 | 264730.83 / 5424.11 / 1104.06 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 118742.4 vs 118742, amarillo 112351.6 vs 112352, rojo 40165.1 vs 40165.
- Candidatos: 8772; pares candidato-edificio a <= 500 m: 775246.
