---
name: confidence-and-experiment
description: Produce calibrated confidence scores for any recommendation or action, and design experiment frameworks to measure the actual causal impact of changes before and after execution.
when-to-use: Use when assigning confidence to any recommendation, action proposal, or prediction. Use when needing to measure whether a change actually worked (causal attribution). Use before executing any action that requires proof of impact.
principles: [Confidence Scoring, Rate of Improvement, First Principles, Governance Hierarchy]
---

# Confidence and Experiment Design Skill

## Purpose

Be calibrated in your confidence and rigorous in your measurement. Overconfidence leads to poor decisions; poorly designed experiments lead to false attributions.

## Agent Instructions

You are a measurement and calibration specialist.

---

## Part 1: Confidence Scoring

### Core Principle

Confidence reflects **data quality and certainty** — NOT importance. A high-stakes recommendation can still have low confidence if the data is sparse.

**If you say 0.8 confidence, you should be right approximately 80% of the time in similar conditions.**

### Calibration Guide

| Score | Data Quality | Historical Evidence | Use For |
|---|---|---|---|
| 0.9–1.0 | Complete, fresh data | Strong, proven pattern | Auto-executing established actions |
| 0.7–0.8 | Good data, minor gaps | Reasonable inference from similar cases | Standard recommendations requiring HITL |
| 0.5–0.6 | Partial data | Some supporting evidence | Flagging for human evaluation |
| 0.3–0.4 | Limited data | Educated guess | Exploratory suggestions only |
| 0.0–0.2 | Very sparse or stale | Speculative | Must be reviewed; never auto-execute |

### Confidence Reducers (apply sequentially, each reduces from current estimate)

| Condition | Reduction |
|---|---|
| Data is >48 hours stale | −0.10 |
| Historical sample <7 days | −0.10 |
| First time proposing this action type | −0.15 |
| Conflicting signals from different sources | −0.10 |
| External factors not captured in data (seasonality, competitive event) | −0.10 |

**Minimum floor:** Never report a confidence below 0.01 (always some information). Never inflate above 0.95 without extraordinary evidence.

### Common Pitfalls

- Overconfidence on small samples (n=3 is not a pattern)
- Anchoring to prior confident predictions rather than recalibrating from new data
- Not reducing confidence when data is stale
- Treating confidence as "how important is this" rather than "how certain am I"

---

## Part 2: Experiment Design

### Core Principle

Design the experiment BEFORE executing the action — not after. Post-hoc rationalization is not measurement.

### Required Fields for Any Experiment

```
HYPOTHESIS:        If we do X, then metric Y will change by Z%
PRIMARY METRIC:    The single metric that determines success
SECONDARY METRICS: Metrics to monitor for side effects
GUARDRAIL METRICS: Metrics that trigger auto-rollback if they deteriorate
SUCCESS CRITERIA:  Primary metric improves by ≥X% (define threshold upfront)
ROLLBACK TRIGGER:  If guardrail metric declines >Y% for N consecutive days → rollback
DURATION:          Minimum observation period before declaring result
SAMPLE SIZE:       Number of items, days, or data points required
```

### Methodology Selection

```
Can you create a control group?
├─ YES → Holdout test (gold standard for causal attribution)
└─ NO → Is this a continuous intervention (ongoing change)?
         ├─ YES → Time-series causal analysis
         └─ NO → Before/after comparison
                 └─ Do you have 14+ days of pre-intervention baseline?
                     ├─ YES → Paired before/after comparison
                     └─ NO → Descriptive only (cannot claim causality)
```

### Minimum Duration by Metric Type

| Metric Type | Min Duration | Reason |
|---|---|---|
| Fast-feedback metrics (opens, clicks) | 7 days | Low variance, fast signal |
| Standard business KPIs (conversion, cost per unit) | 14 days | Medium variance, attribution lag |
| Quality metrics (error rate, accuracy) | 14–21 days | Medium-high variance |
| Revenue metrics | 21 days | High variance, day-of-week effects |
| Lagging outcome metrics (retention, returns) | 30+ days | Significant processing delay |

### Common Pitfalls

- Starting measurement immediately (many systems have 24–72 hour data lag)
- Running experiments during atypical periods (holidays, sale events, system launches)
- Concluding early on noisy metrics
- Not defining the rollback trigger before starting
- Running overlapping experiments on the same metric/scope

## Output Format

Experiment design document:
1. Hypothesis (one sentence, falsifiable)
2. Methodology selection (from decision tree above, with rationale)
3. Primary/secondary/guardrail metrics
4. Success criteria and rollback trigger (specific values, not "if things go wrong")
5. Duration and sample size justification
6. Confidence score with reducers applied
7. Measurement plan (how data will be collected + who reviews at what cadence)
