# V51 C Bank-Wide / K2 Edge

Source:

```text
submission/current/v51_c_bank_wide_k2_edge/submit.py
```

Baseline:

- Starts from `v88_515_plus_gpt_k2_probe`, public LB `88.965`.
- Keeps full-hop exact validation, measured replay-cost packing, and C's K1/K2 template family.

Changes:

- `BANK_COST_MULT`: `1.10 -> 1.35`.
- `K2_SCORE_BIAS`: `1.08 -> 1.12`.

Purpose:

- Test whether C lost a few validated probe-bank cells by pruning near-selected lanes too tightly.
- Slightly favor GPT K2 only through the existing raw/sec selector, without adding new templates or unvalidated tails.

Expected outcome:

- Low-risk calibration version.
- Expected public LB range: `88.5-90.5`.
- A meaningful gain would suggest C is selection/packing limited, not template limited.
