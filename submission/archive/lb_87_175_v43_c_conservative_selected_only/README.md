# V43 Conservative Selected-Only C Packing

Public LB: `87.175`

Submitted source:

```text
submission/archive/lb_87_175_v43_c_conservative_selected_only/submit.py
```

Diff from C / V39 `88.965` baseline:

- Kept C's K1/K2 template family.
- Required K2 templates to fire at least half the time during probing.
- Reduced K2 score bias from `1.08` to `1.02`.
- Returned only fired probes from the selected template, discarding non-selected
  bank candidates.
- Lowered replay caps to `K1_REPLAY_SAFE = 0.985` and `K2_REPLAY_SAFE = 0.980`.

Interpretation:

The selected-only lane underperformed C. This suggests C's mixed low-cost bank
is contributing useful cells, and the stricter K2 gate removes more signal than
it saves in replay stability.
