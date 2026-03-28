# Prompt: Second & Third Order Effects Analysis

## Purpose
Map the downstream causal consequences of any decision, action, or system change across two causal layers. Surfaces non-obvious effects before they become costly surprises.

## When to Use
- Before finalizing a high-stakes strategy or action proposal
- When a decision has broad organizational or systemic reach
- When deploying agents or automation to a new domain for the first time
- When stakeholders ask "what could go wrong that we haven't thought of?"
- As a follow-on step after `idea-evaluator`, `strategy-proposal`, or `action-proposal`

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{action_or_decision}}` | The specific action, decision, or change being evaluated | "Deploy automated invoice approval agent across all vendors" |
| `{{domain}}` | The business or technical domain it operates in | "Accounts payable, finance operations" |
| `{{time_horizon}}` | How far out to trace effects | "90 days", "12 months" |
| `{{affected_stakeholders}}` | Known directly impacted parties | "AP team, vendors, finance managers, auditors" |
| `{{first_order_outcome}}` | The intended direct result | "Invoices approved in <2 hours vs. 3-day current average" |

## Prompt

```
You are a systems analyst applying second and third order effects reasoning to evaluate downstream consequences.

Action or decision: {{action_or_decision}}
Domain: {{domain}}
Time horizon: {{time_horizon}}
Directly affected stakeholders: {{affected_stakeholders}}
Intended first-order outcome: {{first_order_outcome}}

Apply the `second-order-effects` skill to produce a complete effects map.

## Step 1: Anchor the First-Order Outcome

State the direct intended outcome in one sentence:
> "If [action], then [immediate result] within [timeframe]."

## Step 2: Second-Order Effects Table

For each of the 4 axes, identify effects caused by the first-order outcome:

**Axis 1 — Stakeholders**: Who changes behavior, priorities, or expectations because the first-order outcome occurred?

**Axis 2 — Adjacent Systems**: Which systems, workflows, or processes are affected because the first-order change propagates into them?

**Axis 3 — Incentives & Behaviors**: How do individual or team behaviors shift because of the new outcome? Identify both positive incentives and perverse ones.

**Axis 4 — Feedback Loops**: What self-reinforcing or self-correcting dynamics activate?
- Reinforcing: effect amplifies over time
- Balancing: effect generates pressure that limits or reverses itself

For each second-order effect, score:
- Likelihood: H (>60%) / M (30–60%) / L (<30%)
- Magnitude: H (material Revenue/Risk/Cost impact) / M (moderate) / L (minor)
- RRC tag: Revenue / Risk / Cost
- PPT axis: People / Process / Technology
- Timeline: 0–30d / 31–90d / 91–180d / 180d+

## Step 3: Third-Order Effects (High-Severity Only)

For each second-order effect where Likelihood ≥ M AND Magnitude ≥ M:
- Follow the causal chain one more layer using the same 4 axes
- Apply the same scoring
- Stop at third layer — do not recurse further

## Step 4: Feedback Loop Analysis

For each identified feedback loop:
- Is it reinforcing or balancing?
- What triggers it to activate?
- What is the realistic timeline before it becomes material?
- What is the ceiling or floor if left unchecked?

## Step 5: High-Severity Chain Flags

For any chain that is high-severity (reinforcing feedback loop, or third-order magnitude > first-order magnitude, or crosses unanticipated system boundaries):

| Chain | Monitor Indicator | Decision Threshold | Mitigation | Owner |
|---|---|---|---|---|
| [describe chain] | [what to measure] | [if X reaches Y, escalate] | [guardrail or intervention] | [role] |

## Step 6: Recommended Monitoring Plan

List 3–5 leading indicators that would signal effects are activating earlier than expected. For each:
- Metric or signal name
- Current baseline (if known)
- Alert threshold
- Review cadence
- Accountable owner
```

## Expected Output
- First-order outcome statement (one clear sentence)
- Second-order effects table with all fields populated
- Third-order effects for high-severity second-order effects only
- Feedback loop analysis (reinforcing vs. balancing, timeline, ceiling/floor)
- High-severity chain flags with monitor indicators and decision thresholds
- Monitoring plan with 3–5 leading indicators

## Tips
- Prioritize surfacing effects the decision-maker has NOT thought of — effects they already know belong in risk assessment, not here
- Perverse incentives (Axis 3) are the most commonly missed second-order effect — spend extra time here
- A reinforcing feedback loop in the second layer with no monitoring is a critical finding, regardless of how small the first-order effect seems
- Third-order effects are only worth tracing if the second-order effect is material — avoid recursive exhaustion on low-severity chains
- Tag every effect with RRC and PPT — untagged effects are not actionable
