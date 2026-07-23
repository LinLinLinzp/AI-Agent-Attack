# Timeout - v88_515 Exact Control

Archived after the unchanged local `v88_515_exact_control` resubmission timed
out on 2026-07-22.

- Result: timeout / invalid submission
- Submitted source: `submit.py`
- Lineage: exact-control copy of the external `88.515` reference family
- Main replay knob: `REPLAY_SAFE = 0.99`
- Nominal replay cap: `8910s` of `9000s`, leaving about `90s` margin

Interpretation: the external `88.515` result remains useful evidence that this
K=1 replay-ledger strategy can score high, but this local resubmission shows the
unchanged exact-control source is not replay-stable in the current hosted
environment. The next control should lower replay safe before changing template
logic.
