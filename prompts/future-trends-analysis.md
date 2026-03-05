# Prompt: Future Trends Analysis

## Purpose
Evaluate a planned initiative or roadmap against emerging macro trends to identify strategic alignment, gaps, and hedging opportunities.

## When to Use
- During annual or quarterly strategic planning
- When evaluating multi-year investment decisions
- When assessing whether current approaches are future-proof

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{initiative}}` | The plan or initiative being evaluated | "Building an AI customer support chatbot" |
| `{{time_horizon}}` | How far forward to evaluate | "2–3 years" |
| `{{context}}` | Industry and business context | "B2C ecommerce, 10K monthly orders" |

## Prompt

```
You are a strategic trend analyst. Evaluate this initiative against major macro trends over the specified time horizon.

Initiative: {{initiative}}
Time horizon: {{time_horizon}}
Context: {{context}}

Evaluate against these trend categories:

## 1. AI and Automation
- Is this initiative aligned with the direction of AI capability growth?
- Will advances in AI make this obsolete, improve it, or enable new capabilities?
- What is the risk that competitors will use AI to leapfrog this approach?

## 2. Human-Machine Convergence
- How does this initiative navigate the "automate vs. augment" question?
- What is the appropriate human-in-the-loop role 1–3 years from now?
- Is the designed human oversight level increasing or decreasing in the right direction?

## 3. Data and Personalization
- Does this initiative create, leverage, or improve a proprietary data asset?
- How does it position the organization on the personalization curve?
- What data produced by this initiative has compounding value over time?

## 4. Services and Subscription Models
- Is this initiative aligned with a shift from one-time transactions to recurring relationships?
- How does it affect customer retention and lifetime value?
- What subscription or service model could be built around this capability?

## 5. Platform and Integration Trends
- Does this initiative align or conflict with dominant platforms in this space?
- What API, ecosystem, or integration bets is this initiative implicitly making?
- What happens if a key platform dependency disappears or pivots?

## 6. Regulatory and Trust Trends
- What compliance or trust implications exist in this initiative's space?
- Is regulatory direction favorable, neutral, or a headwind?
- How does this initiative build or erode user trust?

## Trend Alignment Summary

| Trend | Alignment | Risk | Opportunity |
|---|---|---|---|
| AI & Automation | Strong/Neutral/Weak | | |
| Human-Machine | Strong/Neutral/Weak | | |
| Data & Personalization | Strong/Neutral/Weak | | |
| Services/Recurring | Strong/Neutral/Weak | | |
| Platform/Integration | Strong/Neutral/Weak | | |
| Regulatory/Trust | Strong/Neutral/Weak | | |

## Strategic Recommendations
1. [Most important adjustment to align with trends]
2. [Best hedge against the highest-risk trend divergence]
3. [Biggest opportunity to accelerate using trend tailwinds]
```

## Expected Output
- Analysis of all 6 trend categories
- Trend alignment summary table
- 3 strategic recommendations
