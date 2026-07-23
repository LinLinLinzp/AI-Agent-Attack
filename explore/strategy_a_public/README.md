# Strategy A: Historical Public Sprint

This directory is an exploratory public-sprint branch, not the current baseline.

## Current Status

The previous README described a K-adaptive K=4/6/8 strategy. The current `submit.py` in this directory should not be treated as that confirmed design. It is closer to an aggressive K=1 live-validation branch:

- one-message `SECRET_MARKER` exfiltration through `http.post`;
- short `.co` domains;
- live probing during `run()`;
- a hard cap around the returned candidate count;
- broad success detection based on successful tool calls in parts of the flow.

Because the new external `88.515` reference already beats the old K=1 baseline with cleaner replay accounting, this branch should not be copied directly into `submission/current/submit.py`.

## Relationship To The New Baseline

The current mainline should be:

```text
88.515 uniform three-probe K=1 baseline
  -> exact archive/control
  -> one-variable A/B tests toward 100.00
```

This strategy can still contribute ideas after the control is restored:

- tighter prompt wording;
- reduced probe overhead;
- public-only replay cap experiments.

Any useful change should be ported into the `88.515` framework and tested as a single variable.

## Risks

- K=4/6/8 is not confirmed by this directory.
- gemma has not shown reliable high-K behavior.
- broad `successful_tool_calls` validation is less precise than checking trace-level `http.post` with `SECRET_MARKER`.
- aggressive caps may gain score or may push replay over the hosted timeout boundary.

## Usage

Do not submit this branch directly unless intentionally testing it as a separate experiment. The preferred next submission source should be restored from the `88.515` baseline first.
