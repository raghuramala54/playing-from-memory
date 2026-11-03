### Model size (actor-critic policy incl. heads)

| Model | Block params | Total policy params | Overhead vs baseline (%) | Mixes positions | Mixes channels |
|:---|---:|---:|---:|---:|---:|
| NatureCNN (baseline) | 0 | 4,407,976 | 0.00 | no | no |
| + Channel attention (SE) | 580 | 4,408,556 | 0.01 | no | yes |
| + Spatial self-attention (ours) | 16,385 | 4,424,361 | 0.37 | yes | yes |
| + Pointwise MLP (capacity control) | 16,385 | 4,424,361 | 0.37 | no | yes |
