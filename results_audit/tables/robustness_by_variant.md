### Clean score and mean retention per variant

| Group | Variant | Models | Clean score | No-op start | Sticky actions | Frozen HUD | 6-px shift |
|:---|---:|---:|---:|---:|---:|---:|---:|
| v1 · trained level | + SE | 9 | 2.19 | 1.02 | 0.80 | 0.99 | 0.64 |
| v1 · trained level | + spatial attn | 9 | 2.34 | 0.99 | 0.84 | 1.05 | 0.78 |
| v1 · trained level | NatureCNN | 9 | 2.51 | 0.83 | 0.76 | 0.99 | 0.72 |
| v1 · unseen level | + SE | 9 | 0.98 | 1.04 | 1.06 | 1.05 | 1.08 |
| v1 · unseen level | + spatial attn | 9 | 0.92 | 0.97 | 1.13 | 0.95 | 1.06 |
| v1 · unseen level | NatureCNN | 9 | 0.96 | 1.02 | 1.02 | 0.97 | 1.01 |
| v2 · training levels | Dense attn + aug | 1 | 1.82 | 0.96 | 0.98 | 1.02 | 0.91 |
| v2 · training levels | NatureCNN | 1 | 1.58 | 1.01 | 1.15 | 1.09 | 0.96 |
| v2 · training levels | NatureCNN + aug | 1 | 1.61 | 1.00 | 1.03 | 1.08 | 1.08 |
| v2 · training levels | Sparse attn + aug | 1 | 1.90 | 0.97 | 1.01 | 1.00 | 0.83 |
| v2 · held-out levels | Dense attn + aug | 1 | 1.26 | 1.02 | 0.95 | 1.03 | 0.99 |
| v2 · held-out levels | NatureCNN | 1 | 1.29 | 1.17 | 0.92 | 1.04 | 1.23 |
| v2 · held-out levels | NatureCNN + aug | 1 | 1.54 | 0.96 | 0.94 | 0.98 | 1.00 |
| v2 · held-out levels | Sparse attn + aug | 1 | 1.37 | 0.93 | 0.95 | 0.88 | 0.91 |
