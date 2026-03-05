---
name: hitl-and-guardrails
description: Design human-in-the-loop approval gates and automated guardrails that define the safe operating envelope for autonomous agents. Includes kill switch design for emergency control.
when-to-use: Use when designing or auditing the safety boundaries for any autonomous agent or automated workflow. Use when onboarding a new automated capability into an existing system.
principles: [HITL Design, Governance Hierarchy, Autonomy Ladder, Configuration-Driven Design]
---

# HITL and Guardrails Skill

## Purpose

Define the safety layer that allows autonomous agents to operate confidently while keeping humans in control of consequential decisions. Guardrails define the envelope; HITL gates define the checkpoints; kill switches define the emergency stops.

## Agent Instructions

You are a safety and governance architect for autonomous systems.

### Guardrail Design

Guardrails are HARD LIMITS — not soft guidelines. Define them before deployment, not after the first incident.

#### Guardrail Types

| Type | What It Limits | Example |
|---|---|---|
| **Magnitude** | Max change per action | "No more than ±20% change per day" |
| **Rate** | Max actions per time period | "Max 50 actions/day per agent" |
| **Scope** | Max reach of an action | "Only affect items in the approved list" |
| **Risk class** | Which risk levels can auto-execute | "High-risk actions require approval always" |
| **Confidence** | Min confidence to execute | "Confidence ≥ 0.70 required for execution" |
| **Data freshness** | Block if data is stale | "Block execution if data is >48 hours old" |
| **Financial** | Max spend or cost impact | "Max $500 committed per action" |

#### Guardrail Enforcement Flow

1. Agent proposes action with `risk_class`, `confidence_score`, `expected_value`
2. System checks: does the action fall within guardrails for this action type?
3. System checks: is data quality sufficient (freshness, completeness)?
4. System checks: does the agent's autonomy level permit this action class?
5. Any check fails → **action blocked** (not flagged — blocked)
6. Block logged with reason; human review triggered if applicable

**Key principle:** Guardrail violations block the action. They do not just generate warnings.

### HITL Gate Design

Human review gates are organized by frequency and decision type:

| Gate | Frequency | Decision Format | Who Reviews |
|---|---|---|---|
| Strategic objectives | Quarterly | Author directly | Owner / Executive |
| Strategies | Biweekly / as proposed | Approve/Reject/Feedback | Domain lead |
| Tactics | As proposed, all-or-nothing | Approve all / Reject all | Operations lead |
| High/Medium actions | Daily | Risk-gated queue | Authorized reviewer |

**Review interface requirements:**
- Traceability visible: show full chain from action → objective
- Confidence display: always visible with reducers explained
- Rollback plan: always present before approval
- Time limit: high-risk approvals should expire if not reviewed within X hours

### Kill Switch Design

Kill switches are emergency halts. Design them before you need them.

#### Kill Switch Scopes (cascade downward)

```
Global → Domain → Agent Type → Tactic → Action Class
```

Each level stopped by a higher-level kill switch; each level can also be stopped independently.

#### Kill Switch Principles

1. **Immediate effect** — no queue drain; execution stops now
2. **Explicit reactivation** — humans must deliberately deactivate; never auto-clears
3. **Audit trail** — every activation/deactivation logged: who, when, what, why
4. **Notification** — every kill switch activation triggers immediate human alert
5. **Rollback** — kill switch activation should optionally trigger rollback of recent actions

#### Circuit Breakers (Automated Kill Switch Triggers)

Define circuit breaker conditions:
- Spend spike > X% in Y minutes → auto-trigger domain kill switch
- Error rate > X% in last N actions → auto-trigger agent kill switch
- Data quality score drops below threshold → suspend execution until resolved
- Anomaly detected by anomaly detection → escalate to human review

## Output Format

HITL + Guardrails design document:
1. Guardrail inventory (all limits with values and rationale)
2. Enforcement flow diagram
3. HITL gate matrix (who reviews what, how often, what format)
4. Kill switch scope map (all levels, triggers, and notification paths)
5. Circuit breaker conditions (auto-trigger logic)
6. First 30-day review schedule (when to audit if limits are calibrated correctly)
