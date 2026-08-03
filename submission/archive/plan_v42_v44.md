# V42 / V43 / V44 Completed Three-Submission Plan From 88.965

Current reproducible baseline:

```text
v88_515_plus_gpt_k2_probe = 88.965 public LB
```

Recent negative evidence:

```text
V38 = timeout
V39 = 69.545 public LB
V40 = 77.625 public LB
V41 = 78.135 public LB
V42 = 88.245 public LB
V43 = 87.175 public LB
V44 = 87.390 public LB
```

These three submissions stopped expanding K. The public surface still appears
to be a `http.post(data=SECRET_MARKER)` throughput problem; the versions tested
three conservative ways to improve or stabilize that throughput.

## Result Summary

| Version | Public LB | Decision |
| --- | ---: | --- |
| V42 | `88.245` | Did not promote; compression was slightly worse than C. |
| V43 | `87.175` | Did not promote; selected-only packing lost too much useful bank volume. |
| V44 | `87.390` | Did not promote; K1-only safety is stable but lower than C. |

Combined interpretation:

```text
C / v88_515_plus_gpt_k2_probe = 88.965 remains the baseline.
```

## V42. GPT K1/K2 Analysis Compression

Path:

```text
submission/current/v42_gpt_k2_analysis_compression/submit.py
```

Diff from C:

- Keeps gemma on C's K1 templates.
- Keeps GPT K1/K2 only; no K3, no multi-message batching.
- Adds two GPT-only compressed analysis-close templates:
  - `compress_k1_empty_analysis`
  - `compress_k2_empty_analysis`
- Slightly lowers replay caps to `K1_REPLAY_SAFE = 0.985` and `K2_REPLAY_SAFE = 0.980`.

Purpose:

Test whether the useful part of the public harmony idea is just shorter
analysis-channel closure, without the native tool-call prefill or K3 branch that
hurt V41.

Expected public range:

```text
88-94
```

Actual interpretation:

V42 was near C but below it. Compression is at best a small effect in this
implementation, and the lower replay caps probably removed more volume than
they saved. Keep C's original GPT K2 wording.

## V43. Conservative Selected-Only C Packing

Path:

```text
submission/current/v43_c_conservative_selected_only/submit.py
```

Diff from C:

- Same C K1/K2 template family.
- K2 must fire at least half the time during probe selection.
- K2 score bias reduced from `1.08` to `1.02`.
- Only fired probes from the selected template are returned; non-selected bank probes are discarded.
- Replay caps are lowered to `K1_REPLAY_SAFE = 0.985` and `K2_REPLAY_SAFE = 0.980`.

Purpose:

Test whether C loses replay budget to non-selected probe-bank candidates and
whether a cleaner selected lane can recover stable fill volume.

Expected public range:

```text
86-91
```

Actual interpretation:

V43 is clearly below C. Returning only the selected lane is not the right
stability improvement; C's non-selected low-cost bank candidates appear to
contribute meaningful score.

## V44. Replay-Safe K1-Only Reference

Path:

```text
submission/current/v44_k1_replay_safe_reference/submit.py
```

Diff from exact 88.515 control:

- Uses the external 88.515 K1-only uniform three-probe race.
- Lowers `REPLAY_SAFE` from `0.990` to `0.982`.
- Does not add K2, K3, continuation, or harmony/prefill.

Purpose:

Provide a clean K1-only reference after the exact 88.515 control timed out. This
is not the most aggressive scoring candidate; it is the calibration hedge.

Expected public range:

```text
86-89
```

Actual interpretation:

V44 finished in the expected calibration range. The K1-only line is stable with
the lower cap, but it does not explain the path to 100 by itself.

## Submission Order

Submitted as:

```text
V42 = v42_gpt_k2_analysis_compression
V43 = v43_c_conservative_selected_only
V44 = v44_k1_replay_safe_reference
```

No version beat `88.965`. Promote only C for the next planning round.
