# Prompt: Team Metrics Review

## Purpose
Build or audit a team metrics system using the Amazon-style approach: separate vanity metrics from actionable metrics, apply the 80/20 filter, and establish a weekly operating cadence.

## When to Use
- When establishing a metrics culture on a new team
- During quarterly metrics audits
- When team reporting feels disconnected from decisions

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{team_context}}` | Team type and function | "Product engineering team, 8 engineers, B2B SaaS" |
| `{{current_metrics}}` | Metrics currently tracked (if any) | "We track: monthly active users, lines of code, story points, NPS" |
| `{{objectives}}` | Team objectives for this period | "Ship 2 major features Q1, reduce bug escape rate by 30%" |

## Prompt

```
You are a metrics system designer applying the Amazon-style operational metrics approach.

Team context: {{team_context}}
Current metrics: {{current_metrics}}
Objectives: {{objectives}}

## 1. Vanity vs. Actionable Audit

Review all current metrics and classify each:

| Metric | Type | Reason |
|---|---|---|
| [metric name] | Vanity / Actionable / Lagging Indicator | [why] |

**Vanity metric:** Makes the team look good but doesn't drive decisions.
**Actionable metric:** Directly informs a specific decision or behavior change.
**Lagging indicator:** Useful for validation, but can't be acted on directly.

## 2. Design the Metrics System

For your team's objectives, design a complete metrics system:

### Leading Indicators (predict future outcomes)
- [Metric]: [Definition] | [Current value] | [Target] | [Review cadence]

### Lagging Indicators (confirm past outcomes)
- [Metric]: [Definition] | [Baseline] | [Target] | [Review cadence]

### Guardrail Metrics (alert if deteriorating)
- [Metric]: [Definition] | [Threshold] | [Alert if ...]

## 3. Pareto Filter

Which 20% of all metrics carry 80% of the decision-making value for this team?
These become the "vital few" — the ones reviewed every week.

List the vital few metrics (3–5 max) with rationale.

## 4. Weekly Metrics Review Cadence

Design the weekly review ritual:
- **Meeting format**: [duration, attendees, frequency]
- **Standard agenda**: [what gets reviewed, in what order]
- **Decision protocol**: [what triggers an action vs. noting and moving on]
- **Escalation path**: [what pattern triggers leadership review]

## 5. Metrics Health Assessment

For each vital metric, score data quality:
- Collection: Is this being measured consistently? (Y/N)
- Reliability: Is the measurement method trustworthy? (Y/N)
- Timeliness: Is data available when needed? (Y/N)
- Action-linked: Does the team know what to do when this metric moves? (Y/N)
```

## Expected Output
- Vanity/actionable/lagging classification of all current metrics
- Complete redesigned metrics system (leading + lagging + guardrail)
- Vital few metrics (Pareto-filtered)
- Weekly review cadence design
- Data quality health scores
