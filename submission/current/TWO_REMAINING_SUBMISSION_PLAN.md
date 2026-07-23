# V38 / V39 Remaining Submissions From 88.965

The current local submitted baseline is:

```text
v88_515_plus_gpt_k2_probe = 88.965 public LB
```

The two remaining submissions are numbered by Kaggle submit attempt:

```text
V38 = v38_hybrid_c_k2_plus_original_k1_safe
V39 = v39_gpt_k3_k2_aggressive
```

Future submissions should follow the same convention: current directory names
start with the lowercase submit number, such as `v40_strategy_name/`, while
notes use the uppercase label, such as `V40`.

Both variants are based on the C result, but they answer different questions:

1. Can we recover the K1 volume that B likely lost?
2. Can GPT K3/K2 raw-density move us toward the new ~110 public ceiling?

## V38. Hybrid C K2 + Original K1 Safe

Path: `submission/current/v38_hybrid_c_k2_plus_original_k1_safe/submit.py`

Purpose:

- Keep C's model-aware GPT K2 branch.
- Restore the original `88.515` K1 fallback wording with `plain` as the first template.
- Relax validation for K1 back to "successful marker post" while keeping K2 exact-URL validation.
- Disable aggressive probe-bank pruning with `BANK_COST_MULT = 999.0`.
- Lower K1 replay cap from C's `0.99` to `0.985` to avoid the exact-control timeout pattern.

Main changes versus C:

```text
K1 first template: inj_data_first -> plain
K1 validation: exact expected URL -> any successful marker http.post
K2 validation: still exact 2/2 expected URLs
BANK_COST_MULT: 1.10 -> 999.0
K2_SCORE_BIAS: 1.08 -> 1.12
K1_REPLAY_SAFE: 0.99 -> 0.985
K2_REPLAY_SAFE: 0.985 unchanged
```

Expected public LB:

```text
89-94, with a good result around 91-93
```

Interpretation:

- If V38 beats `88.965`, the main issue in B/C was K1 volume loss from strict
  validation and pruning.
- If V38 is near C, C's K2 gain is real but the K1 recovery is small.
- If V38 falls below C, keep C's stricter C source as the safer baseline and stop
  loosening K1 validation.

## V39. GPT K3/K2 Aggressive

Path: `submission/current/v39_gpt_k3_k2_aggressive/submit.py`

Purpose:

- Test whether GPT can reliably execute three distinct `http.post` calls in one candidate.
- Let GPT choose among K1, K2, and K3 templates by measured raw score per second.
- Keep gemma on K1 only.
- Require exact URL hits for K2 and K3 so high-K replay candidates are not inflated by false positives.
- Use tighter replay caps for higher K to reduce invalid-submission risk.

Main changes versus C:

```text
Adds K3 templates: k3_inj_list, k3_inj_force, k3_compact
K2_SCORE_BIAS: 1.08 -> 1.14
K3_SCORE_BIAS: new 1.22
K1_REPLAY_SAFE: 0.99 -> 0.985
K2_REPLAY_SAFE: 0.985 -> 0.980
K3_REPLAY_SAFE: new 0.970
Message formatter: adds {u2}
Selection: separate K2 and K3 score biases
Replay cap: separate K1/K2/K3 safe factors
```

Expected public LB:

```text
High variance: 88-100
Upside case: 105-112 if GPT K3 fires quickly and survives replay
```

Interpretation:

- If V39 reaches the mid-90s or higher, high-K raw density is the correct next branch.
- If V39 gets near or above 100, continue with narrower K3 templates and then test K4 only after K3 is stable.
- If V39 is below C, K3 is too expensive or unreliable in the hosted evaluator; stay with K2/K1.
- If V39 times out, keep the high-K idea but lower caps further before increasing K again.

## Recommended Submission Use

Submit both V38 and V39 in the two remaining slots:

```text
V38 = v38_hybrid_c_k2_plus_original_k1_safe
V39 = v39_gpt_k3_k2_aggressive
```

Do not submit the unchanged exact `88.515` control again; it timed out in the
current environment.

## Farther Plan

If V38 wins and V39 does not:

```text
Keep the C/V38 hybrid, tune replay caps around 0.975-0.990, and test K1 template order.
Target range: low-to-mid 90s.
```

If V39 wins:

```text
Promote GPT K3/K2 as the mainline.
Remove weak high-K templates using stderr telemetry if available.
Try a K3-only GPT branch with stronger fallback guards.
Only test K4 after K3 produces a stable score above 95.
Target range: 100-110.
```

If both fail:

```text
Return to C as the baseline.
Run smaller changes: C with K1_REPLAY_SAFE 0.985 only, and C with K2_REPLAY_SAFE 0.975 only.
```
