# V55 K2 Conservative 650

Purpose:

- Same raw34 idea as V54, but with a lower full-chain risk profile.
- Select K2 only after exact live probes.
- Cap K2 at `650` candidates and K1 fallback at `1050`.

Expected public LB:

```text
~102 if GPT selects K2 and Gemma falls back to K1
~110 if both rows select K2
~94 if both rows fall back to K1
format error if even this lower fixed emit volume is unsafe
```

Result rule:

- If V55 succeeds and V54 fails/errors, continue with conservative K2 caps.
- If both V54 and V55 fail, K2 probe-to-emit does not transfer safely and we need a dedicated K2 full-chain notebook before more submissions.

Actual result:

```text
V55 public LB: 61.065
```

Interpretation:

- Completed and did not promote.
- Nearly identical to V54, so lowering the K2 cap did not fix the failure.
- Treat the current exact K2 probe-to-emit transfer as rejected until a
  full-chain notebook proves that bulk K2 replay survives.
