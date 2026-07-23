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
- Latest checked follow-ups: `V38` timed out; `V39` scored `69.454`. Keep `88.965` as the current reproducible baseline.
- Current pending follow-ups: `V40` and `V41`, documented in `submission/current/V40_V41_SUBMISSION_PLAN.md`.
- Goal for the next round: move toward `100.00` first, then the observed ~`110` public ceiling.

Important repo-state note: `submission/current/submit.py` is intentionally not used for this round. The current numbered sources live under `submission/current/v40_*` and `submission/current/v41_*`; copy one variant at a time into the Kaggle notebook writer cell that creates `/kaggle/working/attack.py`. Future submissions should keep this submit-number prefix convention. The existing `submission/current/getting-started-notebook.ipynb` is legacy context and is not currently synchronized with the candidate sources.

Current experiment matrix:

| Version | Status | Purpose |
| --- | --- | --- |
| `v88_515_plus_gpt_k2_probe` | Public LB `88.965` | Current reproducible GPT K2 / gemma K1 baseline |
| `V38` | Timeout | K1-volume recovery while retaining GPT K2 |
| `V39` | Public LB `69.454` | Aggressive GPT K3/K2 density |
| `V40` | Pending | Multi-message K1 batching |
| `V41` | Pending | GPT harmony/prefill probe with gemma K1 fallback |

## Experiment Workflow

- Start with `experiences/README.md` for the experiment index and evidence summary.
- Use `experiences/template_probe_plan.md` to plan low-cost template discovery.
- Use `experiences/local-validation-guide.ipynb` for public-style validation of finalists or a complete `attack.py` portfolio.
- Keep each focused probe and its results in a dedicated `experiences/<experiment>/` directory.
- Before a Kaggle run, syntax-check the selected numbered `submit.py`, then copy it into the notebook cell that writes `/kaggle/working/attack.py`.

## Notes

- `agent.md` is the running project handoff and decision log.
- `COMPETITION_OVERVIEW.md` is the competition-mechanics and scoring reference.
- `NOTEBOOK_INSIGHTS.md` summarizes the strategy lessons from the two high-score notebooks.
- `submission/archive/leaderboard_history.md` is the score and submission-result ledger.
- `references/` is read-only context unless intentionally updating research notes.
- `.venv`, `.uv-cache`, and `.uv-python` stay at the workspace root to avoid breaking the local uv environment.
