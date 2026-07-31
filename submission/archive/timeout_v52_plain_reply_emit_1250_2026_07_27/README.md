# V52 Plain Reply Emit 1250

Kaggle displayed:

```text
Submission Format Error
```

Result:

- Treated as timeout / runtime-budget failure for this archive.
- Did not produce a public score.
- This was raw18 K1 emit, not raw34.
- The failed public run rejects fixed `1250` count as a full-chain submission strategy, even though gateway replay validation suggested the underlying template can score above `100` in isolated replay.

Decision:

- Do not resubmit unchanged.
- Any follow-up must restore replay-margin sizing and hard caps.
