# Validacion de la ampliacion

Cobertura recalculada desde cero con Dijkstra multifuente (estaciones existentes + las k primeras nuevas, enganche exacto al nodo) y comparada con los totales registrados por el greedy (CELF).

| k nuevas | multifuente verde / amarillo / rojo | greedy verde / amarillo / rojo | dif. max (personas) |
|---:|---|---|---:|
| 0 | 8379.68 / 14589.10 / 10423.22 | 8379.68 / 14589.10 / 10423.22 | 0.0000 |
| 50 | 31052.29 / 1867.37 / 472.33 | 31052.29 / 1867.37 / 472.33 | 0.0000 |

- Diferencia maxima: **0.0000** personas.
- k = 0 frente a agregados.json: verde 8379.7 vs 8380, amarillo 14589.1 vs 14589, rojo 10423.2 vs 10423.
- Candidatos: 2562; pares candidato-edificio a <= 500 m: 77955.
