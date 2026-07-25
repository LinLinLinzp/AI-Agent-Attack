# V50 Probe-Emit Aggressive

Ready-to-submit source:

```text
submission/current/v50_probe_emit_aggressive/submit.py
```

Purpose:

Same probe-to-emit idea as V49, but with a smaller safety multiplier and a higher cap.
This is the high-risk attempt to reach or exceed the observed public `~110` band.

Settings:

- `PROBE_REPS = 2` per K1 template.
- `REPLAY_SAFE = 0.985`.
- `UNIT_MEDIAN_MULT = 1.10`.
- `UNIT_MAX_MULT = 1.00`.
- `MAX_RETURN = 1580`.
- Fallback floor `unit >= 8.10s`.

Expected public LB:

```text
95-118 if the probe latency matches replay latency
<90 if the row measures slow and returns too few candidates
timeout/invalid if hosted replay tail latency is materially worse than probes
```
