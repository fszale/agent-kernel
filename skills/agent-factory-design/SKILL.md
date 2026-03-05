---
name: agent-factory-design
description: Design coordinated fleets of domain agents (agent factories) at any evolution stage — from a single agent to cross-factory networks — with orchestration, event contracts, HITL governance, and production and digital output coordination.
when-to-use: Use when designing systems with two or more agents, when planning how AI agents and human teams interact at scale, or when architecting inter-factory communication for Era 3 and Era 4 agentic systems.
principles: [Governance Hierarchy, HITL and Guardrails, Autonomy Ladder, Systems Over Goals, Configuration-Driven Design]
---

# Agent Factory Design Skill

## Purpose

Design agent factories at any of the four evolutionary stages. Produces an orchestration architecture, event bus contract, HITL governance model, and coordination diagram.

## The Four Eras

Use this reference when positioning a client or project on the evolution curve:

| Era | Name | What Exists | Key Challenge |
|---|---|---|---|
| 1 | Single Agent | One domain agent + human operator | Prove value, earn trust |
| 2 | Agent Factory | Coordinated fleet + shared orchestrator | Cross-domain coordination |
| 3 | Hybrid Factory | AI fleet + humans with personal AI | Authority and escalation design |
| 4 | Factory of Factories | Multi-organization agent networks | Trust, protocols, governance standards |

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

## Agent Instructions

You are a factory architect. Design a complete agent factory at the specified Era.

---

### Step 1: Establish the Factory Mandate

1. What is the factory's primary business output? (tangible: a report, a shipment, a reconciled account, a product build)
2. Which KPIs does the factory move as a system?
3. What mix of **digital artifacts** (reports, data, recommendations) and **real-world tangibles** (orders fulfilled, products built, services rendered) does the factory produce?

---

### Step 2: Inventory Agents and Roles

List all agents in the factory:

| Agent ID | Domain | Autonomy Level | Primary KPI | Emits | Consumes |
|---|---|---|---|---|---|
| | | L0-L3 | | | |

**Design rule:** Every agent in a factory must have a unique domain. If two agents share a domain, consolidate them.

---

### Step 3: Design the Orchestrator

The orchestrator is NOT a mega-agent. It is a coordination layer:

| Orchestrator Responsibility | Implementation |
|---|---|
| Task routing | Event-type → capable agent matching (via `discovery.capabilities`) |
| Scheduling | Dependency graph — which agents must complete before others run |
| Escalation | What agent failures or threshold breaches go to human review |
| State management | What shared context does the factory maintain across agent runs |

Produce a brief orchestrator specification:
```yaml
orchestrator:
  routing: capability-match
  schedule: dependency-ordered
  conflict_resolution: human-escalation
  state_store: shared-context-db
  hitl_escalation_triggers:
    - factory_error_rate_exceeds: 0.05
    - daily_budget_exceeds_pct: 0.90
    - kill_switch_any_domain: true
```

---

### Step 4: Define the Event Bus Contract

The event bus is how agents communicate. For each event:

```yaml
events:
  - name: "domain_entity_event"     # snake_case, past tense
    emitted_by: "agent_id"
    consumed_by: ["agent_id_1", "agent_id_2"]
    payload_required_fields:
      - "source_agent_run_id"
      - "entity_id"
      - "metric_and_value"
      - "confidence_score"
      - "justification"
```

**Standard payload required fields for all events:**
- `source_agent_run_id` (traceability)
- `confidence_score` (quality signal)
- `justification` (explain why this event was emitted)

---

### Step 5: Design HITL Governance for the Factory

Factory-level HITL decisions, beyond individual agent HITL:

| Scenario | Who Reviews | SLA |
|---|---|---|
| Agent conflict (two agents with contradictory recommendations) | Factory owner | 4 hours |
| Factory-wide budget alert | Operator | 2 hours |
| Cross-factory event with financial or safety implications | Senior human | 1 hour |
| Kill switch trigger | On-call human | Immediate |

**Era 3 (Hybrid):** Also document each human expert's personal AI task allocation and what the shared fleet can do on their behalf without asking.

**Era 4 (Factory of Factories):** Document the inter-factory trust protocol:
- How does Factory A know a message from Factory B is trustworthy?
- What cross-factory actions require a HITL gate?
- What is the dispute resolution process?

---

### Step 6: Map Outputs to Value Streams

The factory must connect every agent output to a value stream:

| Agent | Output Type | Value Stream | Tangible or Digital |
|---|---|---|---|
| | Analysis/Rec/Exec | Revenue/Risk/Cost | T / D |

**Tangible outputs** = real-world, physical, or contractual results (inventory moved, invoice paid, service delivered, product shipped).
**Digital outputs** = data artifacts (reports, alerts, recommendations, classifications, updated records).

An Era 4 factory of factories can chain digital outputs from one factory into tangible outputs for another.

---

### Step 7: Design the Factory Autonomy Governance

Apply autonomy-ladder principles at the factory level:

| Factory State | Action |
|---|---|
| New | All agents at L0-L1; orchestrator logs only |
| Proven (4+ weeks) | Eligible agents promoted to L2 |
| Mature | Candidate agents promoted to L3 within their guardrail envelope |
| Incident | Affected domain demoted; root cause analysis required |

---

## Output Format

1. Era classification and factory mandate
2. Agent inventory table
3. Orchestrator specification (YAML block)
4. Event bus contract (all emits/consumes)
5. Factory HITL governance table
6. Output mapping to value streams (tangible + digital)
7. Factory architecture diagram reference (use `diagram-design` skill to create `agent-factory-evolution.mmd`)
