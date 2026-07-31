# V54 K2 Probe Ledger 800

Public LB: `60.930`

Source copied from:

```text
submission/current/v54_k2_probe_ledger_800/submit.py
```

Purpose:

- Aggressive raw34 K2 test.
- Select exact K2 only after live probes show two successful EXFIL posts.
- K2 hard cap: `800`; K1 fallback cap: `1120`.

Result interpretation:

- Major regression versus C / V37 `88.965`.
- Raw34 did not transfer into a high public score in this full-chain submission.
- The short scoring time suggests low returned/effective replay volume rather
  than replay timeout pressure.
