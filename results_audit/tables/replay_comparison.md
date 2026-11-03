### Agent vs. blind replay of its own best episode, both with no-op starts (retention = share of clean progress kept)

| Group | Variant | n | Agent retention (no-op) | Open-loop replay retention (no-op) | Agent − replay | Agent > replay | p (Wilcoxon) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| v1 · trained level | all | 27 | 0.95 | 0.83 | 0.12 | 48% | 0.03 |
| v2 · training levels | all | 64 | 0.99 | 0.89 | 0.10 | 56% | 0.05 |
| v1 · trained level | NatureCNN | 9 | 0.83 | 0.79 | 0.04 | 33% | 0.44 |
| v1 · trained level | + SE | 9 | 1.02 | 0.87 | 0.15 | 56% | 0.20 |
| v1 · trained level | + spatial attn | 9 | 0.99 | 0.82 | 0.17 | 56% | 0.16 |
| v2 · training levels | Dense attn + aug | 16 | 0.96 | 0.90 | 0.06 | 75% | 0.14 |
| v2 · training levels | NatureCNN | 16 | 1.01 | 0.88 | 0.13 | 50% | 0.31 |
| v2 · training levels | NatureCNN + aug | 16 | 1.00 | 0.88 | 0.11 | 62% | 0.11 |
| v2 · training levels | Sparse attn + aug | 16 | 0.97 | 0.88 | 0.09 | 38% | 0.43 |
