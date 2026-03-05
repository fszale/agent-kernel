# Prompt: Rate of Improvement Analysis

## Purpose
Analyze collected Rate of Improvement data to determine whether an AI deployment is succeeding, classify the curve shape, identify inflection points, and generate an executive summary.

## When to Use
- At 4+ weeks of deployment data (first meaningful analysis)
- At Week 8 (mid-point milestone review)
- At Week 12 (final analysis and thesis validation)
- Any time when trajectory assessment is needed for stakeholder reporting

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{metric_name}}` | The metric being tracked | "Hours/week on invoice reconciliation" |
| `{{baseline}}` | Baseline value (before deployment) | "14 hours/week" |
| `{{target}}` | Target value | "Under 4 hours/week" |
| `{{weekly_data}}` | Weekly metric values | "W1: 14, W2: 12, W3: 9, W4: 7, W5: 6.5, W6: 5.5, W7: 5" |
| `{{context_notes}}` | Relevant events (retraining, workflow changes) | "Staff training completed W2, workflow v2 deployed W5" |

## Prompt

```
You are analyzing Rate of Improvement data for an AI workflow deployment.

Metric: {{metric_name}}
Baseline: {{baseline}}
Target: {{target}}
Weekly data: {{weekly_data}}
Context: {{context_notes}}

## 1. Data Summary
For each week, calculate:
- Absolute value
- Improvement vs. baseline (%)
- Rate of improvement vs. previous week (% change / week)
- Overall improvement from baseline to latest

Present as a table.

## 2. Curve Shape Classification
Classify the trajectory into one of these patterns:

- ✅ S-Curve (Success): Rapid rise → taper → stabilization
- ⚠️ Rise-Decline: Improvement followed by regression
- ❌ Flat: No meaningful improvement from baseline
- 🔍 Unbounded Rise: Continuous improvement without taper (investigate measurement)

Explain WHY the data shows this pattern. Reference the weekly data specifically.

## 3. Inflection Points
Identify significant trajectory changes:
- When did improvement accelerate most sharply?
- When did rate of improvement begin tapering?
- Do inflection points correlate with events in {{context_notes}}?

## 4. Projection
Based on current trajectory:
- Projected value at Week 12 (if not already there)
- Projected value at Week 24
- Is the target achievable at current trajectory?
- Is the current pace sustainable?
- Has the improvement plateau been reached?

## 5. Executive Summary
Write exactly 3 sentences suitable for presentation to a business owner or executive:
1. What happened (plain language, no jargon)
2. What it is worth (dollar or time value if calculable)
3. What to do next

## 6. Thesis Validation
Evaluate the Rate of Improvement thesis:
- Expected pattern: rapid initial improvement → taper → stabilization (S-curve)
- Actual pattern: [describe]
- Thesis verdict: Supported / Partially Supported / Challenged
- Reasoning: [why — connect to specific data points]
```

## Expected Output
- Weekly data table with calculated rates
- Curve classification with reasoning
- Inflection point analysis
- Projections to Week 12, 24
- Executive summary (3 sentences)
- Thesis validation verdict

## Tips
- Feed in as much context as possible — deployment changes, staff events, and workflow modifications all affect the curve
- Compare results across multiple deployments to validate the thesis at portfolio level
- If the curve is "Rise-Decline" or "Flat", flag for root cause analysis before next sprint
