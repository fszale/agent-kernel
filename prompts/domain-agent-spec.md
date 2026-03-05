# Prompt: Domain Agent Spec

## Purpose
Generate a complete, production-ready `agent-spec.yaml` for a new domain-specific agent. Produces all sections required by the agent-kernel governance framework.

## When to Use
- Designing a new domain agent for a business (finance, operations, sales, support, logistics, etc.)
- Translating a business mandate into a formal agent specification
- Reviewing an existing agent spec for completeness and governance compliance

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{agent_id}}` | Snake_case agent identifier | `accounting` |
| `{{domain}}` | Business domain | `finance` |
| `{{mandate}}` | 2–3 sentence agent mandate | "Reduce days-to-close by automating transaction categorization..." |
| `{{primary_kpi}}` | The one metric this agent most directly moves | `days_to_close` |
| `{{data_sources}}` | Comma-separated list of data inputs | `transactions, bank_statements, invoices` |
| `{{owner_role}}` | Role title responsible for this agent | `Finance Lead` |
| `{{starting_autonomy}}` | L0, L1, or L2 | `L1` |
| `{{domain_risk_profile}}` | standard / elevated (financial, medical, legal, safety) | `elevated` |

## Prompt

```
You are a domain agent architect. Generate a complete, governance-ready agent-spec.yaml.

Agent ID: {{agent_id}}
Domain: {{domain}}
Mandate: {{mandate}}
Primary KPI: {{primary_kpi}}
Data sources: {{data_sources}}
Owner role: {{owner_role}}
Starting autonomy level: {{starting_autonomy}}
Risk profile: {{domain_risk_profile}}

## 1. Discovery Block
Write a `discovery` block with:
- `description`: 2–3 sentences readable by an orchestrator without domain expertise
- `capabilities`: semantic tags in snake_case for what this agent can do
- `requirements.data_sources`: list of inputs needed
- `provides.analysis`: read-only outputs
- `provides.recommendations`: proposed actions needing human review
- `provides.execution`: state-changing actions

## 2. Action Definitions
Design all actions following these rules:
- All financial/medical/legal/safety domains: minimum autonomy L1 for recommendations
- All NEW agents: never start at L3
- For each action: id, risk_class, autonomy_level, required_fields, guardrails
- Include confidence threshold guardrails for all L2+ actions
- ALL actions require: confidence_score, expected_value, rollback_payload

For each action, required_fields MUST include:
  - justification (why this action was selected over alternatives)
  - reasoning_summary (step-by-step chain of thought)

## 3. HITL Configuration
Set confidence thresholds based on risk profile:
- Standard: low_risk_auto_min: 0.70, medium_risk_execute_min: 0.75
- Elevated: low_risk_auto_min: 0.95, medium_risk_execute_min: 0.95

## 4. Prompt Template Assignments
For each major task the agent performs, define a prompt entry:
  template: "{agent_id}/{task_name}"
  version: "1.0"
  variant: "default"

## 5. Model Routing
Assign model tiers:
- Classification/extraction tasks → fast/mini model
- Analysis/detection tasks → fast/mini model
- Reasoning/recommendations/generation → full model

## 6. Cross-Agent Events
Define:
- emits: What events does this agent emit when it detects something notable?
  Format: {domain}_{entity}_{event_verb} (e.g., revenue_variance_detected)
- consumes: What events from other agents should trigger this agent's response?

## 7. Cost Tracking
Specify what costs to track: llm_cost_usd, tooling_cost_usd, human_review_minutes

## 8. Logging Fields
Emit: agent_run_id, action_id, timestamp, risk_class, autonomy_level,
confidence_score, expected_value, status, prompt_version, justification

Output the complete, ready-to-use agent-spec.yaml.
Also provide:
- Autonomy promotion plan: criteria to go from starting level → next level
- Top 3 guardrail risks for this domain
```

## Expected Output
- Complete `agent-spec.yaml` (all sections)
- Autonomy promotion plan (starting level → target L2 or L3)
- Top 3 guardrail risks specific to this domain

## Tips
- For financial agents: set `enabled: false` until Day 30 review passes
- Always include `rollback_payload` in required_fields for financial mutations
- Cross-agent events should be domain-prefixed to avoid collisions across factories
