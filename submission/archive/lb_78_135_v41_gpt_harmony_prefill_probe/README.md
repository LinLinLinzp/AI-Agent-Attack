# LB 78.135: V41 GPT Harmony / Prefill Probe

Public LB reported by user: `78.135`.

Source:

- `submission/current/v41_gpt_harmony_prefill_probe/submit.py`

Key changes from C:

- added GPT-only native-looking harmony and prefill templates;
- included K2 and K3 options in the GPT selector;
- kept gemma on K1 fallback;
- lowered replay safety for higher-K selected lanes.

Interpretation:

The current harmony/prefill implementation did not improve GPT throughput and
scored far below C (`88.965`). The result does not rule out shorter
analysis-channel closure entirely, but it rejects this broad native-prefill plus
high-K template mix.
