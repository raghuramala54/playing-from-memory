### Variants and model size

| Variant | Encoder | Block | Augmentation | Block params | Total params |
|:---|---:|---:|---:|---:|---:|
| NatureCNN | nature | baseline | no | 0 | 4,407,976 |
| NatureCNN + aug | nature | baseline | yes | 0 | 4,407,976 |
| Dense attention + aug | nature | spatial | yes | 16,385 | 4,424,361 |
| Sparse attention + aug (ours) | nature | sparse | yes | 24,833 | 4,432,809 |
