# Prompt: Idea Evaluator

## Purpose
Evaluate any idea or initiative using the PPT framework combined with Revenue, Risk, and Cost dimensions. Produces a scored, actionable assessment.

## When to Use
- Before committing resources to any new idea, product, or initiative
- When comparing multiple competing options
- When stakeholders need a structured rationale for a decision

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{idea_name}}` | Name of the idea or initiative | "AI-Powered Invoice Processing" |
| `{{idea_description}}` | 2–3 sentence description | "Automate invoice matching using AI..." |
| `{{business_context}}` | Industry, size, current challenges | "B2B services company, 50 employees, rapid growth" |
| `{{constraints}}` | Budget, timeline, or technical limitations | "Max 3-month timeline, no new headcount" |

## Prompt

```
You are a strategic idea evaluator with expertise in People, Process, and Technology (PPT) analysis.

Idea: {{idea_name}}
Description: {{idea_description}}
Business context: {{business_context}}
Constraints: {{constraints}}

Perform a complete evaluation of this idea:

## 1. Idea Clarity
State clearly in one paragraph: what the idea is, what problem it solves, who benefits, and what success looks like in 90 days.

## 2. PPT Scoring Matrix
Score each cell 1–10 and provide 2–3 sentence rationale for each score:

| Dimension | Revenue (1-10) | Risk (1-10) | Cost (1-10) |
|-----------|---------------|-------------|-------------|
| People    |               |             |             |
| Process   |               |             |             |
| Technology|               |             |             |

## 3. Quantitative Analysis
- Total Addressable Market (TAM): research and estimate
- Top 3 alternatives/competitors: features, pricing, key differentiators
- Scenario modeling:
  - Conservative: [outcome + assumptions]
  - Expected: [outcome + assumptions]
  - Optimistic: [outcome + assumptions]

## 4. Risk Assessment
- Top 3 risks (one per PPT dimension)
- Mitigation strategy for each

## 5. 30/60/90 Roadmap
- 30 days: [immediate actions]
- 60 days: [near-term milestones]
- 90 days: [target state]

## 6. Final Recommendation
- Total score (out of 90) and classification: Strong (75-90) / Promising (55-74) / Marginal (35-54) / Weak (<35)
- Pareto recommendation: the single highest-impact first action
- Go/No-Go verdict with one-paragraph rationale
- Value stream: primarily Revenue / Risk / Cost
```

## Expected Output
- Completed PPT scoring matrix with rationale
- Quantitative analysis with TAM + competitors + 3 scenarios
- 30/60/90 plan
- Scored classification and Go/No-Go recommendation

## Tips
- Be specific with numbers — ranges are acceptable but vague qualitative scores reduce value
- If the idea scores <35, recommend specific pivots rather than just rejecting
- Connect each PPT score to a concrete business example
