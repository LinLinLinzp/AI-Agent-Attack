# AI Agent Attack Workspace

This workspace is organized around two active workflows:

- `submission/current/`: the current Kaggle submission candidates and handoff notes.
- `validation/`: local/Kaggle validation and template mining.

Reference material and large assets are kept separate so old notebooks are not mistaken for the active submission.

## Directory Map

```text
submission/current/      Current candidate sources and submission notebook context.
submission/archive/      Saved historical submission states.
validation/              Local validation notebook, probe plans, and results.
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
- Goal for the next round: use the two remaining submissions to move toward `100.00` first, then the observed ~`110` public ceiling.

Important repo-state note: `submission/current/submit.py` is intentionally not used for this round. The next run compares `V38` and `V39`, with sources under `submission/current/v38_*` and `submission/current/v39_*`; see `submission/current/TWO_REMAINING_SUBMISSION_PLAN.md`. Copy one variant at a time into the Kaggle notebook writer cell that creates `/kaggle/working/attack.py`. Future submissions should keep this submit-number prefix convention. The existing `submission/current/getting-started-notebook.ipynb` is legacy context and is not currently synchronized with the candidate sources.

## Validation Workflow

Use `validation/fast-template-probe.ipynb` for low-cost template discovery on Kaggle. It uses
one-hop broad screening, successive halving, two-hop finalist checks, and fresh-environment replay.

Use `validation/local-validation-guide.ipynb` only for full public-style validation of a small
number of finalists or a complete `attack.py` candidate portfolio.

Use `validation/template_probe_plan.md` to guide batch template testing. Probe outputs should go under `validation/results/` as CSV or JSON files.

## Notes

- `agent.md` is the running project handoff and decision log.
- `COMPETITION_OVERVIEW.md` is the competition-mechanics and scoring reference.
- `NOTEBOOK_INSIGHTS.md` summarizes the strategy lessons from the two high-score notebooks.
- `references/` is read-only context unless intentionally updating research notes.
- `.venv`, `.uv-cache`, and `.uv-python` stay at the workspace root to avoid breaking the local uv environment.
