# V53 / V54 / V55 Submission Plan

## Purpose

Use the three daily submissions as a decision experiment, not three
near-identical parameter tweaks. This plan is now completed.

Current baseline remains:

```text
C / V37: 88.965
```

Latest calibration:

```text
V51: 87.505
V52: timeout; Kaggle displayed Submission Format Error
```

Gateway replay validation shows the opportunity:

```text
K1 N=1250 isolated replay: ~112.5
GPT K2 N=800 isolated replay: 136.0
```

V52 shows that isolated replay is not enough; full-chain submissions need lower
caps, live probes, and replay-margin sizing.

## V53: K1 Emit Ledger 1120

Source:

```text
submission/current/v53_k1_emit_ledger_1120/submit.py
```

Purpose:

- Control for whether raw18 K1 emit can cross the `100` boundary when fixed
  `1250` is replaced with measured replay sizing.
- Hard cap `1120`, barely above the `100` threshold.

Expected public LB:

```text
98-101 if K1 emit transfers safely
<90 if unvalidated K1 replay success is still too low
format error if full-chain overhead remains much heavier than isolated replay
```

## V54: K2 Probe Ledger 800

Source:

```text
submission/current/v54_k2_probe_ledger_800/submit.py
```

Purpose:

- Aggressive raw34 test.
- Select `k2_inj_list` only if live probes are exact two-post EXFIL.
- K2 hard cap `800`; K1 fallback cap `1120`.

Expected public LB:

```text
100-120 if GPT selects K2 and Gemma falls back to K1
>120 if both rows select stable K2
<90 or error if K2 probe-to-emit does not transfer
```

## V55: K2 Conservative 650

Source:

```text
submission/current/v55_k2_conservative_650/submit.py
```

Purpose:

- Same raw34 test as V54, but lower risk.
- K2 hard cap `650`; K1 fallback cap `1050`.
- If GPT selects K2 and Gemma falls back to K1, the target is still slightly above
  `100`.

Expected public LB:

```text
~102 if GPT K2 + Gemma K1
~110 if both rows K2
~94 if both rows K1
```

## Result Reading

- `V54 > 100`: raw34 path is live; next tune K2 cap upward or specialize probes.
- `V55 > 100` but `V54` errors: K2 path is live but cap-sensitive; continue conservative K2.
- `V53 > 100` but K2 variants fail: K1 emit with ledger is enough; tune K1 cap slowly.
- All three below C or invalid: stop public submissions and run a full-chain K2 notebook before more attempts.

## Actual Results

```text
V53: 65.700
V54: 60.930
V55: 61.065
```

The three submissions scored much faster than prior 12h+ runs. Treat that as
evidence that the variants returned too little replay work, not that they were
close to the replay timeout edge.

Interpretation:

- V53 is roughly `65.700 / 0.09 = 730` K1-equivalent cells. That is consistent
  with the dynamic ledger choosing a high live-probe `replay_unit` and returning
  only around the early live-fill volume.
- V54 and V55 clustered near `61`, despite very different K2 caps. This rejects
  the current K2 probe-to-emit transfer; the public score did not behave like a
  stable raw34 lane.
- The next breakthrough should separate live template validation from replay
  sizing. Live probe latency is too pessimistic when used directly as bulk replay
  cost.
