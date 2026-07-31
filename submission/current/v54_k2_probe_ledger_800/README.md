# V54 K2 Probe Ledger 800

Purpose:

- Test the strongest gateway signal: `k2_inj_list` can replay as two exact EXFIL posts, worth `34 raw = 0.17` per candidate.
- Probe K2 in the live attack row and only select it if all probes are exact.
- Fall back to K1 if K2 is not stable for the current model row.
- Use measured replay-unit sizing plus hard caps instead of a fixed `1250` count.

Expected public LB:

```text
100-120 if GPT selects K2 and Gemma falls back to K1
>120 if both rows select stable K2
<90 if unvalidated K2/K1 emit does not transfer from probes to replay
```

Result rule:

- If V54 beats C, continue K2-ledger variants with count/cap tuning.
- If V54 errors or drops badly, K2 static emit is not ready; return to C-style full live validation.

Actual result:

```text
V54 public LB: 60.930
```

Interpretation:

- Completed and did not promote.
- Raw34 K2 did not transfer into a high public score in this full-chain
  submission.
- The short scoring time points to low returned/effective replay volume rather
  than timeout pressure.
