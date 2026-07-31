# V48 / V49 Direction Plan After V46-V47

Baseline:

```text
C / v88_515_plus_gpt_k2_probe = 88.965 public LB
V46 = 84.170 public LB
V47 = 86.400 public LB
```

Outcome after submission:

```text
V48 = 88.305 public LB
V49 = 68.895 public LB
V50 = 83.880 public LB
```

This plan is now historical. V48 stayed close but did not beat C. V49/V50 rejected
broad probe-to-emit as implemented because unvalidated replay success did not hold.
The active follow-up is `submission/current/V51_V52_SUBMISSION_PLAN.md`.

External analysis incorporated:

- Pilkwang Kim, [AI Agent Security Part 4: Past the Framing Plateau](https://pilkwangkim.github.io/posts/AI-Agent-Security-Part-4-Past-the-Framing-Plateau/)
- Pilkwang Kim, [AI Agent Security Part 5: The Raw Wall from the Inside](https://pilkwangkim.github.io/posts/AI-Agent-Security-Part-5-The-Raw-Wall-from-the-Inside-KR/)

## Current Interpretation

V46 and V47 are negative evidence for same-candidate `EXFILTRATION + CONFUSED_DEPUTY`
stacking. The theoretical raw value looked attractive, but the added email tool call
increased candidate length, replay variance, and selector noise enough to lose public
score versus C. CD should not stay in the public-score mainline.

The gap from `88.965` to `100.000` is about `123` K=1-equivalent successful cells, and
the gap to `110.000` is about `233` K=1-equivalent cells. That is too large for ordinary
single-post prompt tweaks, but not necessarily too large for replay-cost-tax fixes if C
is generation-underfilled.

After Part 4/5, bounded K should be treated more cautiously. The scorer pays every
firing post, but packing several posts into one candidate loses the per-candidate `+2`
cell bonus and spends another model generation per post. If fixed candidate overhead is
small, K>1 can be throughput-neutral or slightly worse. Bounded K remains a thing to
audit, not the next mainline.

## V48 Candidate: C Replay-Cost-Tax Fix

Purpose:

Keep C's scored primitive and template family, but stop paying generation-side costs
that do not improve the returned replay set.

Experiment:

- Start from `submission/current/v88_515_plus_gpt_k2_probe/submit.py`.
- Keep CD templates removed.
- Reset `slowest` after the warm-up trial, so a cold model-load sample does not inflate
  the search reserve.
- Preserve C's near-selected mixed probe bank. V43 showed fully selected-only packing
  loses useful volume, so V48 only changes the fill economics after selection.
- Add a gated positive one-token terminal variant (`then reply OK only`) for the
  selected single-post family, because it can reduce the replay wrap-up generation
  itself rather than only speeding generation-time validation.
- Use full `max_tool_hops=8` only for probe calibration and periodic replay-cost audits.
- During selected-template fill, validate at `max_tool_hops=1` because the scored
  `http.post` happens at hop 0; charge each accepted candidate with the measured or
  audited full-hop replay unit so returned candidates still fit the evaluator replay
  budget.
- Use `EnvInteractionResult.successful_tool_calls` as a cheap first-pass fire signal,
  with exact URL trace checks at a fixed cadence to catch parser drift.

Expected public LB:

```text
89-96 most likely
96-100 if C is materially generation-underfilled by full-hop fill and warm-up reserve
<88 if hop-1 acceptance admits replay misses or full-hop replay cost is undercharged
```

Why this helps:

Part 4/5 identifies the durable lever as true replay-cost sizing plus avoiding validation
work that is not scored. C already has harmony collapse and measured replay sizing, but
it still pays full-hop generation during fill and carries the warm-up `slowest` into the
deadline reserve. V48 tests whether that is the missing slack between high 80s and 100.

## V49 / V50 Candidate: Probe-To-Emit Jump

Purpose:

Use the final submission slots for the only remaining large-jump hypothesis: C may be
underfilled because it live-validates every returned candidate during generation. V49
and V50 keep the single-post primitive, spend only a few probes to estimate row-specific
replay cost, then emit a larger portfolio without validating each returned candidate.

Experiment:

- `V49` source: `submission/current/v49_probe_emit_safe/submit.py`.
- `V50` source: `submission/current/v50_probe_emit_aggressive/submit.py`.
- Both probe the current model row with full `max_tool_hops=8` K1 samples.
- Both choose the fastest reliable K1 template from the C/V48 family.
- Both compute a row-specific candidate count from measured latency.
- V49 uses `REPLAY_SAFE = 0.955`, stronger latency multipliers, and `MAX_RETURN = 1320`.
- V50 uses `REPLAY_SAFE = 0.985`, lighter multipliers, and `MAX_RETURN = 1580`.

Expected public LB:

```text
V49: 88-96 if measured unit stays near C; 100-112 if replay unit is <= about 7.7s
V50: 95-118 if probe latency matches replay latency; timeout if replay tail is worse
```

Why this helps:

The public 110 observation is easier to explain by returning about `1223` stable K1
cells than by CD stack or broad K>1. Probe-to-emit is the cleanest way to test whether
our current live-validation strategy is leaving those cells on the table.

Pre-submit experience, now historical:

Run `experiences/final-two-slots-probe/notebook.ipynb` on Kaggle. If both models show
`safe_n >= 1112`, V49 was expected to be a realistic `100+` attempt. If both showed
`aggressive_n >= 1223` without spiky max latency, V50 was the `110+` attempt.

Actual V49/V50 public LB results did not validate this rule.

## Non-Mainline Ideas

- True parallelism inside `AttackAlgorithm.run` is unlikely to help: the evaluator
  replays candidates sequentially, and the provided attack env is a single opaque
  session. Concurrent calls against the same env would be unsafe.
- Snapshot/restore can be useful for generation calibration, but it cannot reduce
  evaluator replay cost.
- Further prompt shortening is a secondary lever. Prior V42/V44 evidence says small
  formatting changes can easily lose more compliance than they save in latency.
- `UNTRUSTED_TO_ACTION + EXFILTRATION` is the only attractive same-post raw stack on
  paper, but the public guardrail taint window currently covers the predicate arming
  window, so this is a source-audit problem rather than a template tweak.
- CD can be kept as a private hedge later, but not in the next public-score variants.

## Historical Result

1. V48 scored `88.305`, close but below C.
2. V49 scored `68.895`, a major regression.
3. V50 scored `83.880`, below C despite not timing out.
4. Keep C (`88.965`) as baseline and move to V51/V52.
