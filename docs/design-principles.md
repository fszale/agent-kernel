# docs/design-principles.md

# Design Principles Reference

This is the condensed reference for all principles encoded in the agent-kernel. For the full documentation, see [PHILOSOPHY.md](../PHILOSOPHY.md).

---

## Quick Reference Card

### The Four Operating Principles

| Principle | One-Line Summary | Primary Use |
|---|---|---|
| **Pareto (80/20)** | 20% of work delivers 80% of value — find that 20% | Prioritization, planning |
| **30/60/90** | Immediate / Soon / Later — map everything to a horizon | Planning, goal-setting |
| **First Principles** | Strip all assumptions, rebuild from base elements | Problem-solving, design |
| **Bias Towards Action** | A good decision now beats a perfect decision later | Execution, anti-paralysis |

### The PPT Evaluation Trifecta

Every significant decision must address all three dimensions:

```
People    → Who is affected? Skills needed? Change management?
Process   → What workflows change? Where are the bottlenecks?
Technology → What tooling? Integration complexity? Build vs. buy?
```

### Three Value Streams

Every output should connect to at least one:
- 💰 **Revenue Generation** — grow the top line
- 🛡️ **Risk Mitigation** — reduce probability or impact of failure
- 💸 **Cost Savings** — eliminate waste or reduce operating expense

---

## Principle Lookup by Situation

| Situation | Best Principle |
|---|---|
| "We're overanalyzing and not doing anything" | Bias Towards Action |
| "Everything feels equally important" | Pareto (80/20) |
| "We have no idea where to start" | 30/60/90 + Pareto |
| "The conventional solution isn't working" | First Principles |
| "The team is stuck and demoralized" | Shake the Box |
| "We need to make a major decision" | PPT Assessment |
| "We need to measure AI impact" | Rate of Improvement |
| "We need to deploy an autonomous agent safely" | Governance Hierarchy + HITL |
| "An agent is making too many unchecked decisions" | Autonomy Ladder + Guardrails |
| "Our actions aren't traceable back to objectives" | Traceability Contract |

---

## Governance Hierarchy Summary

```
Business Objective (human-authored quarterly)
         ↓  objective_alignment
Strategy (agent-proposed, human-approved biweekly)
         ↓  strategy_alignment + intent
Tactic (action bundle, all-or-nothing approval)
         ↓  tactic_alignment
Action (atomic execution, risk-gated)
```

**30-second traceability test:** Every action must trace to an objective in under 30 seconds.

<!-- DIAGRAM: governance-hierarchy START -->
```mermaid
graph TB
    subgraph HUMAN["👤 Human-Authored"]
        OBJ["🎯 Business Objective
─────────────────
rationale: WHY this matters
priority: Critical|High|Med|Low
target_kpis: metric + timeframe"]
    end

    subgraph AGENT_APPROVED["🤖 Agent-Proposed · Human-Approved"]
        STR["📐 Strategy
─────────────────
objective_alignment: HOW not WHICH
thesis: falsifiable claim
evidence: supporting data
expected_outcomes: KPI + timeframe"]
    end

    subgraph AGENT_BUNDLE["🔗 Agent-Bundled · All-or-Nothing Approval"]
        TAC["📦 Tactic
─────────────────
strategy_alignment: HOW not WHICH
intent: WHY actions must go together
execution_mode: Sequential|Parallel|Phased
risk_level: Low|Med|High"]
    end

    subgraph AGENT_EXEC["⚡ Agent-Executed · Risk-Gated"]
        ACT["🔧 Action
─────────────────
tactic_alignment: role in bundle
risk_class: Low|Med|High
confidence_score: 0.0-1.0
expected_value: $ or metric delta
justification: REQUIRED
reasoning_summary: REQUIRED
rollback: how to undo"]
    end

    OBJ -->|"Quarterly HITL review"| STR
    STR -->|"Biweekly HITL review"| TAC
    TAC -->|"All-or-nothing HITL"| ACT

    ACT -->|"✅ 30-sec traceability test"| OBJ

    GUARD["🛡️ Guardrails
max_change_pct
min_confidence
max_actions/day
financial_cap"] -.->|"blocks violations"| ACT
    KILL["🔴 Kill Switches
Global → Domain
→ Agent Type
→ Tactic
→ Action Class"] -.->|"immediate halt"| ACT

    style HUMAN fill:#1a3a5c,color:#fff,stroke:#4a9ede
    style AGENT_APPROVED fill:#1a4a2e,color:#fff,stroke:#4ade80
    style AGENT_BUNDLE fill:#3a2a5c,color:#fff,stroke:#a78bfa
    style AGENT_EXEC fill:#4a2a1a,color:#fff,stroke:#fb923c
    style GUARD fill:#2a1a1a,color:#fff,stroke:#f87171
    style KILL fill:#2a1a1a,color:#fff,stroke:#f87171
```
<!-- DIAGRAM: governance-hierarchy END -->

## Autonomy Ladder Summary

| Level | Name | Executes? | When |
|---|---|---|---|
| L0 | Observe | ❌ Never | New, unknown capabilities |
| L1 | Recommend | ❌ Proposes only | Proven detection, unproven execution |
| L2 | Approve-to-Execute | ✅ With human approval | Established with HITL |
| L3 | Guardrailed Auto | ✅ Within envelope | Proven track record (4+ weeks) |

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

## Rate of Improvement Summary

```
Deploy → Measure the metric the business cares about → Track weekly
Expected curve: Rapid rise → Taper → Stable (S-curve = SUCCESS)
```

Formula: `RoI(t) = ΔI/Δt` — rate of improvement per time period.

<!-- DIAGRAM: rate-of-improvement-curve START -->
<!-- DIAGRAM: rate-of-improvement-curve END -->

<!-- DIAGRAM: agent-factory-evolution START -->
```mermaid
graph TB
    subgraph ERA1["⚙️ Era 1 — Single Agent
Today: pilot deployments"]
        A1["🤖 Domain Agent
(e.g., Accounting Agent)
L0→L3 autonomy
HITL per action
Guardrailed"]
        H1["👤 Human
operator + approver"]
        A1 <-->|"approvals
recommendations"| H1
    end

    subgraph ERA2["🏭 Era 2 — Agent Factory
Near future: coordinated fleets"]
        ORCH["🧠 Orchestrator
(event bus + scheduler
+ routing)"]
        A2a["🤖 Finance
Agent"]
        A2b["🤖 Operations
Agent"]
        A2c["🤖 Support
Agent"]
        A2d["🤖 Intelligence
Agent"]
        H2["👥 Human Team
(HITL where needed)"]
        ORCH --> A2a & A2b & A2c & A2d
        A2a <-->|"cross-agent events"| A2b
        A2b <-->|"cross-agent events"| A2c
        A2c <-->|"cross-agent events"| A2d
        ORCH <-->|"escalations
strategic approvals"| H2
    end

    subgraph ERA3["🏭+👤 Era 3 — Hybrid Factory
Mid future: AI amplifies humans"]
        HF1["👤 Human Expert
with personal AI
assistant factory"]
        HF2["👤 Human Expert
with personal AI
assistant factory"]
        SHARED["🤖 Shared Agent
Factory
(coordinated fleet)"]
        HF1 <-->|"instructions
high-level goals"| SHARED
        HF2 <-->|"instructions
high-level goals"| SHARED
        HF1 <-->|"collaboration"| HF2
    end

    subgraph ERA4["🌐 Era 4 — Factory of Factories
Far future: autonomous coordination"]
        FAC_A["🏭 Factory A
(Company / Domain A)
AI fleet + humans"]
        FAC_B["🏭 Factory B
(Company / Domain B)
AI fleet + humans"]
        FAC_C["🏭 Factory C
(Company / Domain C)
AI fleet + humans"]
        PROTO["📋 Standard Protocol
(agent-to-agent API
trustability contracts
verifiable rationale)"]
        FAC_A <-->|"agent-to-agent
calls"| PROTO
        FAC_B <-->|"agent-to-agent
calls"| PROTO
        FAC_C <-->|"agent-to-agent
calls"| PROTO
        HITL_GOV["👤 HITL Governance
(cross-factory standards
audit + intervention)"]
        PROTO <-->|"exceptions
escalations"| HITL_GOV
    end

    ERA1 -->|"scale up: add agents"| ERA2
    ERA2 -->|"empower humans: personal AI"| ERA3
    ERA3 -->|"standardize: inter-factory protocols"| ERA4

    style ERA1 fill:#1a3a5c,color:#fff,stroke:#4a9ede
    style ERA2 fill:#1a4a2e,color:#fff,stroke:#4ade80
    style ERA3 fill:#3a3a1a,color:#fff,stroke:#facc15
    style ERA4 fill:#3a2a5c,color:#fff,stroke:#a78bfa
```
<!-- DIAGRAM: agent-factory-evolution END -->

---

*For the full documentation of each principle, see [PHILOSOPHY.md](../PHILOSOPHY.md).*
