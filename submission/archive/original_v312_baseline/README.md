# Original v312 Baseline

Archived from `submission/current/v312_baseline` as the original baseline kept
with the v7/v9 submission sweep.

- Public LB: not recorded in this archive entry.
- Source: `submit.py`
- Strategy: replay-safe K=1 fill selecting the highest measured raw-per-second
  template.
- Key knobs: `MARGIN_S = 60.0`, `SLOWEST0 = 24.0`,
  `REPLAY_SAFE = 0.96`, `PROBE_REPS = 2`.

Kept as a historical control. It is no longer an active current candidate.
