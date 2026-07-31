# Full-Chain Underfill Audit

Purpose:

Check the part public LB cannot show directly:

- how many candidates `AttackAlgorithm.run()` actually returns;
- how long generation takes;
- which template/lane was selected from stderr;
- whether the returned count explains the public score.

Why:

V53/V54/V55 scored much faster than previous 12h+ submissions and landed at
`65.700`, `60.930`, and `61.065`. That strongly suggests underfilled returned
or effective replay volume. Before more blind submissions, run this audit in a
Kaggle notebook using the same environment as the competition.

Minimal notebook procedure:

1. Open the existing Kaggle `Local Validation Guide` notebook.
2. Use its environment/model setup cells.
3. Upload or paste `probe.py` into `/kaggle/working/probe.py`.
4. Set `ATTACK_PATH` to one candidate source at a time:

```python
ATTACK_PATH = "/kaggle/working/attack.py"
```

5. Copy one local source into `/kaggle/working/attack.py`, for example:

```text
submission/current/v56_c_exact_tail_release/submit.py
submission/current/v57_c_hop1_exact_fill/submit.py
submission/current/v58_static_fast_route_1120/submit.py
```

6. Run only the `AttackAlgorithm.run(...)` stage first:

```python
exec(open("/kaggle/working/probe.py").read())
run_attack_only("/kaggle/working/attack.py", env, config)
```

7. Preserve stderr output from the candidate source. The useful fields are:

```text
selected=...
k=...
fill_unit=...
returned=...
replay_cost=...
fill=...
fast=...
audit=...
fail=...
```

Decision rules:

- If a candidate returns below about `990`, it cannot beat C unless it has stable
  K2 raw34 cells.
- If V58 returns exactly `1120` but local replay succeeds and public still fails,
  isolated replay is missing an official full-chain constraint.
- If V57 returns much more than C while keeping audit failures at `0`, exact hop1
  fill is worth another public submission.

Record outputs in this directory as `logs_YYYY_MM_DD.txt`.
