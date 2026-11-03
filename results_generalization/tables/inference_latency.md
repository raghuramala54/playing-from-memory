### Policy latency at batch 1 (budget 66.6 ms)

| Variant | Device | Mean (ms) | p95 (ms) | Real-time |
|:---|---:|---:|---:|---:|
| NatureCNN | CPU | 0.930 | 3.574 | yes |
| NatureCNN + aug | CPU | 0.570 | 0.667 | yes |
| Dense attention + aug | CPU | 0.699 | 0.731 | yes |
| Sparse attention + aug (ours) | CPU | 1.151 | 1.206 | yes |
| NatureCNN | CUDA | 0.348 | 0.389 | yes |
| NatureCNN + aug | CUDA | 0.343 | 0.377 | yes |
| Dense attention + aug | CUDA | 0.471 | 0.503 | yes |
| Sparse attention + aug (ours) | CUDA | 0.647 | 0.686 | yes |
