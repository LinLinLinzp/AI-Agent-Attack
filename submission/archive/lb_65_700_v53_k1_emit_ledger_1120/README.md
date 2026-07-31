# V53 K1 Emit Ledger 1120

Public LB: `65.700`

Source copied from:

```text
submission/current/v53_k1_emit_ledger_1120/submit.py
```

Purpose:

- Test whether raw18 K1 emit can cross `100` when fixed `1250` is replaced with
  measured replay sizing.
- Hard cap: `1120`.

Result interpretation:

- Major regression versus C / V37 `88.965`.
- `65.700 / 0.09 = 730` K1-equivalent cells, so this behaved like an underfilled
  submission rather than a near-timeout high-volume replay.
- The user observed that scoring completed much faster than previous 12h+ runs.
  Treat live probe latency as too pessimistic for bulk replay sizing in this
  implementation.
