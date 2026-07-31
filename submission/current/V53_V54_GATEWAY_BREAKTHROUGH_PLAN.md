# V53 / V54 Gateway Breakthrough Plan

Historical note: this two-version plan is superseded by
`submission/current/V53_V55_SUBMISSION_PLAN.md`, which adds V55 as the
conservative K2 raw34 cap test.

## Result Interpretation

Latest public results:

```text
V51: 87.505
V52: timeout; Kaggle displayed Submission Format Error
```

Gateway replay validation still shows the underlying replay path can exceed `100`
in isolated runs:

```text
static_v52_plain_reply, gpt_oss, N=1250: 112.58
static_v52_plain_reply, gemma,   N=1250: 112.50
gpt_k2_inj_list_only,  gpt_oss, N=800:  136.00
```

The combined lesson is not "static count is safe"; it is narrower:

- raw18 K1 and raw34 K2 replay paths can score above `100` when replayed in isolation;
- V52 proves fixed `1250` emit times out across the official full-chain submission;
- the next versions must restore measured replay-margin sizing and hard caps.

## V53: K1 Emit Ledger 1120

Source:

```text
submission/current/v53_k1_emit_ledger_1120/submit.py
```

Purpose:

- Keep the V52/static K1 idea but remove the fixed `1250` count.
- Probe a small K1 family, then size returned candidates by conservative replay unit.
- Hard cap at `1120`, barely above the `100` threshold if replay success is high.

Expected public LB:

```text
98-101 if K1 emit is stable and the 1120 cap survives hosted replay
<90 if unvalidated K1 emit still loses replay predicates
format error if full-chain overhead is still much heavier than gateway replay validation
```

## V54: K2 Probe Ledger 800

Source:

```text
submission/current/v54_k2_probe_ledger_800/submit.py
```

Purpose:

- Test the strongest high-density signal: exact two-post `k2_inj_list` is `34 raw = 0.17` per candidate.
- Select K2 only if current-row probes are exact; otherwise fall back to K1.
- Use measured replay unit plus hard caps: `800` for K2, `1120` for K1.

Expected public LB:

```text
100-120 if GPT selects K2 and Gemma falls back to K1
>120 if both rows select stable K2
<90 if probe-to-emit does not transfer to replay
```

## Submission Reading

- Submit V53 first if the priority is a cautious 100-threshold test.
- Submit V54 first if the priority is a real breakthrough attempt.
- Do not submit any fixed `1250` or `2000` count variant until one ledger version succeeds.
