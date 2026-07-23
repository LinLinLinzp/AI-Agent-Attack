# LB 86.720: K1 Safe-Speed Variant

Public LB reported by user: `86.720`.

Source:

- `submission/current/v88_515_plus_k1_safe_speed/submit.py`

Key changes from the external `88.515` reference:

- added `inj_data_first`;
- required exact destination URL validation;
- used successful-candidate latency for replay packing;
- filtered slower fired probe-bank candidates;
- kept `REPLAY_SAFE = 0.99`.

Interpretation:

This version finished, unlike the exact `88.515` control resubmission, but it scored below the external `88.515` reference. The likely lesson is that stricter validation and bank pruning reduced returned candidate volume more than the faster template recovered. Do not promote as the mainline.

