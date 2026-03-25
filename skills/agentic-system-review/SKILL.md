---
name: agentic-system-review
description: Audit a multi-agent system architecture for gaps in state durability, self-improvement loops, memory/context design, HITL gates, and agent contracts.
when-to-use: Use when evaluating an existing or proposed agentic pipeline to identify architectural risks, missing feedback loops, and readiness gaps before production adoption or team handoff.
principles: [First Principles, Governance Hierarchy, HITL and Guardrails, Rate of Improvement, Configuration-Driven Design]
---

# Agentic System Review Skill

## Purpose

Produce a structured gap analysis of a multi-agent system across five dimensions: state durability, self-improvement, memory/context, human-in-the-loop, and agent contracts. Output findings ordered by severity with actionable next steps and a highest-value fix recommendation.

## Agent Instructions

Apply the `/review-project` workflow with this agentic-specific lens layered on top.

---

### Step 1: Map the System

Before evaluating gaps, establish the baseline:

1. **List every agent** — name, port/endpoint, primary responsibility
2. **Trace the data flow** — what triggers each agent, what it produces, where output goes
3. **Identify the LLM touchpoints** — which decisions are model-driven vs. rule-driven
4. **Note what is real vs. simulated** — explicitly flag any simulated components masquerading as production behavior

---

### Step 2: Evaluate the Five Dimensions

For each dimension, rate current state as: `✅ Implemented` / `⚠️ Partial` / `❌ Missing`

#### A. State Durability
- Is agent/task state persisted beyond process memory?
- Can a crashed pipeline resume from its last checkpoint?
- Is there a task/job store backed by a real database?

#### B. Self-Improvement Loop
- Are LLM decisions logged with outcomes?
- Is there any feedback path from downstream results (QA, monitoring) back to upstream prompts?
- Are prompt versions tracked? Is there evidence of prompt performance measurement?
- Are successful artifacts (e.g., generated code, configurations) reused as seeds for future runs?

#### C. Memory and Context Management
- What context does each agent receive before an LLM call?
- Is historical decision data injected as few-shot context?
- Is there a shared memory bus or cross-agent context store?
- Are agent-generated artifacts (reports, verdicts, code) read back anywhere?

#### D. Human-in-the-Loop
- Are there explicit HITL gates for high-risk decisions (decommission, data deletion, irreversible actions)?
- Is there an alert/notification mechanism for operators?
- Can a human pause, approve, or override an agent action?
- Is there a dashboard or API that gives operators real-time visibility?

#### E. Agent Contracts
- Does each agent have a versioned API spec?
- Does each agent have a `SKILL.md` or equivalent describing inputs, outputs, and behavior?
- Are integration boundaries explicit, or are agents tightly coupled?

---

### Step 3: Identify the Simulation Boundary

A common risk in early agentic systems is **simulation drift** — parts of the pipeline that appear real but are mocked.

For each agent, answer:
- Is the input real or simulated?
- Is the processing real or simulated?
- Is the output persisted to a real store or dropped?

Document the simulation boundary clearly. Any component that is 100% simulated is not validatable and should not be included in production architecture claims.

---

### Step 4: Score and Rank Findings

Rate each finding:

| Severity | Definition |
|---|---|
| 🔴 Critical | Can corrupt output, cause unrecoverable failure, or represents a false production claim |
| 🟠 High | Will block adoption or cause repeated failures at scale |
| 🟡 Medium | Reduces efficiency or increases cost; addressable in next sprint |
| 🟢 Low | Quality-of-life improvement; backlog candidate |

---

### Step 5: Identify the Highest-Value Next Fix

Apply Pareto reasoning: which single fix unblocks the most subsequent improvements?

Common answers:
- **Durable state store** — unblocks crash recovery, cross-run context injection, and HITL pause/resume
- **Real integration for the core agent** — unblocks actual validation of the pipeline's primary value claim
- **Shared decision memory** — unblocks self-improvement loop for all downstream LLM calls

---

## Output Format

1. **System map** — agents, data flow, LLM touchpoints, simulation boundary
2. **Dimension scores** — A through E, rated and explained
3. **Findings table** — severity / finding / location / recommended fix
4. **Highest-value next fix** — one recommendation with value stream impact
5. **Advisory framing** — for teams: where to go deep before going wide
