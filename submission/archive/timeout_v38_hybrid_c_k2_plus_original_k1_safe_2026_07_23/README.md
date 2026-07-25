# Timeout - V38 Hybrid C K2 + Original K1 Safe

Archived after `V38` timed out.

- Result: timeout / invalid submission
- Submitted source: `submit.py`
- Lineage: C (`88.965`) follow-up
- Source before archive: `submission/current/v38_hybrid_c_k2_plus_original_k1_safe/submit.py`

Key changes from C:

- restored original-style K1 wording and K1 volume;
- kept the GPT K2 branch from C;
- used safer replay settings than the exact `88.515` control, but still not enough for this hosted run.

Interpretation:

This version was intended to recover K1 volume while retaining C's K2 gain. The
timeout means the current K1/K2 replay mix is not stable enough. Do not promote
or resubmit unchanged.
