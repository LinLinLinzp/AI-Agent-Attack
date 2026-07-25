# LB 77.625: V40 Multi-Message K1 Batching

Public LB reported by user: `77.625`.

Source:

- `submission/current/v40_multimessage_k1_batching/submit.py`

Key changes from C:

- returned multi-message candidates with two or three K1 user turns;
- attempted to share one fresh replay reset across several stable K1 actions;
- used lower replay safety for batch2 and batch3 than for single-message K1.

Interpretation:

Continuation batching did not pay off in this implementation. The score is far
below C (`88.965`), so the likely loss is replay reliability or slower hosted
continuation. Do not promote this branch as the mainline.
