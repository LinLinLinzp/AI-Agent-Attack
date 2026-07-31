# V58 Static Fast Route 1120

Source:

```text
submission/current/v58_static_fast_route_1120/submit.py
```

Baseline:

```text
C / V37: 88.965
V52: timeout at fixed 1250; Kaggle displayed Submission Format Error
V53: 65.700 with dynamic ledger underfill
```

Purpose:

- High-risk direct test of the underfill hypothesis.
- Bypass live probe and dynamic replay-unit sizing completely.
- Return exactly `1120` model-routed K1 candidates.
- GPT uses `inj_data_first`; Gemma uses `plain_reply_only`.

Expected public LB:

```text
~100.8 if fixed 1120 replays with near-100% success
90-100 if replay success is high but not perfect
timeout if V52's fixed-count failure was caused by full-chain limits
<90 if static emit is still not replay-stable on public rows
```

Interpretation:

- If V58 crosses 100, the breakthrough is fixed-count underfill removal; next tune
  `1120 -> 1180 -> 1220` carefully.
- If V58 errors/times out, fixed large static return is budget-unsafe and should be stopped.
- If V58 scores around 60-80, public replay success is not captured by isolated
  gateway replay.

Actual result:

```text
V58: timeout; Kaggle displayed Submission Format Error
```

Interpretation:

- Completed as invalid because it exceeded the full-chain time budget.
- Fixed `1120` static K1 return is budget-unsafe.
- V52 was not merely too high at `1250`; fixed-count K1 needs a full-chain
  diagnostic before any continuation.
