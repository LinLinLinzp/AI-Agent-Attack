# V56 C Exact Tail Release

Source:

```text
submission/current/v56_c_exact_tail_release/submit.py
```

Baseline:

```text
C / V37: 88.965
```

Purpose:

- Keep C's full-hop exact validation and K1/K2 template family.
- Reset cold-start `slowest` after warm-up.
- Reduce generation reserve from `MARGIN_S = 60`, `MARGIN_MULT = 1.35` to
  `MARGIN_S = 45`, `MARGIN_MULT = 1.20`.

Experiment:

- Tests whether C is losing candidates at the tail of `AttackAlgorithm.run()`.
- Does not loosen replay-cost accounting and does not add unvalidated candidates.

Expected public LB:

```text
88-92 most likely
92-95 if generation tail reserve was a real bottleneck
timeout if run() tail reserve was already near the hosted limit
```

Interpretation:

- If V56 beats C, continue exact-validation margin tuning.
- If V56 is near C but lower, generation tail is not the main 100-point bottleneck.
- If V56 times out, restore C's original generation reserve.

Actual result:

```text
V56 public LB: 88.965
```

Interpretation:

- Completed and tied C exactly.
- Generation-tail reserve is not the missing 100-point bottleneck.
- Keep C/V37 as the reproducible baseline.
