# V42 GPT K2 Analysis Compression

Public LB: `88.245`

Submitted source:

```text
submission/archive/lb_88_245_v42_gpt_k2_analysis_compression/submit.py
```

Diff from C / V39 `88.965` baseline:

- Added GPT-only compressed analysis-close K1/K2 templates.
- Kept GPT at K1/K2 only; no K3 and no multi-message batching.
- Lowered replay caps to `K1_REPLAY_SAFE = 0.985` and `K2_REPLAY_SAFE = 0.980`.
- Slightly reduced K2 score bias from `1.08` to `1.06`.

Interpretation:

The variant finished and stayed close to C, but did not promote. The result is
negative evidence for the compressed harmony-style templates and for lowering
C's replay cap in this form. Keep C's original GPT K2 wording as the mainline.
