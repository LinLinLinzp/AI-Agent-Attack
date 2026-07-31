# Current Results Archive - Best LB 88.965 - 2026-07-28

This file consolidates the recent public submissions around the `88.965`
baseline. Exact submitted sources are archived in the directories listed below.

## Status Convention

Kaggle displayed `Submission Format Error` for V52, V57, and V58. Based on the
competition behavior and the user's observation, these are treated as timeouts:
the run exceeded the full-chain budget and did not produce a valid served
submission in time.

## Current Baseline

| Label | Source | Public LB | Archive | Decision |
| --- | --- | ---: | --- | --- |
| C / V37 | `submission/current/v88_515_plus_gpt_k2_probe/submit.py` | `88.965` | `submission/archive/lb_88_965_v88_515_plus_gpt_k2_probe/` | Current reproducible baseline |
| V56 | `submission/current/v56_c_exact_tail_release/submit.py` | `88.965` | `submission/archive/lb_88_965_v56_c_exact_tail_release/` | Tied C; confirms baseline reproducibility but no gain |

## Recent Submission Results

| Version | Public Result | Archive | Main Test | Interpretation |
| --- | ---: | --- | --- | --- |
| V48 | `88.305` | `lb_88_305_v48_replay_cost_tax_fix/` | Replay-cost-tax fix from C | Close to C, but fast-fill shortcut still loses score |
| V49 | `68.895` | `lb_68_895_v49_probe_emit_safe/` | Safe probe-to-emit portfolio | Broad unvalidated emit does not transfer |
| V50 | `83.880` | `lb_83_880_v50_probe_emit_aggressive/` | Aggressive probe-to-emit portfolio | More volume helps but remains below C |
| V51 | `87.505` | `lb_87_505_v51_c_bank_wide_k2_edge/` | Wider C bank retention and stronger K2 bias | Below C; do not continue unchanged |
| V52 | `timeout` | `timeout_v52_plain_reply_emit_1250_2026_07_27/` | Fixed `1250` raw18 K1 emit | Fixed count exceeded full-chain budget |
| V53 | `65.700` | `lb_65_700_v53_k1_emit_ledger_1120/` | K1 emit ledger targeting high volume | Underfilled; about `730` K1-equivalent cells |
| V54 | `60.930` | `lb_60_930_v54_k2_probe_ledger_800/` | Aggressive raw34/K2 probe ledger | K2 raw-density path did not transfer |
| V55 | `61.065` | `lb_61_065_v55_k2_conservative_650/` | Conservative raw34/K2 probe ledger | Same failure as V54; cap was not the main issue |
| V56 | `88.965` | `lb_88_965_v56_c_exact_tail_release/` | C exact validation with smaller tail reserve | Tied C; tail reserve is not bottleneck |
| V57 | `timeout` | `timeout_v57_c_hop1_exact_fill_2026_07_28/` | Hop1 exact fill with full-hop audits | Cheap fill remains budget-unsafe |
| V58 | `timeout` | `timeout_v58_static_fast_route_1120_2026_07_28/` | Fixed `1120` model-routed K1 | Fixed large K1 return remains budget-unsafe |

## Consolidated Reading

- The current hard baseline is still `88.965`.
- V53/V54/V55 completed much faster than the older 12h+ scoring runs, which is
  evidence for too little returned/effective replay work rather than timeout.
- V52/V57/V58 are timeout-class failures. They test the opposite boundary:
  fixed or shortcut-filled volume can exceed the full-chain budget even when the
  theoretical score is above `100`.
- V56 tying C means the previous tail-generation reserve was not the missing
  score source.
- The path to `100+` is unlikely to be plain K1 parameter tuning. The next
  useful work should either produce a full-chain diagnostic for replay budget
  accounting or find a new raw-per-candidate mechanism that transfers in public
  scoring.

## Do Not Resubmit Unchanged

- `v52_plain_reply_emit_1250`
- `v53_k1_emit_ledger_1120`
- `v54_k2_probe_ledger_800`
- `v55_k2_conservative_650`
- `v57_c_hop1_exact_fill`
- `v58_static_fast_route_1120`

Future numbered variants should start at `V59`.
