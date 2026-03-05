# Prompt: PPT Assessment

## Purpose
Evaluate any decision, change, or initiative through the People · Process · Technology lens. Produces a structured impact assessment with ranked recommendations.

## When to Use
- Before making any significant organizational or technical decision
- During change management planning
- When a decision has unclear second-order effects

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{decision}}` | The decision or change being assessed | "Replacing manual weekly reporting with an automated dashboard" |
| `{{context}}` | Background and current state | "Finance team of 5 spends 8hrs/week on Excel reports" |
| `{{options}}` | 2–3 options being considered (or just describe the one option) | "Option A: Build custom. Option B: Use off-shelf tool." |

## Prompt

```
You are a PPT (People, Process, Technology) impact analyst.

Decision: {{decision}}
Context: {{context}}
Options: {{options}}

## 1. People Impact
For each stakeholder group affected:
- Who benefits and how?
- Who is at risk or negatively affected?
- What training or change management is required?
- What is the adoption risk?
- Estimated People impact: High / Medium / Low (positive or negative)

## 2. Process Impact
- What workflows change and how?
- Where does complexity increase or decrease?
- What manual work is eliminated? What new manual work is introduced?
- What are the bottleneck risks?
- What does the optimized process look like (diagram or step list)?
- Estimated Process impact: High / Medium / Low

## 3. Technology Impact
- What systems are affected or required?
- What is the integration complexity?
- What is the security/reliability/maintenance implication?
- Build vs. buy vs. configure?
- Estimated Technology impact: High / Medium / Low

## 4. Value Stream Assessment
For each option, rate impact (1–5):

| Option | Revenue | Risk Reduction | Cost Savings | Total |
|---|---|---|---|---|
| A | | | | |
| B | | | | |

## 5. Risk Register
Top 3 risks across all options:
- Risk: [description]
- Likelihood: High / Medium / Low
- Impact: High / Medium / Low
- Mitigation: [specific action]

## 6. Ranked Recommendation
Rank options from best to worst with rationale. Include:
- Which option best balances all three PPT dimensions
- What must be true for the recommended option to succeed
- First 30-day implementation step
```

## Expected Output
- Structured PPT assessment (all 3 dimensions)
- Value stream scoring for each option
- Risk register with mitigations
- Ranked recommendation with rationale
