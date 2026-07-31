# V48 Replay-Cost-Tax Fix

Ready-to-submit source:

```text
submission/current/v48_replay_cost_tax_fix/submit.py
```

Baseline:

```text
C / v88_515_plus_gpt_k2_probe = 88.965 public LB
```

Key changes from C:

- Adds one positive terminal K1 template: `Then reply OK only`.
- Resets `slowest` after warm-up so a cold-start sample does not inflate the search reserve.
- Keeps C's near-selected mixed probe bank; does not repeat V43's selected-only regression.
- For selected K1 fill, uses `max_tool_hops=1` cheap validation.
- Charges every cheap accepted K1 fill candidate by the measured full-hop replay unit from probes/audits.
- Runs periodic full-hop audits every 32 fill attempts; one audit miss disables fast fill.

Expected public LB:

```text
89-96 most likely
96-100 if C was materially generation-underfilled by full-hop fill
<88 if hop-1 cheap acceptance admits too many replay misses
```
