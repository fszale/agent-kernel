# Prompt: Action Proposal

## Purpose
Propose a single executable action with full traceability, calibrated confidence, guardrail evaluation, expected value, rollback plan, and required decision rationale fields.

## When to Use
- When an agent is ready to propose a specific executable action for human review or auto-execution
- When generating action payloads for any governed workflow
- When testing action proposal quality against governance standards

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{action_type}}` | Category of action | "Process automation", "Budget reallocation", "Content update" |
| `{{objective}}` | Business objective this traces back to | "Reduce processing cost by 20%" |
| `{{tactic_or_strategy}}` | The parent tactic or strategy | "Automate invoice matching workflow" |
| `{{available_data}}` | Data available to inform this action | "Last 90 days of processing logs, error rate history" |
| `{{guardrails}}` | Limits that apply to this action type | "Max 30% scope change per action, confidence ≥ 0.7 required" |

## Prompt

```
You are an action proposer. Generate a complete, governance-ready action proposal.

Action type: {{action_type}}
Objective: {{objective}}
Parent tactic or strategy: {{tactic_or_strategy}}
Available data: {{available_data}}
Guardrails: {{guardrails}}

## Action Proposal Structure

### 1. Action Description
Clear, one-sentence description of what the action does and what it affects.

### 2. Traceability
- Tactic alignment: HOW does this action contribute to the parent tactic/strategy?
- Strategy alignment: HOW does the tactic/strategy connect to the objective?
- Objective: [state the objective]
- Traceability test: Can this chain be read in <30 seconds? Yes / No

### 3. Confidence Assessment
State your confidence score (0.0–1.0):
- Starting estimate: [value]
- Apply reducers:
  - Data stale >48h: [Y/N] → −0.10
  - Sample <7 days: [Y/N] → −0.10
  - First time this action type: [Y/N] → −0.15
  - Conflicting signals: [Y/N] → −0.10
  - External unaccounted factors: [Y/N] → −0.10
- Final confidence: [value]
- Interpretation: [Auto-execute / HITL required / Flag for review / Do not execute]

### 4. Guardrail Evaluation
For each applicable guardrail, check compliance:
| Guardrail | Limit | Proposed Value | Pass/Fail |
|---|---|---|---|
| [Guardrail name] | [limit] | [proposed] | [P/F] |

If any guardrail fails: **BLOCK THIS ACTION**. Provide alternative that passes.

### 5. Expected Value
- Primary metric affected: [metric name]
- Estimated impact: [amount + timeframe]
- Basis for estimate: [data or reference used]

### 6. Rollback Plan
- Is this action reversible? Yes / Partially / No
- Rollback steps: [specific, executable steps to undo]
- Time to rollback: [estimate]

### 7. Decision Rationale (REQUIRED FIELDS)
- **justification**: Why was this action chosen over alternatives? What alternatives were considered and why were they ruled out?
- **reasoning_summary**: Step-by-step summary of the chain of thought: [data observed] → [pattern identified] → [action derived] → [expected outcome]
```

## Expected Output
- Complete action proposal with all fields
- Confidence score with reducers applied
- Guardrail compliance table
- Rollback plan
- justification and reasoning_summary fields (non-negotiable)

## Tips
- If any guardrail fails, do not propose the action — propose the alternative that passes instead
- Always write justification and reasoning_summary even for "obvious" actions — these fields are for auditors, not the agent's benefit
- If confidence falls below 0.5 after reducers, flag for human review regardless of risk class
