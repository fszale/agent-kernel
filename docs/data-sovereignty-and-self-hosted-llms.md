# docs/data-sovereignty-and-self-hosted-llms.md

# Data Sovereignty & Self-Hosted LLMs

## The thesis

The proprietary value in an agentic deployment isn't the model. It's the captured business intelligence that makes a generic model good at *this* business: the skills, notes, prompts, decision frameworks, and input/access/output contracts described in [`role-scoping-and-data-access.md`](role-scoping-and-data-access.md). That layer is the actual alpha — it took real operating experience to build, and it's what turns a frontier model from a generalist into something that plays Architect, Advisor, or COO for a specific organization.

Every time that layer is sent to a third-party frontier model as tokens, two risks are taken on regardless of the provider's stated policies: the proprietary context becomes an input the provider handles at scale, and the business becomes dependent on a provider whose pricing, weights, and terms it doesn't control. Neither risk requires bad faith from the provider — it's a structural property of routing proprietary reasoning through someone else's infrastructure.

## External validation

This isn't a fringe concern. In late June 2026, Palantir CEO Alex Karp made this argument publicly and directly: enterprises using frontier models are, in his words, "livid" that they're paying for tokens while the same interaction pipeline extracts their proprietary operating data. He framed the alternative — enterprises controlling their own weights, data, and business logic — as the reason for Palantir's NVIDIA partnership. The market response (a same-day stock move) suggests this framing is resonating well beyond one company's talking points.

Sources: [Palantir CEO Alex Karp: Enterprises Are "Livid" Over AI Models That "Steal" Their Business Value (247wallst.com)](https://247wallst.com/investing/2026/07/01/palantir-ceo-alex-karp-enterprises-are-livid-over-ai-models-that-steal-their-business-value/), [Palantir CEO Alex Karp Says AI Labs Are Chasing 'Tokens' While Enterprises Fear for Their IP (Yahoo Finance)](https://finance.yahoo.com/technology/ai/articles/palantir-ceo-alex-karp-says-223226928.html), [Karp Says Frontier AI Labs Are Stealing Enterprise Value And VCs Are Listening (Forbes)](https://www.forbes.com/sites/josipamajic/2026/07/02/karp-says-frontier-ai-labs-are-stealing-enterprise-value-and-vcs-are-listening/)

## The architecture pattern

The contract model already in production (see [`architecture-security-and-guardrails.md`](architecture-security-and-guardrails.md)) is what makes this a natural extension rather than a rebuild — it already decides what data is allowed to cross the wire for any given task. Self-hosting adds a third layer underneath that decision, not a replacement for it:

1. **Proprietary context layer** — skills, notes, prompts, decision frameworks, and historical outcomes. Versioned and stored entirely within the client's own infrastructure. Never transmitted anywhere as training-eligible data.
2. **Governance layer** — the existing input/access/output contracts and guardrails (see [`architecture-security-and-guardrails.md`](architecture-security-and-guardrails.md)). Decides, per task, what data (if any) is allowed to leave the proprietary layer, and which sensitivity tier applies.
3. **Reasoning substrate, tiered by sensitivity** — not a single all-or-nothing choice:
   - **Tier 1 (low-sensitivity, e.g. boilerplate, public-facing drafts):** frontier models, used freely — through ChatGPT, Claude, Antigravity, Cursor, or whichever runtime fits the task.
   - **Tier 2 (business-sensitive):** private or dedicated model deployments with contractual data-use guarantees.
   - **Tier 3 (core proprietary alpha):** self-hosted or open-weight models, running on infrastructure the client controls, so the most valuable context never leaves the building.

The tier is enforced by the kernel's own governance layer, not by whichever coding assistant or agent product is doing the reasoning — so the client isn't locked into one vendor to get this. The same contracts and guardrails apply whether the goal/loop is being driven through ChatGPT, Claude, Antigravity, Cursor, or a fully custom factory; MCP is used underneath, where it fits, to expose additional skills/tools/actions to whichever runtime is attached, not to enforce the tier itself.

Today's production deployments (the 150-person engineering org, the personal factory, the Amazon-seller agent factory) run primarily on frontier models — GPT, Opus, Fable-class models — for the reasoning substrate, which is exactly why the outcomes have been strong: frontier models are currently the best available reasoning engines. The sovereignty pattern above doesn't argue against using them; it argues for controlling *which* data reaches them, tier by tier, so the business captures the upside of frontier-model reasoning without surrendering the proprietary layer that makes the whole system valuable in the first place.

## What this means for a commercial engagement

This is the actual strategic question worth a working session, not a slide deck: for a given client's proprietary knowledge base, what belongs in Tier 3 versus Tier 1/2, and what does the self-hosted or dedicated-deployment substrate need to look like to make Tier 3 practical without giving up the velocity gains frontier models currently provide.
