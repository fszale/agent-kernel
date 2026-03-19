---
name: domain-agent-design
description: Design complete domain-specific AI agents with capability discovery, skill assignments, prompt routing, model selection, action definitions, HITL rules, and cross-agent event contracts.
when-to-use: Use when scoping a new agent for a specific business domain (finance, operations, sales, support, etc.) that will run as part of a larger agent factory or standalone.
principles: [Governance Hierarchy, HITL and Guardrails, Autonomy Ladder, Configuration-Driven Design, Bias Towards Action]
---

# Domain Agent Design Skill

## Purpose

Design a production-ready domain agent from mandate to configuration. Produces a fully specified `agent-spec.yaml` with all governance, capability, scheduling, and safety fields populated.

<!-- DIAGRAM: agent-architecture START -->
```mermaid
graph TB
    subgraph INPUTS["Inputs"]
        DS["Data Sources
transactions, logs
KPIs, config"]
        CFG["Agent Config
guardrails, HITL
kill switches"]
        EVT_IN["Cross-Agent Events
consumed from bus"]
    end

    subgraph AGENT["Agent Runtime"]
        DISCO["Discovery Layer
capabilities
requirements
provides"]
        SKILLS["Skills
injected context
into system prompt"]
        PROMPTS["Prompts
task templates
with versioning
and A/B support"]
        MODEL["Model Router
primary to fallback
timeout handling"]
        RATIONALE["Decision Rationale
justification: REQUIRED
decision_summary: REQUIRED
evidence: REQUIRED"]
    end

    subgraph SAFETY["Safety Layer"]
        CONF["Confidence
Scoring
0.0 to 1.0"]
        GUARD["Guardrail
Evaluation
Hard limits"]
        HITL_GATE["HITL Gate
Low: auto
Med/High: approval"]
    end

    subgraph OUTPUTS["Outputs"]
        ANALYSIS["Analysis
read-only reports"]
        RECS["Recommendations
proposed actions"]
        EXEC["Execution
atomic actions
with rollback payload"]
        EVT_OUT["Cross-Agent Events
emitted to bus"]
    end

    DS --> DISCO
    CFG --> GUARD
    EVT_IN --> DISCO
    DISCO --> SKILLS
    SKILLS --> PROMPTS
    PROMPTS --> MODEL
    MODEL --> RATIONALE
    RATIONALE --> CONF
    CONF --> GUARD
    GUARD --> HITL_GATE
    HITL_GATE -->|"approved"| ANALYSIS
    HITL_GATE -->|"approved"| RECS
    HITL_GATE -->|"approved"| EXEC
    EXEC --> EVT_OUT

    style INPUTS fill:#1a3a5c,color:#fff,stroke:#4a9ede
    style AGENT fill:#1a4a2e,color:#fff,stroke:#4ade80
    style SAFETY fill:#3a2a1a,color:#fff,stroke:#fb923c
    style OUTPUTS fill:#3a2a5c,color:#fff,stroke:#a78bfa
```
<!-- DIAGRAM: agent-architecture END -->

## Agent Instructions

You are an agent architect. Design a complete domain agent based on the given context.

---

### Step 1: Define the Agent's Mandate

Answer four questions:
1. **What business problem does this agent solve?** (measurable, specific)
2. **What is the primary KPI it moves?** (one metric, not a list)
3. **Who owns this agent?** (a role title, not a person's name)
4. **What is its domain?** (finance, operations, sales, support, logistics…)

Write a 2–3 sentence `description` suitable for the `discovery` block — readable by an orchestrator without domain expertise.

---

### Step 2: Map Capabilities

List what the agent **provides** across three tiers:

| Tier | What It Is | Autonomy Minimum |
|---|---|---|
| `analysis` | Read-only reporting and assessment | L0 |
| `recommendations` | Proposed actions requiring human decision | L1 |
| `execution` | Actions that change state | L2 or L3 |

**Naming convention:** Use snake_case, domain-prefixed:
- `transaction_categorization` not `categorize`
- `variance_alert` not `alert`

---

### Step 3: Assign Skills and Prompts

Select which agent-kernel skills to inject into the agent's system context (keep total tokens < 3K):

| Situation | Recommended Skills |
|---|---|
| Agent handles financial data | `hitl-and-guardrails`, `confidence-and-experiment` |
| Agent makes recommendations | `governance-hierarchy-design`, `tactic-design` |
| Agent interacts with humans | `radical-candor`, `lead-with-empathy` |
| Agent measures outcomes | `rate-of-improvement` |
| Agent runs autonomously | `hitl-and-guardrails`, `autonomy-ladder` |

For each task type, define a prompt template:
```yaml
prompts:
  primary_task_name:
    template: "domain/task_name"
    version: "1.0"
    variant: "default"
```

---

### Step 4: Configure Model Routing

Route by task complexity using provider-neutral profiles:

| Task Type | Recommended Model Profile | Notes |
|---|---|---|
| Classification, extraction | `fast` | High volume, low cost |
| Analysis, variance detection | `balanced` | Structured output |
| Reasoning, recommendations | `deep` | Complex judgment |
| Code generation | `deep` | Correctness matters |

Always define `fallback_profiles`. Always set `timeout_ms`. Map profiles to concrete vendor models in runtime configuration, not in this generic spec.

---

### Step 5: Define Actions by Risk Class

For each action:

| Field | Required? | Notes |
|---|---|---|
| `id` | Yes | snake_case, domain-prefixed |
| `risk_class` | Yes | `low` / `medium` / `high` |
| `autonomy_level` | Yes | Start at L1, promote based on evidence |
| `required_fields` | Yes | Fields the action payload must include |
| `guardrails` | For L2+ | Domain-specific limits |

**Financial data always starts at L1 for recommendations, L2 for execution minimum.**

---

### Step 6: Design HITL Rules

Apply these minimums:

| Risk Class | Rule |
|---|---|
| Low | May auto-execute if confidence ≥ threshold |
| Medium | Approval required; SLA = 4 hours |
| High | Approval required; SLA = 2 hours; senior sign-off |

**For financial, medical, legal, or safety domains:** bump all thresholds by +0.10.

---

### Step 7: Define Cross-Agent Events

For each event:
- **emits:** What signal does this agent send when something notable happens? (e.g., `variance_detected`, `anomaly_flagged`)
- **consumes:** What signals from other agents should trigger a response? (e.g., `ad_spend_anomaly`, `inventory_alert`)

Keep event names short, past-tense, descriptive: `{domain}_{thing}_{event}`.

---

### Step 8: Set the Starting Autonomy Level

**Rule:** All new agents start at L0 or L1. Never design a new agent starting at L3.

Use the autonomy-ladder skill to plan the promotion path. Document:
- What must be true to promote from L1 → L2?
- What triggers automatic demotion?

---

## Output Format

1. Complete `agent-spec.yaml` populated with all sections
2. Capability map table (analysis / recommendations / execution tier)
3. Cross-agent event contract (emits + consumes)
4. HITL rule summary
5. Starting autonomy level and promotion criteria
