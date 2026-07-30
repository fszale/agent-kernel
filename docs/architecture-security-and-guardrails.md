# docs/architecture-security-and-guardrails.md

# Architecture, Security & Token Optimization

Direct answer to the second question: **how is security/data-privacy handled, and how is token consumption optimized?**

## Guardrails and human review

Guardrails in this kernel are hard limits, not suggestions — an out-of-envelope action is blocked, not flagged. Every agent/twin role operates inside:

- **Guardrails** — magnitude, rate, scope, risk-class, confidence, and data-freshness limits set before deployment.
- **HITL gates** — low-risk output is automatic; medium/high-risk actions queue for human approval, with the full objective→action chain visible in under 30 seconds.
- **Kill switches** — scoped from global down to a single action class, immediate effect, explicit reactivation only, fully audited.

Full mechanics: [`hitl-and-guardrails`](../skills/hitl-and-guardrails/SKILL.md).

## Data privacy: the contract, in practice

The input/access/output contract described in [`role-scoping-and-data-access.md`](role-scoping-and-data-access.md) is the actual security control — not a policy document sitting next to the system, but the thing that determines what data physically leaves the environment as tokens. Security review starts with one question per role: **does this specific task require this specific data to be sent to a model at all, or can it be resolved locally, redacted, or aggregated first?** Nothing is sent by default; it has to be in the contract.

This is also the seam where the self-hosted question lives — see [`data-sovereignty-and-self-hosted-llms.md`](data-sovereignty-and-self-hosted-llms.md) for the architecture pattern that keeps the proprietary layer off frontier providers entirely.

## Runtime interoperability via MCP

Roles aren't locked to one coding assistant or agent product. When a role needs an additional skill, tool, or action — a specific API call, a specific system integration — MCP (Model Context Protocol) is used where it fits, as the standard way to expose that capability. That's what lets the same tool be reused across ChatGPT (formerly Codex, now merged into the unified ChatGPT app), Claude, Antigravity, Cursor, or a custom goal/loop, instead of rebuilding a bespoke integration per runtime.

That's an interoperability convenience, not the security boundary. The guardrails, HITL gates, and input/access/output contracts described above are enforced by the kernel's own governance design — they don't depend on MCP, and they hold regardless of which protocol a given tool happens to use to connect. MCP just means the reasoning layer on top (which model or IDE is doing the work) is replaceable without rebuilding every tool integration underneath it.

## Token optimization

In production across the deployments described in the role-scoping doc, the effective techniques so far, in combination rather than any single one:

- **Model-per-function routing** — a different model for orchestration, a different model for coding/execution, a different model for final output generation. Not one model doing everything at every step.
- **Selective context assembly** — only the skills, prompts, and metadata relevant to the current task are loaded into context, not the whole kernel.
- **Mandatory revision discipline** — prompts, skills, and metadata are treated as versioned artifacts that get revised on a cadence, not written once and left stale. Context quality degrades silently if this discipline lapses.
- **Caching and prompt compression** where the task shape allows it, and RAG vs. full-context chosen deliberately per task rather than defaulting to one or the other.

One honest caveat worth stating in a client conversation rather than glossing over: model cost and token efficiency are both improving fast and the rate of improvement is itself accelerating. That's an opportunity (today's optimization work keeps paying dividends as models get cheaper) and a challenge (over-fit the architecture to today's model economics and parts of it are stale in two quarters). The contracts and guardrails layer is deliberately built to be model-agnostic for this reason — the governance model doesn't change when the underlying model does.
