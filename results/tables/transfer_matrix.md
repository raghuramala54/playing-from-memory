### Cross-level transfer: evaluation max x, mean ± std over seeds (multiple of the random policy); diagonal = trained and tested on the same level

| Trained on | Model | Test 1-1 | Test 1-2 | Test 1-3 |
|:---|---:|---:|---:|---:|
| 1-1 | NatureCNN (baseline) | 910 ± 176 (1.0×) | 525 ± 181 (1.0×) | 382 ± 17 (1.2×) |
| 1-1 | + Channel attention (SE) | 845 ± 51 (1.0×) | 545 ± 137 (1.0×) | 358 ± 11 (1.1×) |
| 1-1 | + Spatial self-attention (ours) | 1,057 ± 30 (1.2×) | 664 ± 138 (1.2×) | 364 ± 26 (1.1×) |
| 1-2 | NatureCNN (baseline) | 746 ± 144 (0.9×) | 1,518 ± 292 (2.8×) | 362 ± 10 (1.1×) |
| 1-2 | + Channel attention (SE) | 808 ± 165 (0.9×) | 1,016 ± 85 (1.9×) | 357 ± 21 (1.1×) |
| 1-2 | + Spatial self-attention (ours) | 835 ± 217 (1.0×) | 1,585 ± 295 (3.0×) | 345 ± 35 (1.0×) |
| 1-3 | NatureCNN (baseline) | 670 ± 96 (0.8×) | 292 ± 90 (0.5×) | 1,087 ± 264 (3.3×) |
| 1-3 | + Channel attention (SE) | 627 ± 91 (0.7×) | 444 ± 38 (0.8×) | 1,056 ± 239 (3.2×) |
| 1-3 | + Spatial self-attention (ours) | 491 ± 86 (0.6×) | 349 ± 156 (0.7×) | 974 ± 330 (2.9×) |
| – | Random policy | 873 (1.0×) | 537 (1.0×) | 332 (1.0×) |
