# V57 C Hop1 Exact Fill

Result: timeout

Kaggle displayed: `Submission Format Error`

Source copied from:

```text
submission/current/v57_c_hop1_exact_fill/submit.py
```

Purpose:

- Retest cheap fill with exact hop1 trace checks and periodic full-hop audits.

Result interpretation:

- Exceeded the full-chain time budget before producing a valid served output.
- Exact hop1 fill is not full-chain budget-safe in this form.
- Do not resubmit unchanged.
