### Do training-level measurements predict unseen-level score? (v1 models; Holm over measures)

| Measure (training levels) | n models | Spearman ρ | 95% CI | p | Within-level ρ | Within-level p | p (Holm) | Within-level p (Holm) |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| Policy entropy | 27 | 0.802 | 0.59 to 0.91 | 0.000 | -0.010 | 0.961 | 0.000 | 1.000 |
| Training-level score | 27 | -0.762 | -0.87 to -0.58 | 0.000 | 0.044 | 0.828 | 0.000 | 1.000 |
| Level information η² | 27 | 0.589 | 0.19 to 0.80 | 0.001 | 0.207 | 0.300 | 0.012 | 1.000 |
| Shift sensitivity (KL) | 27 | -0.515 | -0.71 to -0.18 | 0.006 | -0.168 | 0.401 | 0.054 | 1.000 |
| Closed-loop index (sticky) | 27 | 0.482 | 0.09 to 0.81 | 0.011 | -0.272 | 0.170 | 0.088 | 1.000 |
| No-op retention | 27 | -0.293 | -0.62 to 0.09 | 0.137 | -0.161 | 0.423 | 0.962 | 1.000 |
| Dormant neurons (τ = 0.1) | 27 | 0.287 | -0.08 to 0.58 | 0.147 | 0.126 | 0.532 | 0.962 | 1.000 |
| Attention entropy | 9 | -0.217 | -0.84 to 0.72 | 0.576 | 0.300 | 0.433 | 1.000 | 1.000 |
| Sticky-action retention | 27 | 0.129 | -0.31 to 0.59 | 0.522 | -0.220 | 0.269 | 1.000 | 1.000 |
| Closed-loop index (no-op) | 27 | 0.125 | -0.28 to 0.59 | 0.534 | -0.226 | 0.257 | 1.000 | 1.000 |
| Shift retention | 27 | 0.117 | -0.32 to 0.53 | 0.560 | -0.082 | 0.683 | 1.000 | 1.000 |
| Frozen-HUD retention | 27 | 0.008 | -0.43 to 0.48 | 0.968 | -0.335 | 0.087 | 1.000 | 1.000 |
