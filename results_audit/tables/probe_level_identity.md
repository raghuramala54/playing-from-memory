### Level information in encoder features on shared frames (22 levels; probe chance 0.05; folds split by episode)

| Family | Encoder | Models | Level-explained variance η² | ± sd | Probe accuracy, HUD hidden | Probe accuracy, HUD visible |
|:---|---:|---:|---:|---:|---:|---:|
| v1 | NatureCNN | 9 | 0.234 | 0.070 | 0.781 | 0.831 |
| v1 | + SE | 9 | 0.259 | 0.082 | 0.791 | 0.827 |
| v1 | + spatial attn | 9 | 0.253 | 0.053 | 0.799 | 0.832 |
| v2 | Dense attn + aug | 1 | 0.183 | – | 0.898 | 0.955 |
| v2 | NatureCNN + aug | 1 | 0.184 | – | 0.894 | 0.965 |
| v2 | NatureCNN | 1 | 0.207 | – | 0.889 | 0.981 |
| v2 | Sparse attn + aug | 1 | 0.179 | – | 0.897 | 0.957 |
| control | untrained encoder (control) | 1 | 0.363 | – | 0.689 | 0.811 |
| control | raw pixels 15×16 (control) | 1 | 0.789 | – | 0.785 | 0.820 |
