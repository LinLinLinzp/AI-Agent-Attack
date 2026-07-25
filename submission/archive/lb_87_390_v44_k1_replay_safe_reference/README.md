# V44 Replay-Safe K1 Reference

Public LB: `87.390`

Submitted source:

```text
submission/archive/lb_87_390_v44_k1_replay_safe_reference/submit.py
```

Diff from exact `88.515` reference:

- Kept the external `88.515` K1-only uniform three-probe race.
- Lowered `REPLAY_SAFE` from `0.990` to `0.982`.
- Did not add K2, K3, continuation, or harmony/prefill behavior.

Interpretation:

The run finished but did not beat C or the external `88.515` reference. Pure
K1 with extra replay headroom is stable, but it leaves too much score on the
table. The current best path remains C's GPT K2 / gemma K1 branch.
