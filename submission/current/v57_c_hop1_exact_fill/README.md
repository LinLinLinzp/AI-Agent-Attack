# V57 C Hop1 Exact Fill

Source:

```text
submission/current/v57_c_hop1_exact_fill/submit.py
```

Baseline:

```text
C / V37: 88.965
V48: 88.305
```

Purpose:

- Retest V48's cheap-fill idea, but remove the weak acceptance signal.
- Selected K1 fill uses `max_tool_hops = 1` and exact trace URL/data checks.
- Periodic full-hop audits every `24` fill attempts keep the replay-unit estimate
  conservative.
- K2-selected rows stay full-hop exact, because K2 needs more than one tool call.

Experiment:

- Tests whether C can gain generation throughput without admitting replay misses.
- If this beats C, V48 failed because `successful_tool_calls` was too weak, not
  because hop1 fill is fundamentally bad.

Expected public LB:

```text
88-96 most likely
96-100 if C was generation-underfilled and hop1 exact remains replay-stable
<88 if hop1 exact traces still do not transfer to full-hop replay
```

Interpretation:

- If V57 beats C by several points, keep exact hop1 fill and tune audit cadence.
- If V57 is close but lower, replay cap, not generation validation, is the main wall.
- If V57 drops hard, do not continue cheap fill.

Actual result:

```text
V57: timeout; Kaggle displayed Submission Format Error
```

Interpretation:

- Completed as invalid because it exceeded the full-chain time budget.
- Hop1 exact fill plus full-hop audits is not full-chain budget-safe in this form.
- Do not resubmit unchanged.
