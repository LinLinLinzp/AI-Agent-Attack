# AI Agent Attack Workspace

This workspace is organized around two active workflows:

- `submission/current/`: numbered Kaggle submission candidates and handoff notes.
- `experiences/`: local/Kaggle probes, validation notebooks, and experiment records.

Reference material and large assets are kept separate so old notebooks are not mistaken for the active submission.

## Directory Map

```text
submission/current/      Current candidate sources and submission notebook context.
submission/archive/      Saved historical submission states.
experiences/              Probe families, experiment records, and validation guides.
explore/                  SDK analysis and public/private strategy research.
references/notebooks/    Official, LB, and working reference notebooks.
references/88_515/       External 88.515 public LB reference notebook.
references/sdk/          Competition SDK archive and extracted SDK.
models/                  Local model archives.
scratch/                 Temporary experiments.
```

## Current Submission

Current working baseline:

- Public LB `88.965`, from `submission/current/v88_515_plus_gpt_k2_probe/submit.py`.
- Strategy: model-aware GPT K2 / gemma K1 probe built from the external `88.515` reference strategy.
- Latest checked follow-ups: `V38` timed out; `V39` scored `69.454`; `V40` scored `77.625`; `V41` scored `78.135`; `V42` scored `88.245`; `V43` scored `87.175`; `V44` scored `87.390`; `V46` scored `84.170`; `V47` scored `86.400`; `V48` scored `88.305`; `V49` scored `68.895`; `V50` scored `83.880`; `V51` scored `87.505`; `V52` timed out; `V53` scored `65.700`; `V54` scored `60.930`; `V55` scored `61.065`; `V56` scored `88.965`; `V57` and `V58` timed out. Kaggle displayed `Submission Format Error` for V52/V57/V58, but these are treated as runtime-budget failures. Keep `88.965` as the current reproducible baseline.
- Current next direction: V56 tied C exactly, so generation-tail reserve is not the 100-point bottleneck. V57/V58 timed out, rejecting cheap-fill and fixed `1120` static return as budget-safe full-chain strategies. The next step should be a full-chain diagnostic or a new raw-per-candidate mechanism, not more K1 volume tuning.
- Goal for the next round: move toward `100.00` first, then the observed ~`110` public ceiling.

Important repo-state note: `submission/current/submit.py` is intentionally not used for this round. Numbered sources live under `submission/current/vNN_*`; copy one variant at a time into the Kaggle notebook writer cell that creates `/kaggle/working/attack.py`. Future submissions should keep this submit-number prefix convention. The existing `submission/current/getting-started-notebook.ipynb` is legacy context and is not currently synchronized with the candidate sources.

Current experiment matrix:

| Version | Status | Purpose |
| --- | --- | --- |
| `v88_515_plus_gpt_k2_probe` | Public LB `88.965` | Current reproducible GPT K2 / gemma K1 baseline |
| `V38` | Timeout | K1-volume recovery while retaining GPT K2 |
| `V39` | Public LB `69.454` | Aggressive GPT K3/K2 density |
| `V40` | Public LB `77.625` | Multi-message K1 batching |
| `V41` | Public LB `78.135` | GPT harmony/prefill probe with gemma K1 fallback |
| `V42` | Public LB `88.245` | GPT K1/K2 analysis-channel compression |
| `V43` | Public LB `87.175` | Conservative selected-template replay packing |
| `V44` | Public LB `87.390` | Replay-safe K1-only 88.515 reference |
| `V46` | Public LB `84.170` | Aggressive GPT K2 + CD stack |
| `V47` | Public LB `86.400` | Conservative same-candidate EXFIL + CD stack copied from V45 |
| `V48` | Public LB `88.305` | Replay-cost-tax fix from C; fast K1 fill charged by full-hop replay cost |
| `V49` | Public LB `68.895` | Safe probe-to-emit jump; rejected broad unvalidated portfolio |
| `V50` | Public LB `83.880` | Aggressive probe-to-emit jump; below C but not timeout |
| `V51` | Public LB `87.505` | C bank-wide / K2-edge validated calibration; did not promote |
| `V52` | Timeout | Fixed plain `Reply OK.` emit test, 1250 target candidates; Kaggle displayed `Submission Format Error` |
| `V53` | Public LB `65.700` | K1 emit with measured replay ledger; scored like ~730 K1 cells, so ledger was too conservative or selected a slow lane |
| `V54` | Public LB `60.930` | Aggressive K2 exact-probe ledger; raw34 path did not transfer into high public score |
| `V55` | Public LB `61.065` | Conservative K2 exact-probe ledger; nearly same result as V54, confirming the cap was not the main issue |
| `V56` | Public LB `88.965` | C full-hop exact validation with smaller generation tail reserve; tied C exactly |
| `V57` | Timeout | C selector with hop1 exact trace fill and full-hop audits; Kaggle displayed `Submission Format Error` |
| `V58` | Timeout | Fixed model-routed K1 `1120` underfill test; Kaggle displayed `Submission Format Error` |

## Experiment Workflow

- Start with `experiences/README.md` for the experiment index and evidence summary.
- Use `experiences/full-chain-underfill-audit/` before more blind submissions when possible.
- Use `experiences/template_probe_plan.md` to plan low-cost template discovery.
- Use `experiences/local-validation-guide.ipynb` for public-style validation of finalists or a complete `attack.py` portfolio.
- Keep each focused probe and its results in a dedicated `experiences/<experiment>/` directory.
- Before a Kaggle run, syntax-check the selected numbered `submit.py`, then copy it into the notebook cell that writes `/kaggle/working/attack.py`.

## Notes

- `agent.md` is the running project handoff and decision log.
- `COMPETITION_OVERVIEW.md` is the competition-mechanics and scoring reference.
- `NOTEBOOK_INSIGHTS.md` summarizes the strategy lessons from the two high-score notebooks.
- `submission/archive/leaderboard_history.md` is the score and submission-result ledger.
- `submission/archive/best_lb_88_965_results_v48_v58_archive_2026_07_28.md` is the consolidated V48-V58 result archive.
- `references/` is read-only context unless intentionally updating research notes.
- `.venv`, `.uv-cache`, and `.uv-python` stay at the workspace root to avoid breaking the local uv environment.
