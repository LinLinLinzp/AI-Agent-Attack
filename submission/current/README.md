# Current submission

This directory is intentionally minimal after the 2026-08-01 archive cleanup.

- `submit.py`: currently tracks the V101 K2 double-post engine (repository-internal
  working copy; the golden control for the best confirmed public result is V62,
  archived under `submission/archive/`).
- `HANDOFF.md`: results, conclusions, archive map, and continuation plan (snapshot
  through V70 at 2026-08-01; later V77–V170 variants live in `vNN_*/` subdirectories).

Completed versions are stored directly under `submission/archive/`, with the
public score or `timeout` in each directory name. A full V77–V170 experiment
progression is preserved in the `vNN_*/` directories here.

Do not modify `submit.py` in place when starting a new experiment. Copy it to a
new numbered directory in the next environment and retain this file as the
golden control.
