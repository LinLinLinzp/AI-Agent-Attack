# V56 / V57 / V58 Breakthrough Plan

This plan is now completed.

## Current Diagnosis

Baseline remains:

```text
C / V37: 88.965
```

Latest results:

```text
V53: 65.700
V54: 60.930
V55: 61.065
V56: 88.965
V57: timeout; Kaggle displayed Submission Format Error
V58: timeout; Kaggle displayed Submission Format Error
```

The user observed that V53/V54/V55 scored much faster than earlier 12h+ runs.
That makes the failure shape look like underfilled returned/effective replay
volume, not replay timeout pressure.

The important correction is that C's strength is not just template selection.
C live-validates every returned candidate during fill. V49/V50/V53/V54/V55 all
show that broad probe-to-emit or static emit does not transfer automatically.

## V56: Exact Tail Release

Source:

```text
submission/current/v56_c_exact_tail_release/submit.py
```

Purpose:

- Preserve C's full-hop exact validation.
- Reset cold-start `slowest` after warm-up.
- Reduce generation reserve to test whether C is losing candidates at the tail.

Expected:

```text
88-92 most likely
92-95 if generation reserve is a real bottleneck
timeout if C's original reserve was necessary
```

## V57: Hop1 Exact Fill

Source:

```text
submission/current/v57_c_hop1_exact_fill/submit.py
```

Purpose:

- Retest cheap fill, but require exact trace validation at hop1.
- Avoid V48's weak `successful_tool_calls` acceptance signal.
- Charge each accepted cheap-fill candidate by the full-hop replay unit.

Expected:

```text
88-96 most likely
96-100 if generation validation is the missing slack
<88 if hop1 exact still fails replay transfer
```

## V58: Static Fast Route 1120

Source:

```text
submission/current/v58_static_fast_route_1120/submit.py
```

Purpose:

- Direct high-risk test of the underfill hypothesis.
- Return `1120` model-routed K1 candidates with no live probe.
- If all replay, score is about `1120 * 0.09 = 100.8`.

Expected:

```text
~100.8 if fixed 1120 is replay-stable
90-100 if replay hit rate is high but imperfect
timeout if fixed static count exceeds the full-chain budget
<90 if isolated gateway replay is not predictive
```

## Result Reading

- `V56 > C`: exact-validation tail reserve matters; continue with smaller reserve
  and maybe `MARGIN_S = 35`.
- `V57 > C`: cheap exact fill works; tune audit cadence and maybe combine with
  V56's tail reserve.
- `V58 > 100`: public 100 is reachable through fixed underfill removal; tune count
  toward the observed 110 ceiling.
- `V58` invalid: stop fixed static count. The V52 failure was not just too-large
  `1250`.
- All three below C: C/V37 remains the mainline, and we need a Kaggle full-chain
  diagnostic notebook before more public submissions.

## Actual Results

```text
V56: 88.965
V57: timeout; Kaggle displayed Submission Format Error
V58: timeout; Kaggle displayed Submission Format Error
```

Interpretation:

- V56 tied C exactly. Lowering the generation-tail reserve and resetting warm-up
  `slowest` did not add public score, so C is not meaningfully generation-tail
  limited.
- V57 timed out, rejecting the current hop1 exact-fill shortcut. Even with exact
  URL/data checks and audits, cheap fill is not full-chain budget-safe.
- V58 timed out, rejecting fixed `1120` static K1 return. The earlier V52 fixed
  count failure was not merely because `1250` was too high.
- The 88.965 wall now looks like a replay-budget / raw-density frontier. Further
  K1 volume tuning is unlikely to cross 100 without a new per-candidate raw
  multiplier or a proven lower-cost replay path.
