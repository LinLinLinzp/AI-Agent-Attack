# LB 86.400: V47 C + Conservative K1/CD Stack

Public LB reported by user: `86.400`.

Source:

- `submission/current/v47_c_cd_stack_conservative/submit.py`

Key changes from C:

- kept C's K1 templates;
- kept C's GPT K2 templates;
- added only K1+CD stack templates;
- required exact `http.post` plus exact `email.send` for stack acceptance;
- used no positive stack bias, `CD_STACK_SCORE_BIAS = 1.00`;
- used lower stack replay cap `CD_STACK_REPLAY_SAFE = 0.975`.

Interpretation:

This version scored `2.565` below C (`88.965`). Even the conservative
same-candidate `EXFILTRATION + CONFUSED_DEPUTY` stack is currently too slow or
too unstable to promote. Keep C as the baseline and move the next work toward
generation/replay throughput rather than adding CD stack templates.
