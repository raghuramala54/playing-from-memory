### How episodes ended (share): death, stall (no progress for STALL_STEPS decisions), flag, end of replay

| Group | Condition | death | flag | replay_end | stall |
|:---|---:|---:|---:|---:|---:|
| v1 · trained level | Clean | 0.96 | 0.01 | 0.00 | 0.03 |
| v1 · trained level | No-op start | 0.99 | 0.00 | 0.00 | 0.01 |
| v1 · trained level | Sticky actions | 0.96 | 0.00 | 0.00 | 0.04 |
| v1 · trained level | Frozen HUD | 0.96 | 0.01 | 0.00 | 0.03 |
| v1 · trained level | 6-px shift | 0.97 | 0.00 | 0.00 | 0.03 |
| v1 · trained level | Open-loop replay + no-op start | 0.91 | 0.07 | 0.01 | 0.00 |
| v1 · unseen level | Clean | 0.92 | 0.00 | 0.00 | 0.08 |
| v1 · unseen level | No-op start | 0.94 | 0.00 | 0.00 | 0.06 |
| v1 · unseen level | Sticky actions | 0.94 | 0.00 | 0.00 | 0.06 |
| v1 · unseen level | Frozen HUD | 0.93 | 0.00 | 0.00 | 0.07 |
| v1 · unseen level | 6-px shift | 0.90 | 0.00 | 0.00 | 0.10 |
| v2 · training levels | Clean | 1.00 | 0.00 | 0.00 | 0.00 |
| v2 · training levels | No-op start | 0.99 | 0.00 | 0.00 | 0.01 |
| v2 · training levels | Sticky actions | 1.00 | 0.00 | 0.00 | 0.00 |
| v2 · training levels | Frozen HUD | 1.00 | 0.00 | 0.00 | 0.00 |
| v2 · training levels | 6-px shift | 0.99 | 0.00 | 0.00 | 0.01 |
| v2 · training levels | Open-loop replay + no-op start | 0.93 | 0.00 | 0.07 | 0.00 |
| v2 · held-out levels | Clean | 0.99 | 0.00 | 0.00 | 0.01 |
| v2 · held-out levels | No-op start | 1.00 | 0.00 | 0.00 | 0.00 |
| v2 · held-out levels | Sticky actions | 0.99 | 0.00 | 0.00 | 0.01 |
| v2 · held-out levels | Frozen HUD | 1.00 | 0.00 | 0.00 | 0.00 |
| v2 · held-out levels | 6-px shift | 0.99 | 0.00 | 0.00 | 0.01 |
