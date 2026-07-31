# V55 K2 Conservative 650

Public LB: `61.065`

Source copied from:

```text
submission/current/v55_k2_conservative_650/submit.py
```

Purpose:

- Conservative version of the V54 raw34 K2 test.
- K2 hard cap: `650`; K1 fallback cap: `1050`.

Result interpretation:

- Major regression versus C / V37 `88.965`.
- The score is nearly identical to V54, so lower K2 cap did not fix the failure.
- Treat the current K2 probe-to-emit transfer as rejected until a full-chain
  notebook proves that the selected K2 message survives bulk replay.
