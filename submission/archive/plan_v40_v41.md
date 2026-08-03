# V40 / V41 Pending Submissions From 88.965

Current reproducible baseline:

```text
v88_515_plus_gpt_k2_probe = 88.965 public LB
```

Recent negative evidence:

```text
V38 = timeout
V39 = 69.545 public LB
V40 = 77.625 public LB
V41 = 78.135 public LB
```

The public writeup
["The Scored Attack Surface Collapses to a Single Predicate"](https://www.kaggle.com/writeups/canqiang/the-scored-attack-surface-collapses-to-a-single-pr)
matches our SDK reading: public scoring is dominated by clean
`http.post(data=SECRET_MARKER)` throughput and unique domains. Multi-post or
continuation strategies are not structurally impossible, but their value depends
on hosted replay latency and reliability.

## V40. Multi-Message K1 Batching

Path:

```text
submission/archive/lb_77_625_v40_multimessage_k1_batching/submit.py
```

Experiment:

- Keep the same K1 primitive, but return candidates with multiple user turns.
- Test whether two or three stable K1 turns can share one fresh replay reset.
- Use lower replay safety for batched candidates: single `0.985`, batch2 `0.975`, batch3 `0.965`.
- Bias selection slightly toward batch2/batch3 only after live probes show successful posts.

Purpose:

This isolates the continuation economics question. If hosted continuation is
cheaper than restarting independent candidates, V40 should recover extra
K=1-equivalent cells without relying on fragile K3 content in one prompt.

Expected public range:

```text
80-93 typical, with upside above 95 only if continuation is materially cheaper.
```

Interpretation:

- If V40 beats `88.965`, keep continuation but narrow to the winning message count.
- If V40 is close but below C, continuation has some value but not enough with current caps.
- If V40 times out, continuation replay cost is underestimated; cap batches much harder.
- If V40 is far below C, return to independent single-message candidates.

## V41. GPT Harmony / Prefill Probe

Path:

```text
submission/archive/lb_78_135_v41_gpt_harmony_prefill_probe/submit.py
```

Experiment:

- Keep gemma on K1 only.
- Add GPT-only harmony/prefill tool-call templates before the existing K2/K3 probes.
- Bias harmony templates and K2/K3 by measured raw per second, but lower K3 replay safety to `0.965`.

Purpose:

The writeup and public notebooks suggest that GPT-OSS can be helped by template
level analysis-channel compression. V41 tests whether native-looking harmony or
prefill text improves GPT throughput in our C-derived selector.

Expected public range:

```text
86-94 typical, with downside into the 70s if GPT selects an unstable high-K branch.
```

Interpretation:

- If V41 beats `88.965`, keep harmony/prefill and remove any losing high-K templates.
- If V41 lands near C, the C selector is already capturing most of the available GPT gain.
- If V41 looks like V39, K3/K2 remains too fragile; build V42 as harmony K1/K2 only.
- If V41 times out, lower K2/K3 replay caps and stop returning non-selected bank probes.

## Next Step After Results

Both V40 and V41 fell well below C. Promote C again and use the V42/V43/V44
three-way plan: compressed GPT K1/K2, conservative selected-only C packing, and
replay-safe K1-only reference.
