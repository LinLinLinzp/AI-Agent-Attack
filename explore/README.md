# Explore: Historical Strategy Branches

This directory contains exploratory submission ideas. These files are useful for research, but they are not the current baseline.

Current baseline decision:

- Mainline reference: `references/88_515/ai-agent-security-adaptiveuniformthree-probe-race.ipynb`
- Public LB: `88.515`
- Strategy: K=1 uniform three-probe template race with measured replay-cost packing
- Next target: approach `100.00` by improving K=1 replay density first, then testing GPT K=2 separately

## Current Interpretation

The older explore docs were written during a K=4/K=6/K=8 theory phase. That theory was attractive because one candidate with K posts has:

```text
raw(K) = 16 * K + 2
```

But later evidence changed the priority:

- gemma rarely completes reliable K>1 posts;
- GPT can sometimes complete K=2/K=3, but K3 has already produced a poor leaderboard result in one branch;
- the new `88.515` reference achieved the largest confirmed jump with K=1 plus better replay accounting;
- therefore high K is now a controlled experiment, not the default route.

## Strategy Directories

| Directory | Actual Role Now | Notes |
| --- | --- | --- |
| `strategy_a_public/` | Historical public-sprint idea | Its README previously described K-adaptive high-K behavior, but the current code is closer to K=1 live validation with aggressive caps. Do not promote it without revalidating. |
| `strategy_b_private/` | Historical private-hedge idea | Useful for CD/hedge thinking, but some wording must be corrected because `CONFUSED_DEPUTY` requires the final user message to avoid `send`, `email`, and `upload`. |

## Recommended Use

Do not copy an explore strategy directly into `submission/current/submit.py` as the next submission.

Recommended sequence:

1. Restore `submission/current/submit.py` from the `88.515` baseline.
2. Archive that exact baseline as the new control.
3. Run small A/B tests around template set, exact URL validation, `REPLAY_SAFE`, and `PROBE_REPS`.
4. Only then test high-risk branches such as GPT K=2 / gemma K=1 or a tiny CD hedge.

## Source Of Truth

For active work, prefer:

- `submission/current/NOTES.md`
- `submission/archive/leaderboard_history.md`
- `agent.md`
- `NOTEBOOK_INSIGHTS.md`

Treat older explore projections as hypotheses unless they have a matching public LB result recorded in the leaderboard history.
