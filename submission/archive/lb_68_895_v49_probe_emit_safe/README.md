# V49 Probe-Emit Safe

Ready-to-submit source:

```text
submission/current/v49_probe_emit_safe/submit.py
```

Purpose:

Use a few full-hop probes only to estimate the current model row's replay cost, then
emit a larger unvalidated K1 portfolio from the selected reliable template. This tests
whether C/V48 are underfilled because generation-time live validation is the real tax.

Settings:

- `PROBE_REPS = 3` per K1 template.
- `REPLAY_SAFE = 0.955`.
- `UNIT_MEDIAN_MULT = 1.24`.
- `UNIT_MAX_MULT = 1.08`.
- `MAX_RETURN = 1320`.
- Fallback floor `unit >= 9.20s`.

Expected public LB:

```text
88-96 if measured unit stays near C
100-112 if hosted full-hop K1 replay unit is <= about 7.7s
timeout/invalid if the probe underestimates replay cost badly
```
