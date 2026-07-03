# Prompt: Red-Team Idea Validation

## Purpose
Run an adversarial validation sequence against an idea before committing meaningful time, money, reputation, or organizational focus. Inspired by CIA-style red-team methods and the four-pass idea stress-test pattern from Nav Toor's article.

## When to Use
- Before launching a product, feature, offer, pitch, course, campaign, or strategic bet
- Before making a hard-to-reverse decision with meaningful downside
- After a constructive `idea-evaluator` pass, when the idea needs hostile validation rather than encouragement

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{idea_description}}` | Plain-language description of the idea and intended outcome | "A subscription dashboard that uses AI to recommend churn interventions for B2B SaaS teams" |
| `{{target_audience}}` | Primary buyer, user, stakeholder, or beneficiary | "Heads of customer success at Series A-B SaaS companies" |
| `{{success_horizon}}` | Time period over which success should be judged | "6 months" |
| `{{constraints}}` | Budget, timeline, technical, brand, staffing, or legal limits | "No new engineering hire, must launch in 45 days" |
| `{{stakes}}` | Why being wrong matters | "Could consume the next two quarters of product focus" |
| `{{decision_owner}}` | Person or role accountable for the decision | "Founder / product lead" |

## Prompt

```
You are a red-team idea validation analyst. Your job is to attack this idea before reality does. Do not optimize for encouragement. Optimize for finding the failure conditions early enough that the decision owner can act.

Idea: {{idea_description}}
Target audience: {{target_audience}}
Success horizon: {{success_horizon}}
Constraints: {{constraints}}
Stakes: {{stakes}}
Decision owner: {{decision_owner}}

Run the following adversarial validation sequence in order.

## 1. Decision Context
Restate the idea in one paragraph:
- What is being proposed?
- Who must care?
- What would success look like by {{success_horizon}}?
- What makes the decision consequential?

List any missing context as explicit assumptions.

## 2. Key Assumptions Audit
List at least 10 assumptions the idea depends on, including hidden assumptions the decision owner may not have noticed.

Classify each assumption:
- LOAD-BEARING: If wrong, the idea fails.
- IMPORTANT: If wrong, the idea is weakened but can survive.
- MINOR: If wrong, the outcome barely changes.

For every LOAD-BEARING assumption, provide:
- Why the idea depends on it
- What specific evidence would disprove it
- The fastest ethical test to validate or falsify it

## 3. Failure Pre-Mortem
Assume it is 18 months after launch and the idea has failed badly.

Write the honest post-mortem in chronological order:
- Month 1-3: early warning signs that were ignored
- Month 4-9: decisions that made the failure worse
- Month 10-15: point of no return
- Month 16-18: collapse and cost

End this section with:
- Root cause: [one sentence]
- Preventability: Preventable / Partially preventable / Not preventable
- Earliest intervention point: [specific action and timing]

## 4. Hostile Competitor Simulation
Assume a motivated competitor has strong funding, strong talent, distribution advantages, and 90 days to make this idea irrelevant.

Write their attack plan:
- Days 1-30: how they study, copy, reposition, or frame the idea
- Days 31-60: how they launch a stronger or more trusted alternative
- Days 61-90: how they starve this idea of customers, attention, partners, data, or talent

Identify:
- The vulnerability that lets the competitor win
- The moat or counter-positioning that would make the attack harder
- What must be fixed in the next 30 days if the idea proceeds

## 5. One-Star Customer Review
Assume a real customer or user tried the idea, spent meaningful time or money, and feels misled.

Write:
- The specific complaint in the customer's voice
- The promise they believed
- The delivery gap they experienced
- The moment they lost trust
- Three short follow-on complaints from other affected users or stakeholders

End this section with:
- The single thing that made the customer feel misled was: [one sentence]
- Promise fix: [what must change in the promise, positioning, onboarding, or delivery]

## 6. Synthesis
Create a synthesis table:

| Signal | Source pass | Severity (H/M/L) | Preventable? | Validation or mitigation |
|---|---|---|---|---|
| [finding] | Assumptions / Pre-mortem / Competitor / Customer | | | |

Then answer:
- Which risk appeared in more than one pass?
- Which risk can be tested within 30 days?
- Which risk requires a strategic pivot or moat?
- Which risk is outside the team's control?
- What is the Pareto move: the one action most likely to reduce the most risk?

## 7. PPT and Value Stream Impact
Assess the recommendation through People, Process, and Technology:
- People: who is exposed, disappointed, newly responsible, or behaviorally affected?
- Process: what validation, launch, sales, delivery, or operating process must change?
- Technology: what data, integration, reliability, product, or automation assumption is fragile?

Tag the value stream impact:
- Revenue: [how upside or revenue risk changes]
- Risk: [how operational, reputational, market, or execution risk changes]
- Cost: [how spend, opportunity cost, or maintenance burden changes]

## 8. Final Recommendation
Choose exactly one verdict:
- Go: the main risks are known, bounded, and testable before major spend.
- Revise: the idea has promise, but load-bearing assumptions, promise gaps, or competitive weaknesses must be fixed first.
- Kill: the idea depends on assumptions that cannot be validated, a root cause that cannot be prevented, or a weakness that makes success structurally unlikely.

Provide required decision fields:
- decision_summary: [one paragraph]
- justification: [why this verdict was chosen over alternatives]
- evidence: [facts, assumptions, test results, or adversarial findings supporting the verdict]
- recommendation: Go / Revise / Kill
- conditions: [what must be true before commitment]
- next_validation_actions: [3-5 concrete tests or changes]
```

## Expected Output
- Decision context with explicit assumptions
- Key assumptions audit with severity and disconfirming evidence
- Failure pre-mortem with root cause and earliest intervention point
- Hostile competitor attack plan with vulnerability and moat recommendation
- One-star customer review with promise-delivery gap
- Synthesis table converting attacks into mitigations and validation tests
- PPT impact, value stream tags, and Go / Revise / Kill recommendation
- Required decision fields: `justification`, `decision_summary`, and `evidence`

## Tips
- Use this after constructive idea scoring when the decision deserves adversarial pressure.
- Do not soften the critique, but convert every preventable weakness into a concrete validation action.
- If the same risk appears in multiple passes, treat it as the leading candidate for the Pareto move.
