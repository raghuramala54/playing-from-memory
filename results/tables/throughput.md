### Training throughput (20 CPU cores, n_envs=8)

| Stage | Steps/s | Hours per 1M steps |
|:---|---:|---:|
| 1 env, random actions | 154.35 | 1.80 |
| 8 envs, random actions | 344.40 | 0.81 |
| PPO iteration: collect + update on CUDA | 254.18 | 1.09 |
