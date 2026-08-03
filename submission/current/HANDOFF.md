# AI Agent Security submission handoff

Snapshot date: 2026-08-01

## Final state

- Best confirmed public score: **92.160**, V62.
- Stable fallback: V56/V37 family at **88.965**.
- Target: `>100`; gap from V62 is `7.840`, or roughly `88` additional K1-equivalent successful cells at `0.09` points per cell.
- V64 through V70 all ended as timeout-class `Submission Format Error` runs. V68–V70 are recorded from the user's final observation that all newly submitted variants timed out.
- `submission/current/submit.py` is an exact copy of the submitted V62 source.
- V62 SHA-256: `c19c6e088488c661ef425824c4d30d1619448a11dd410f3fa3ee955ae713252d`.

## Result table

| Version | Public result | Core change | Conclusion |
| --- | ---: | --- | --- |
| V31 / baseline | 84.735 | Earlier adaptive baseline | Superseded. |
| V36 | 86.720 | K1 safe-speed with stricter pruning | Validation/pruning lost useful volume. |
| V37 / C | 88.965 | GPT K2 probe, Gemma K1 | First strong model-aware baseline, but later generic K2 work did not transfer. |
| V38 | timeout | Restore K1 volume around C | Replay/cap mix unsafe. |
| V39 | 69.545 | Aggressive GPT K3/K2 | High-K density failed badly. |
| V40 | 77.625 | Multi-message K1 batching | Continuation batching did not pay. |
| V41 | 78.135 | GPT harmony/prefill | Native-looking control tokens did not improve hosted score. |
| V42 | 88.245 | GPT K1/K2 analysis compression | Close, but compressed prompts did not beat C. |
| V43 | 87.175 | Selected-lane-only packing | Discarded useful validated bank candidates. |
| V44 | 87.390 | Conservative K1-only | Stable but not enough volume. |
| V45 | 87.840 observed | Submission associated with the V45 slot | Historical source mapping is uncertain; do not use as a control. |
| V46 | 84.170 | Aggressive K2 + confused-deputy stacking | Extra raw score did not repay latency. |
| V47 | 86.400 | Conservative K1 + confused-deputy stacking | Same negative result with lower risk. |
| V48 | 88.305 | Replay-cost tax / hop1 shortcut | Close but below the exact full-hop family. |
| V49 | 68.895 | Safe probe-to-emit | Unvalidated bulk prompts lost replay success. |
| V50 | 83.880 | Aggressive probe-to-emit | More volume recovered some score but stayed below baseline. |
| V51 | 87.505 | Wider bank, stronger K2 bias | Wider retention/K2 bias did not help. |
| V52 | timeout | Fixed 1250 K1 emit | Fixed large return count is unsafe. |
| V53 | 65.700 | Dynamic K1 emit ledger | Live-probe latency overestimated bulk cost and under-returned. |
| V54 | 60.930 | K2 ledger, cap 800 | Raw34 K2 did not transfer. |
| V55 | 61.065 | K2 ledger, cap 650 | Lowering K2 count did not solve transfer. |
| V56 | 88.965 | Exact tail-reserve release | Tied C; generation reserve was not the bottleneck. |
| V57 | timeout | Hop1 exact fill | Full-chain budget unsafe. |
| V58 | timeout | Static 1120 K1 | Even 1120 fixed K1 was unsafe. |
| V59 | 87.920 | Two-stage exact race | Focusing probes on early leaders underperformed. |
| V60 | timeout | Exact baseline plus bounded unvalidated tail | Tail crossed the runtime boundary. |
| V61 | 80.505 | Short GPT K2 prompts | Short output alone did not produce reliable K2 throughput. |
| **V62** | **92.160** | K1-only, exact full-hop validation, top-three leader race, replay-safe `0.99` | **Golden control and best result.** |
| V63 | 88.020 | Hop1 fill plus audits, replay-safe `0.975` | Cheap validation reduced effective success/volume. |
| V64 | timeout | V62 with top-three race reduced to two | Tiny change timed out; V62 has little hosted margin. |
| V65 | timeout | Short K1 microtemplates | Prompt shortening did not improve full-chain safety. |
| V66 | timeout | Strict GPT K2 selection, K1 fallback | Local exact gates did not guarantee hosted replay safety. |
| V67 | timeout | GPT/Gemma-specific K1 pools | Model-specific prompting remains unvalidated; Gemma chat-template claim is not proven. |
| V68 | timeout | GPT-only strict K3 relay, Gemma K1 | Local 3/3 behavior did not transfer safely. |
| V69 | timeout | V68 with larger K3 replay allocation | Scaling K3 worsened budget risk. |
| V70 | timeout | GPT K3→K2→K1 cascade, Gemma K1 | Reject this relay cascade as the current mainline. |

The complete older leaderboard narrative remains in
`submission/archive/leaderboard_history.md`.

## Why V62 won

V62 did not reduce validation strength. It retained full-hop exact trace checks
and gained by simplifying selection and allocation:

1. It removed GPT K2 from the active race, eliminating a slower and less stable lane.
2. It used a one-probe screening pass, then spent the remaining probes on the top three K1 leaders.
3. It selected by measured raw score per time/effective replay cost.
4. It retained useful validated bank candidates and filled with the winning exact template.
5. It kept `K1_REPLAY_SAFE = 0.99`, converting most of the measured replay budget into scored candidates.

The improvement is therefore best understood as cleaner K1 template confidence
and replay-budget utilization. It is not evidence that K2/K3 or chat-template
tokens helped.

## What the timeout cluster proves

V64 changed only the leader count from three to two yet timed out. That is the
strongest warning in the latest batch: V62's observed success is near the hosted
runtime boundary and has limited repeatability margin. A local latency gain or a
shorter prompt is insufficient evidence; the relevant quantity is complete
hosted replay time across every returned candidate.

V65–V70 add a second lesson. Model-specific wording, strict local K2/K3 gates,
and relay prompts can all look good locally while failing the hosted full-chain
budget. Gemma should not be assumed to need or not need chat-template control
tokens until a controlled hosted A/B run demonstrates it.

## Paths to keep when moving environments

- Golden source: `submission/current/submit.py`
- This handoff: `submission/current/HANDOFF.md`
- V62 scored source: `submission/archive/lb_92_160_v62_singlepost_confidence_clean/`
- V59–V70 sources: direct `lb_*_vNN_*` or `timeout_vNN_*` directories under `submission/archive/`
- Full leaderboard history: `submission/archive/leaderboard_history.md`
- K2/K3 prompt evidence: `experiences/k2-prompt-probe/`
- Throughput and replay artifacts: `experiences/frontier-throughput-audit/`
- Local validation guide: `experiences/local-validation-guide.ipynb`

## Recommended continuation

1. Freeze V62. Do not edit or overwrite the golden `submit.py`.
2. First reproduce V62 in the new environment with telemetry for selected template, returned count, replay-cost estimate, model family, and generation duration.
3. Build a full-chain local simulator calibrated against V62's hosted 92.160 run and the V64 timeout. Optimize against the boundary interval, not raw local latency.
4. Pursue `>100` only through a bounded experiment that changes one factor at a time. The highest-value unknown is not another prompt phrase; it is which model/row subset creates V62's extra score and timeout variance.
5. Do not resume generic K2/K3, hop1 fill, static large returns, continuation batching, confused-deputy stacking, or chat-template tokens without new hosted evidence.

The next useful experiment should be diagnostic-first: preserve V62's returned
portfolio and validation path, then add telemetry or a very small model-specific
probe that cannot materially change the replay cap. A new scoring variant should
only follow after that diagnostic explains the V62/V64 split.
