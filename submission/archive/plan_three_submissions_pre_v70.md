# Three Parallel Submissions

Use these three variants for the next parallel Kaggle submissions. Copy one file at a time into the Kaggle notebook cell that writes `/kaggle/working/attack.py`.

## A. Exact Control

Path: `submission/current/v88_515_exact_control/submit.py`

Status:

```text
TIMED OUT on 2026-07-22. Do not resubmit unchanged.
```

Purpose:

- Reproduce the external `88.515` reference.
- Calibrate whether the saved notebook source still behaves the same in the current hosted environment.
- Provide the control for interpreting B and C.

Expected public LB:

```text
87-90
```

Observed result:

```text
timeout / invalid submission
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

Observed result:

```text
86.720
```

Interpretation:

- It finished, so the stricter K1 variant did avoid the exact-control timeout.
- It underperformed the external `88.515`, so `inj_data_first` plus exact URL
  validation and probe-bank pruning did not produce a net throughput gain.
- Most likely, strict validation/pruning reduced returned volume more than the
  faster template recovered.
- Do not promote B as the mainline.

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

Observed result:

```text
88.965
```

Interpretation:

- This is the best local submitted result in this round.
- It beat B by `2.245` points, about `25` K=1-equivalent cells.
- It beat the external `88.515` reference by `0.450` points, about `5` K=1-equivalent cells.
- Without stderr telemetry we cannot prove the gain came directly from K2, but the model-aware K2 branch is now worth a cleaner follow-up.

## Result Interpretation

| Result Pattern | Next Move |
| --- | --- |
| A around `88`, B higher, C not higher | Continue K=1 tuning: `REPLAY_SAFE`, `PROBE_REPS`, and template set |
| A around `88`, B around `94`, C near or above `98` | Promote GPT K2 / gemma K1 as the next main experiment |
| A below `85` | First investigate source/environment mismatch before interpreting B/C |
| A times out | Treat `REPLAY_SAFE = 0.99` as too aggressive in this environment; archive A and make the next K=1 control a lower replay-safe variant before changing templates |
| C far below B | Disable K2 and return to K1 replay-density work |

Actual pattern:

```text
A timeout, B = 86.720, C = 88.965
```

Next move:

```text
Promote C as the current reproducible public baseline, then run a cleaner K2-vs-K1 replay-safe A/B around 0.985/0.975.
```
