# Prompt: Agent Factory Design

## Purpose
Design a complete agent factory at any evolutionary stage — from Era 1 (single agent) to Era 4 (factory of factories) — with orchestration, event contracts, HITL governance, and mapping of tangible and digital outputs.

## When to Use
- Designing a coordinated multi-agent system for a business
- Planning the evolution path from a pilot agent to a full factory
- Architecting inter-company or inter-domain agent coordination
- Designing the governance model for a hybrid AI + human team

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{factory_name}}` | Name of the factory | "E-commerce Operations Factory" |
| `{{era}}` | Target evolution era (1/2/3/4) | `2` |
| `{{business_context}}` | Industry, size, current operational state | "Mid-size e-commerce brand, 50 employees, 5K orders/day" |
| `{{factory_mandate}}` | What the factory is designed to produce | "Automate order fulfillment, financial reconciliation, and inventory management" |
| `{{human_team}}` | Who the human team is and their roles | "Operations Lead, Finance Lead, 3 ops specialists" |
| `{{constraints}}` | Timeline, budget, or regulatory limits | "Launch within 90 days; must use existing ERP" |

## Prompt

```
You are an agent factory architect. Design a complete factory at the specified evolutionary era.

Factory name: {{factory_name}}
Target era: {{era}}
Business context: {{business_context}}
Factory mandate: {{factory_mandate}}
Human team: {{human_team}}
Constraints: {{constraints}}

## 1. Era Classification and Context
State the era, explain what it means for this factory, and describe the primary challenge to solve at this stage.

## 2. Agent Inventory
Design the agent lineup:
- What domains need an agent?
- What is each agent's primary KPI?
- What is each agent's starting autonomy level?
- What does each agent provide to the factory (analysis / recommendations / execution)?

Format as a table: Agent ID | Domain | Primary KPI | Autonomy Start | Provides

## 3. Orchestrator Design
Specify the coordination layer:
- Routing logic (how tasks get assigned to agents)
- Dependency schedule (which agents must run before others)
- Escalation triggers (what causes work to go to a human)
- Shared state (what the factory remembers across agent runs)
- Budget governance (daily limits, alert thresholds)

## 4. Event Bus Contract
For each significant signal in the factory:
- Event name (snake_case, past tense: {domain}_{entity}_{verb})
- Emitted by: agent ID
- Consumed by: agent IDs or orchestrator
- Required payload fields

Ensure all events include: source_agent_run_id, confidence_score, justification

## 5. Factory HITL Governance
Design escalation rules at the factory level (beyond individual agent HITL):
- Agent conflict resolution
- Budget threshold alerts
- Cross-domain compound decisions
- Kill switch protocols and who can reactivate

For Era 3 (Hybrid): Also document the human expert allocation model:
  - What tasks does each human hand off to the factory?
  - What does the factory never do without explicit human instruction?
  - How does a human's personal AI assistant interact with the shared factory?

For Era 4 (Factory of Factories): Also design:
  - Inter-factory trust protocol (how to verify agent-to-agent messages)
  - Cross-factory HITL gates
  - Dispute resolution process between factories

## 6. Output Mapping (Digital + Tangible)
Map every agent's outputs to:
- Output type (analysis report, recommendation, executed action)
- Value stream (Revenue / Risk / Cost)
- Nature: Digital artifact (data, report, alert, update) OR Tangible result (shipment, payment, fulfilled order, product)

Show how digital outputs chain into tangible results.

## 7. 30/60/90 Factory Launch Plan
Using the 30/60/90 framework:
- 30 days: What is the Era 1 version (minimum viable factory)?
- 60 days: What agents get added? What autonomy levels get promoted?
- 90 days: What does the full factory look like at steady state?

## 8. Rate of Improvement Plan
- What is the factory's primary metric baseline?
- How is the S-curve measured at the factory level (not per-agent)?
- What does "factory graduation" look like — the point where the factory is self-optimizing?
```

## Expected Output
- Era classification and factory mandate
- Agent inventory table (with autonomy starting levels)
- Orchestrator spec
- Event bus contract (all events documented)
- HITL governance table
- Digital + tangible output mapping
- 30/60/90 launch plan
- Rate of Improvement measurement plan

## Tips
- Never design Era 4 for a client who hasn't shipped Era 2
- Always start new agents at L0 or L1 — never at L3
- For Era 3, the personal AI layer is as important as the shared factory layer
- For Era 4, the trust protocol is more important than the feature set
