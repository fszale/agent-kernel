# docs/role-scoping-and-data-access.md

# Role Scoping & Data Access

This is a direct answer to one question: **what roles have actually been built with this kernel, and what does the data ingestion/access model look like for each?**

Not a hypothetical framework — three live deployments, in order of how agentic they are.

## 1. 150-person engineering organization — Architect twin

A version of this kernel is deployed inside a 150-person engineering org. Team members use it two ways: manually, to review their own projects from multiple perspectives, and as part of automated GitHub workflows that run the same review on every PR.

In this deployment the twin plays a single, narrow role: **Architect**. It reviews code and design decisions against the kernel's PPT / first-principles / governance lenses (see [`solution-review-package`](../skills/solution-review-package/SKILL.md) and [`architecture-review.md`](../prompts/architecture-review.md)) and produces a review — it does not merge, deploy, or modify anything itself. Read-only by construction.

## 2. Personal factory instance — Advisor twin

In Filip's own agent factory, the twin's role is **Advisor**, not operator. It supervises the outputs of other agents in the factory, watches observed activity over time, and surfaces recommendations for improvement. It sits one layer above execution — closer to a chief-of-staff function than to a worker agent.

## 3. Amazon seller business — fully agent-run factory

This is the deepest deployment: an entire operating business run by a factory of digital twins, each scoped to one functional role:

| Role | Function |
|---|---|
| Director (COO) | Overall coordination, priority-setting across the other agents |
| Marketer | Campaign and listing strategy |
| Inventory Manager | Stock levels, reorder timing |
| Sales Agent | Pricing and sales execution |
| Business Analyst | Competitive and product analysis |
| Optimizer | Cross-cutting performance tuning |
| (additional roles) | Added as the business needs them |

Each role is a separate twin with its own scope — not one generalist agent wearing different hats. This is the pattern [`domain-agent-design`](../skills/domain-agent-design/SKILL.md) and [`agent-spec-domain-template.yaml`](../templates/agent-spec-domain-template.yaml) exist to formalize.

## In progress

A twin focused on originating unique data products is under active development. Early-stage — not yet a reference pattern.

## The data access model: input/access/output contracts

This is the governed part, and it's the same across all three deployments above: **data security comes first — every twin/agent has an explicit input/access/output contract**, not open-ended access to whatever it can reach.

In practice, a contract answers three questions per role, before the role is ever turned on:

1. **Input** — exactly which data sources this role is allowed to read (a specific repo, a specific product catalog, a specific ledger — never "everything").
2. **Access** — what it's allowed to *do* with that data (read-only analysis vs. propose-only recommendation vs. execute-with-approval — see [`hitl-and-guardrails`](../skills/hitl-and-guardrails/SKILL.md) for the approval-gate mechanics).
3. **Output** — what it's allowed to emit, and to whom (a report to a human, an event to another agent, a state-changing action).

In a custom-built factory, each contract is implemented as an MCP (Model Context Protocol) server — one governed connector per data source or tool, rather than access logic re-implemented inside every agent. That's also what lets a role be driven by whichever runtime fits the task (ChatGPT, Claude, Antigravity, Cursor, or a custom goal/loop) without changing what that role is allowed to see or do — see [`architecture-security-and-guardrails.md`](architecture-security-and-guardrails.md) for the enforcement mechanics.

The reason this matters more than the role list itself: the contract is what decides what actually crosses the wire to a model provider. That's the hinge point for the architecture and data-sovereignty questions — see [`architecture-security-and-guardrails.md`](architecture-security-and-guardrails.md) and [`data-sovereignty-and-self-hosted-llms.md`](data-sovereignty-and-self-hosted-llms.md).
