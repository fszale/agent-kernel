---
name: tactic-design
description: Design action bundles (tactics) where multiple actions share a logical dependency and must be executed together to achieve the intended outcome. Distinguish bundling necessity from convenience grouping.
when-to-use: Use when an agent is proposing multiple related actions. Use when two or more actions from different domains must be coordinated. Use to review proposed action groups for bundling validity.
principles: [Governance Hierarchy, Tactic Design, Traceability]
---

# Tactic Design Skill

## Purpose

Group actions into coherent tactics only when they share genuine logical dependency. Tactics enable coordinated execution and protect the intent behind bundled actions.

## Agent Instructions

You are a tactic architect for multi-agent operational systems.

### Core Principle

A tactic is a bundle of actions where the **combined effect is greater than or different from the sum of individual effects**. If you can't articulate WHY they must happen together, they don't belong in a tactic.

### When to Bundle

Bundle when actions have TRUE logical dependency:

| Type | Signal | Example |
|---|---|---|
| **Sequential dependency** | Action B only makes sense if Action A completes first | Cut budget on Campaign X → immediately reallocate that freed budget to Campaign Y |
| **Risk mitigation** | Individual actions are higher risk; together they offset each other | Reduce price → simultaneously increase volume-driving activity |
| **Timing sensitivity** | Both must happen within the same window or adverse effects occur | Pause one process → redirect capacity to another before the window closes |
| **Cross-domain coordination** | Two different agents/domains must act in sync | Inventory reorder + associated content pause to avoid stockout |

### When NOT to Bundle

| Anti-Pattern | Problem |
|---|---|
| **Independence** | Actions target different objectives with no interaction — keep them separate |
| **Convenience grouping** | Happen to be proposed at the same time but have no logical relationship |
| **Single action** | By definition, one action is not a tactic |
| **Unclear intent** | If you can't articulate the WHY in one sentence, don't bundle |

### Writing a Strong Intent Field

The `intent` field is what a human approver reads to decide whether to approve the entire bundle.

**Strong intent template:**
> "[Action A description] and [Action B description] must happen together because [specific causal reason]. Doing A without B would result in [negative outcome]. Doing B without A would result in [other negative outcome]. Together, they achieve [combined goal] which advances [strategy]."

**Bad examples:**
- "Optimize performance" (too vague)
- "Group of related actions for this week" (convenience grouping)
- "Changes to improve the system" (no dependency articulated)

### Tactic Patterns

| Pattern | When to Use | Actions |
|---|---|---|
| **Cut-and-Redirect** | Freeing resources in one area to deploy elsewhere | Reduce/stop X → immediately increase/start Y |
| **Test-then-Scale** | Validate before full commitment | Small controlled test → evaluate → full rollout |
| **Prepare-then-Launch** | Prerequisites before main action | Prepare/update A → then launch B |
| **Defensive Bundle** | Multiple moves to protect a position simultaneously | Hold price + increase defense + remove waste |
| **Cross-Domain Sync** | Agents from different domains must coordinate | Action from Agent A + Action from Agent B in same window |

### Execution Mode Selection

- **Sequential** — order matters; later actions depend on earlier ones completing
- **Parallel** — all actions should happen simultaneously to maximize combined effect
- **Phased** — natural stages (prepare / execute / measure) with defined gates between phases

### Approval Rules for Tactics

Tactics are approved **all-or-nothing**:
- ✅ Approve all — all actions execute in the defined mode
- ❌ Reject all — no actions execute; agent receives the rejection rationale
- No cherry-picking individual actions from a tactic

This rule preserves the logical dependency that justified bundling.

## Output Format

Tactic design record:
1. Tactic title and type (which pattern)
2. Constituent actions (ID, description, risk class each)
3. Dependency type (sequential/risk-mitigation/timing/cross-domain)
4. Intent field (strong statement of WHY bundled — see template above)
5. Execution mode with rationale
6. Combined expected value + combined risk class
7. Strategy alignment (HOW this tactic executes the linked strategy)
