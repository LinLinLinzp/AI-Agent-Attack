# LB 69.545: V39 GPT K3/K2 Aggressive

Public LB confirmed from the Kaggle submissions page: `69.545`.

Source:

- `submission/current/v39_gpt_k3_k2_aggressive/submit.py`

Key changes from C:

- added GPT K3 templates;
- increased high-K selection bias;
- kept gemma on K1 fallback;
- lowered K3 replay safety relative to K1/K2.

Interpretation:

This version scored far below C (`88.965`). The result is strong negative
evidence for broad GPT K3/K2 raw-density expansion in the current hosted
environment. Do not promote; only revisit high-K after a narrower hosted probe
shows stable raw per replay second.
