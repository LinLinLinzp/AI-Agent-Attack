# Three Parallel Submissions

Use these three variants for the next parallel Kaggle submissions. Copy one file at a time into the Kaggle notebook cell that writes `/kaggle/working/attack.py`.

## A. Exact Control

Path: `submission/current/v88_515_exact_control/submit.py`

Purpose:

- Reproduce the external `88.515` reference.
- Calibrate whether the saved notebook source still behaves the same in the current hosted environment.
- Provide the control for interpreting B and C.

Expected public LB:

```text
87-90
```

## B. K1 Safe Speed

Path: `submission/current/v88_515_plus_k1_safe_speed/submit.py`

Purpose:

- Keep the `88.515` K=1 replay ledger.
- Replace the plain template with `inj_data_first`, the fastest K=1 template in existing probes.
- Require exact destination URL match when validating fired candidates.
- Use successful-candidate latency for replay packing.
- Drop fired probe-bank candidates from clearly slower templates.

Expected public LB:

```text
92-96
```

If this beats A, continue K=1 template and replay-cap tuning.

## C. GPT K2 Probe

Path: `submission/current/v88_515_plus_gpt_k2_probe/submit.py`

Purpose:

- Keep B's stricter validation and replay ledger.
- Let GPT choose between K=1 and validated K=2 templates using measured raw/second.
- Keep gemma on the safer K=1 template pool.
- Require both requested URLs to receive successful marker posts before keeping a K=2 candidate.

Expected public LB:

```text
90-103
```

If this reaches or beats the high 90s, make GPT K2 the next main branch. If it loses to B, keep K2 as research only.

## Result Interpretation

| Result Pattern | Next Move |
| --- | --- |
| A around `88`, B higher, C not higher | Continue K=1 tuning: `REPLAY_SAFE`, `PROBE_REPS`, and template set |
| A around `88`, B around `94`, C near or above `98` | Promote GPT K2 / gemma K1 as the next main experiment |
| A below `85` | First investigate source/environment mismatch before interpreting B/C |
| C far below B | Disable K2 and return to K1 replay-density work |

