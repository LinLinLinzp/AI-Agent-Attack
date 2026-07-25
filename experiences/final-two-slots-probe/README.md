# Final Two Slots Probe

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

Decision rule:

- If `safe_n` is above about `1112` for both public rows, V49 has a realistic `100+`
  public path.
- If `aggressive_n` is above about `1223` for both rows and max latency is stable,
  V50 is the `110+` attempt.
- If the slow row stays below `1000`, use V48 instead of burning both attempts on
  probe-to-emit.
