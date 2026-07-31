# V58 Static Fast Route 1120

Result: timeout

Kaggle displayed: `Submission Format Error`

Source copied from:

```text
submission/current/v58_static_fast_route_1120/submit.py
```

Purpose:

- Direct fixed-count test of `1120` model-routed K1 candidates.
- Theoretical public score if stable: `100.8`.

Result interpretation:

- Exceeded the full-chain time budget before producing a valid served output.
- Fixed large static K1 return is budget-unsafe; V52's fixed-count failure was not only
  because `1250` was too high.
- Do not continue fixed-count K1 without a full-chain diagnostic.
