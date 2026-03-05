# Prompt: Bottleneck Identification

## Purpose
Systematically identify and rank operational bottlenecks, scoring each for AI automation potential and producing a ranked list with a clear #1 recommendation.

## When to Use
- After completing a process audit or Shadow Walk observation
- When you have raw operational observations but need structured analysis
- To prioritize which problems to solve first

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{process_observations}}` | Raw notes from process observation | (paste Shadow Walk notes or audit output) |
| `{{business_context}}` | Industry, size, tech maturity | "B2B service company, 25 employees, uses accounting software + email" |
| `{{owner_priorities}}` | What the owner cares about most | "Reducing time on scheduling and customer follow-ups" |

## Prompt

```
You are an operational bottleneck analyst.

Business context: {{business_context}}
Owner's stated priorities: {{owner_priorities}}

Process observations:
{{process_observations}}

Analyze these observations and identify ALL operational bottlenecks. For each bottleneck:

1. **Name it**: Give a clear, concise label

2. **Describe it**: What is happening and why is it a problem?

3. **Quantify it**: Estimate:
   - Time consumed (hours/week)
   - Error frequency (errors per week or %)
   - Estimated cost impact ($)

4. **Score it** using this matrix:

| Factor | Weight | Score (1-5) | Weighted |
|---|---|---|---|
| Time consumed | 30% | | |
| Repetitiveness | 20% | | |
| Error frequency | 20% | | |
| Business impact | 20% | | |
| Data availability | 10% | | |
| **Composite** | | | |

5. **AI Readiness**:
   - 🟢 HIGH: Clear data, repetitive, standard AI capability
   - 🟡 MEDIUM: Partial data or requires some customization
   - 🔴 LOW: Unstructured, requires judgment, limited data

6. **Recommended approach**: In one sentence, if AI were applied, what would the solution look like?

Rank all bottlenecks by composite score (highest first).

Final output: "If you could only fix ONE bottleneck with AI, fix [X] because [specific, quantified reason]."
```

## Expected Output
- Ranked list of 5–10 bottlenecks with scores
- AI readiness rating for each
- One-line solution description per bottleneck
- Clear #1 recommendation with rationale

## Tips
- Cross-reference output with the owner's stated priorities
- Use this output as input to the [workflow-design.md](workflow-design.md) prompt for the #1 recommendation
- Revisit after deployment to recalculate scores against the new baseline
