"""Helper cell for Kaggle Local Validation Guide.

Usage inside a Kaggle notebook after `env` and `config` are already defined:

    exec(open("/kaggle/working/probe.py").read())
    run_attack_only("/kaggle/working/attack.py", env, config)

This measures AttackAlgorithm.run() only. It does not replay candidates.
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import time
from pathlib import Path
from typing import Any


def load_attack_class(path: str | Path) -> type:
    attack_path = Path(path)
    spec = importlib.util.spec_from_file_location("underfill_attack", attack_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {attack_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, "AttackAlgorithm"):
        raise AttributeError(f"{attack_path} does not define AttackAlgorithm")
    return module.AttackAlgorithm


def candidate_messages(candidate: Any) -> tuple[str, ...]:
    value = getattr(candidate, "user_messages", None)
    if value is None:
        value = getattr(candidate, "messages", None)
    if value is None:
        return ()
    return tuple(str(item) for item in value)


def run_attack_only(path: str | Path, env: Any, config: Any) -> dict[str, Any]:
    klass = load_attack_class(path)
    stream = io.StringIO()
    started = time.monotonic()
    with contextlib.redirect_stderr(stream):
        candidates = klass().run(env, config)
    elapsed = time.monotonic() - started
    first_messages = candidate_messages(candidates[0]) if candidates else ()
    result = {
        "path": str(path),
        "model_name": str(getattr(config, "model_name", "")),
        "returned": len(candidates),
        "elapsed_s": round(elapsed, 3),
        "score_est_k1": round(len(candidates) * 0.09, 3),
        "first_messages": first_messages,
        "stderr": stream.getvalue()[-4000:],
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result
