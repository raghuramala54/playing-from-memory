### Evaluation: 10 episodes per seed and level (stochastic policy); ± = std over seeds

| Level | Agent | Seeds | Episodes | Max x | Flag rate (%) | Reward |
|:---|---:|---:|---:|---:|---:|---:|
| 1-1 | NatureCNN (baseline) | 3 | 30 | 910 ± 176 | 0.0 ± 0.0 | 830 ± 170 |
| 1-1 | + Channel attention (SE) | 3 | 30 | 845 ± 51 | 0.0 ± 0.0 | 767 ± 50 |
| 1-1 | + Spatial self-attention (ours) | 3 | 30 | 1,057 ± 30 | 0.0 ± 0.0 | 974 ± 28 |
| 1-1 | Random policy | 3 | 30 | 873 ± 275 | 3.3 ± 5.8 | 715 ± 222 |
| 1-2 | NatureCNN (baseline) | 3 | 30 | 1,518 ± 292 | 0.0 ± 0.0 | 1,429 ± 286 |
| 1-2 | + Channel attention (SE) | 3 | 30 | 1,016 ± 85 | 0.0 ± 0.0 | 838 ± 179 |
| 1-2 | + Spatial self-attention (ours) | 3 | 30 | 1,585 ± 295 | 0.0 ± 0.0 | 1,470 ± 287 |
| 1-2 | Random policy | 3 | 30 | 537 ± 131 | 0.0 ± 0.0 | 403 ± 101 |
| 1-3 | NatureCNN (baseline) | 3 | 30 | 1,087 ± 264 | 0.0 ± 0.0 | 1,011 ± 260 |
| 1-3 | + Channel attention (SE) | 3 | 30 | 1,056 ± 239 | 0.0 ± 0.0 | 981 ± 235 |
| 1-3 | + Spatial self-attention (ours) | 3 | 30 | 974 ± 330 | 0.0 ± 0.0 | 900 ± 325 |
| 1-3 | Random policy | 3 | 30 | 332 ± 26 | 0.0 ± 0.0 | 265 ± 26 |
