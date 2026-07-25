# LB 84.170: V46 GPT K2 + CD Stack Aggressive

Public LB reported by user: `84.170`.

Source:

- `submission/current/v46_gpt_k2_cd_stack_aggressive/submit.py`

Key changes from C:

- added K1+CD stack templates;
- added GPT-only K2+CD stack templates;
- used positive CD-stack selection bias `CD_STACK_SCORE_BIAS = 1.08`;
- used `CD_STACK_REPLAY_SAFE = 0.982`.

Interpretation:

This version scored `4.795` below C (`88.965`). The aggressive same-candidate
`EXFILTRATION + CONFUSED_DEPUTY` stack did not pay off. The likely causes are
extra tool-generation latency, lower replay reproducibility, and selector noise
from the larger template bank. Do not resubmit unchanged.
