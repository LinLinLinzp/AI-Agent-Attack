# Final Two Slots Probe

Status:

Historical. V49 scored `68.895` and V50 scored `83.880`, so the broad
probe-to-emit approach this notebook was designed for did not hold up on public
LB. Keep this notebook as a replay-sizing pattern, not as the active submission
decision rule.

Purpose:

Before spending the last two public submissions, measure whether the probe-to-emit
idea can safely return enough K1 candidates to break `100` or `110`.

Run on Kaggle:

1. Upload this directory.
2. Attach the competition dataset and the same GGUF model datasets used by the other
   experience notebooks.
3. Enable GPU.
4. Run `notebook.ipynb`.
5. Send back the printed summary plus `final_two_slots_probe_results.json`.

Original decision rule, now historical:

- If `safe_n` was above about `1112` for both public rows, V49 was expected to
  have a realistic `100+` public path.
- If `aggressive_n` is above about `1223` for both rows and max latency is stable,
  V50 was the `110+` attempt.
- If the slow row stayed below `1000`, the old rule would have used V48 instead
  of burning both attempts on probe-to-emit.

After public LB results, do not use this rule for active submission selection.
