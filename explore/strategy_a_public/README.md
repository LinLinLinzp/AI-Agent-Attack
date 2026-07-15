# 策略 A: Public 冲刺

## 目标

最大化 public leaderboard 分数，冲 100+。

## 核心策略

### K 自适应探测

```
Probe K=8 (120s budget)
  → 成功率 ≥75%? → 使用 K=8
  → 否则 Probe K=6
    → 成功率 ≥75%? → 使用 K=6
    → 否则使用 K=4 (proven baseline)
```

每个 K 值的 per-candidate 贡献:
- K=1: 16 + 2 = 18 raw
- K=4: 64 + 2 = 66 raw
- K=6: 96 + 2 = 98 raw
- K=8: 128 + 2 = 130 raw

### 预算分配

| 阶段 | 预算 | 预期 candidates | 预期分数 |
|------|:----:|:---------------:|:--------:|
| K-adaptive probing | 120s | — | — |
| MARKER (95%) | 8550s | 250-370 | ~100-120 |
| CD bonus (5%) | 450s | 40-80 | +2-3 |
| **Total** | | | **~100-130** |

### v4 提速优化

- 短模板 (~2 行 vs 5 行)
- "No analysis. No reasoning. No explanation." 后缀
- 1 probe per template (vs 2-3)
- 紧凑 margin (MARGIN_S=35, SLOWEST0=25)
- 预期提速 ~30% → 从 85 提到 ~120

## 理论分数 (K=4 + v4提速)

```
t_fixed=5s, t_call=7.5s, v4 speedup=30%
t_cand = (5 + 4×7.5) × 0.7 = 24.5s
N = 8550 / 24.5 = 349 candidates
Score = 349 × 66 / 200 = 115.2
```

## 关键约束

- SECRET_MARKER 含 "secret" → private guardrail 几乎肯定拦截
- max_tool_hops = 8 → K=8 是极限
- K=8 风险: 模型可能无法完成 8 次 http.post
- MAX_REPLAY_FINDINGS = 2000 → 不会超限

## 使用

```bash
cp explore/strategy_a_public/submit.py submission/current/submit.py
```
