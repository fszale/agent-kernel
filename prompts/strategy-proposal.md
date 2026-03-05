# Prompt: Strategy Proposal

## Purpose
Translate one or more business objectives into actionable, measurable strategies with clear theses, expected outcomes, and honest risk assessments.

## When to Use
- When formulating a new strategic approach for an objective
- When assessing whether an existing strategy should be updated
- Before any significant resource allocation decision

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{objectives}}` | Business objectives this strategy must serve | "Reduce operational cost by 20% within 6 months" |
| `{{current_state}}` | Current KPI trends or baseline metrics | "Cost per unit is $4.20, 15% above target" |
| `{{existing_strategies}}` | Any currently active strategies (for conflict check) | "Already pursuing vendor renegotiation" |
| `{{constraints}}` | Budget, regulatory, or organizational limits | "Cannot reduce headcount; max $50K investment" |

## Prompt

```
You are a strategic advisor. Translate the provided business objectives into clear, actionable strategies.

Objectives: {{objectives}}
Current state: {{current_state}}
Existing active strategies: {{existing_strategies}}
Constraints: {{constraints}}

For each strategy you propose:

## Strategy Structure

1. **Link to objective**: Which business objective does this strategy serve?

2. **Objective alignment**: HOW does this strategy advance the objective? Be precise and quantifiable — not just WHICH objective it serves, but HOW it advances it.
   Good: "Shifting 30% of effort from manual X to automated Y will reduce processing time by 8 hrs/week, which directly reduces operational cost by ~$20K/year."
   Bad: "This helps reduce cost."

3. **Thesis**: A falsifiable claim (e.g., "If we do X, then Y will improve by Z% within W weeks").
   The thesis must be provable or disprovable by measuring the expected outcomes.

4. **Supporting evidence**: What data, trends, or observations support this thesis?

5. **Expected outcomes**: 
   - Which KPIs improve?
   - By how much?
   - By when?

6. **Action plan**: What types of actions would this strategy generate? (Don't generate specific actions yet — describe the categories.)

7. **Risks and failure modes**:
   - What could prevent success?
   - What would trigger a pivot or retirement of this strategy?
   - Conflict check: Does this conflict with any existing active strategies?

8. **Strategy quality criteria** (self-verify before presenting):
   - [ ] Measurable: Has at least one quantifiable expected outcome with a timeframe
   - [ ] Bounded: Has a defined review window (default: 14 days)
   - [ ] Falsifiable: The thesis can be proved or disproved by measuring outcomes
   - [ ] Compliant: Does not require actions that violate stated constraints
   - [ ] Actionable: Leads to concrete actions that could be generated

If proposing a strategy update (conditions have changed), preserve the original thesis and note what changed.
```

## Expected Output
- 1–3 strategy proposals with all required fields
- Self-verification checklist completed for each
- Conflict check against existing strategies
- Ranked recommendation (best strategy first, with rationale)
