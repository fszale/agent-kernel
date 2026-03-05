---
name: autonomy-ladder
description: Design and manage a progressive autonomy system (L0–L3) for AI agents, with defined promotion criteria, demotion triggers, and calibrated review cadences at each level.
when-to-use: Use when deploying any autonomous agent or automated decision-making workflow. Use when an existing agent's performance warrants promotion to higher autonomy. Use after any incident to review demotion appropriateness.
principles: [Autonomy Ladder, HITL Design, Rate of Improvement, Confidence Scoring]
---

# Autonomy Ladder Skill

## Purpose

Manage how much autonomy an agent has in a disciplined, evidence-based way. Autonomy is earned through demonstrated performance — never granted upfront.

## Agent Instructions

You are an agent autonomy manager and performance reviewer.

### The Four Levels

| Level | Name | What the Agent Does | Human Role |
|---|---|---|---|
| **L0** | Observe | Detects patterns, reports findings; proposes nothing | Reviews daily brief; decides all responses |
| **L1** | Recommend | Proposes actions with expected value and risk; presents options | Reviews recommendations; decides what to execute |
| **L2** | Approve-to-Execute | Generates complete executable payload; executes only after explicit approval | Approves or rejects in review interface |
| **L3** | Guardrailed Auto | Executes autonomously within guardrail envelope; alerts on anomalies | Audits weekly; responds to alerts; reviews anomalies |

<!-- DIAGRAM: autonomy-ladder START -->
```mermaid
graph LR
    L0["🔭 L0
OBSERVE
──────────
Detects + reports
No proposals
No execution"]
    L1["💡 L1
RECOMMEND
──────────
Proposes actions
Expected value
Human decides"]
    L2["✅ L2
APPROVE-TO-EXEC
──────────
Full payload ready
Human approves
Then executes"]
    L3["🚀 L3
GUARDRAILED AUTO
──────────
Executes in envelope
Alerts on anomaly
Weekly audit"]

    L0 -->|"PROMOTE: 4+ weeks
accurate detection
no incidents"| L1
    L1 -->|"PROMOTE: 4+ weeks
ROI > threshold
errors < 1%"| L2
    L2 -->|"PROMOTE: 4+ weeks
provable value
guardrail adherence"| L3

    L3 -->|"DEMOTE:
anomaly detected"| L2
    L2 -->|"DEMOTE:
incident occurs"| L1
    L1 -->|"DEMOTE:
kill switch"| L0

    NEW["🆕 New agent
or capability"] -->|"Always start here"| L0

    style L0 fill:#1a3a5c,color:#fff,stroke:#4a9ede
    style L1 fill:#1a4a2e,color:#fff,stroke:#4ade80
    style L2 fill:#3a3a1a,color:#fff,stroke:#facc15
    style L3 fill:#1a4a2e,color:#fff,stroke:#4ade80
    style NEW fill:#2a2a2a,color:#fff,stroke:#6b7280
```
<!-- DIAGRAM: autonomy-ladder END -->

### Promotion Criteria (L→L+1)

**ALL of the following must be true for 4+ consecutive weeks:**

| Criterion | How to Verify |
|---|---|
| ROI > defined threshold (e.g., 5×) | Positive expected value realized from executed actions |
| Error rate < defined threshold (e.g., 1%) | Percentage of actions producing unintended outcomes |
| No incidents attributable to this agent | No human-reported problems triggered by agent actions |
| Guardrail adherence | No guardrail violations (blocked actions indicate miscalibration) |

**Promotion process:**
1. Review evidence for all 4 criteria across last 4 weeks
2. Document the evidence in an autonomy review record
3. Human decision: promote, hold, or demote
4. Update agent spec with new autonomy level
5. Notify team of change and new review schedule

### Demotion Triggers (immediate, any one sufficient)

| Trigger | Action |
|---|---|
| Severe anomaly (spend spike, data breach, system failure) | Demote to L0 immediately; activate kill switch |
| Incident attributable to agent automation | Demote to L1; investigate root cause before re-promotion |
| Manual kill switch activation | Demote to L2 pending investigation |
| Sustained error rate > threshold | Demote one level; recalibrate before review |
| Data quality failure | Suspend (hold at current level, pause execution) |

**Demotion is not failure — it is the system working correctly.** An agent that gets demoted and is recalibrated before re-promotion is safer than one that was never demoted.

### Review Cadence by Level

| Level | Review After | What to Review |
|---|---|---|
| L0 | 2 weeks | Is detection accurate? Are reports actionable? |
| L1 | 4 weeks | Are recommendations high quality? What % are accepted? |
| L2 | 6 weeks | Are approvals routine or frequently rejected? Is confidence calibrated? |
| L3 | Weekly alert review | Anomaly log; guardrail violations; KPI trends |

### Starting Level for New Agents

Always start new capabilities at **L0**:
- Observe first; understand what the agent actually detects
- Verify accuracy of detection before allowing recommendations
- This is not optional, even for "simple" cases

### Applying to Batches of Action Types

An agent can be at different levels for different action types:
- Action type A (well-tested): L3
- Action type B (new capability): L0
- Action type C (medium risk): L2

Manage autonomy at the action-class level, not just the agent level.

## Output Format

Autonomy review document:
1. Current level and action-type breakdown
2. Promotion evidence (4 criteria × 4 weeks)
3. Promotion/hold/demotion recommendation with rationale
4. New review schedule
5. Any open anomalies or incidents to resolve before re-promotion
