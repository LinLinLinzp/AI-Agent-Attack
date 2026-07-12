# AI Agent Attack Workspace

This workspace is organized around two active workflows:

- `submission/current/`: the current Kaggle submission package.
- `validation/`: local/Kaggle validation and template mining.

Reference material and large assets are kept separate so old notebooks are not mistaken for the active submission.

## Directory Map

```text
submission/current/      Current submit.py source and submission notebook.
submission/archive/      Saved historical submission states.
validation/              Local validation notebook, probe plans, and results.
references/notebooks/    Official, LB, and working reference notebooks.
references/sdk/          Competition SDK archive and extracted SDK.
models/                  Local model archives.
scratch/                 Temporary experiments.
```

## Current Submission

Use these files when preparing a Kaggle submission:

- `submission/current/submit.py`
- `submission/current/getting-started-notebook.ipynb`

The current attack strategy is a ShadowCat-style live validation-fill loop: it probes the live environment, keeps only candidates that actually fire `http.post(data=SECRET_MARKER)`, and stops before the budget edge.

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
