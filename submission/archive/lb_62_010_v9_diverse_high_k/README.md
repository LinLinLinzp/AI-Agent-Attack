# LB 62.010 - v9 Diverse High-K

Archived from `submission/current/v9_diverse_high_k` after the public LB result
returned.

- Public LB: `62.010`
- Source: `submit.py`
- Strategy: model-aware template selection with GPT high-K probes and safer
  gemma K=1 templates.
- Key knobs: `MARGIN_S = 45.0`, `SLOWEST0 = 20.0`,
  `REPLAY_SAFE = 0.97`, `PROBE_REPS = 2`.

This run did not promote; it scored below the stronger K=1 replay-safe line.
