# LB 88.965: GPT K2 / Gemma K1 Probe

Public LB reported by user: `88.965`.

Source:

- `submission/current/v88_515_plus_gpt_k2_probe/submit.py`

Key changes from the K1 safe-speed variant:

- GPT can choose K2 `inj_list` / `inj_force` templates using measured raw/second;
- gemma remains on the K1 template pool;
- K2 candidates require both requested URLs to receive successful marker posts;
- K2 path uses `K2_REPLAY_SAFE = 0.985`.

Interpretation:

This is the current best local submitted result. It beats the K1 safe-speed variant by `2.245` points and the external `88.515` reference by `0.450`. Promote it as the current reproducible public baseline, but run a cleaner follow-up before concluding the gain is entirely from K2.

