---
name: staged-validation
description: Design a phased go/no-go validation roadmap for R&D or platform teams building systems that will be adopted by multiple downstream teams.
when-to-use: Use when an R&D group has a working prototype and needs a structured path from proof-of-concept to production-ready platform, with clear success criteria at each stage.
principles: [Bias Towards Action, Governance Hierarchy, Rate of Improvement, First Principles, HITL and Guardrails]
---

# Staged Validation Skill

## Purpose

Convert a prototype or incomplete architecture into a sequenced validation roadmap. Each phase has a focused scope, explicit success criteria, and a go/no-go gate. Prevents R&D teams from scaling prematurely or building breadth before depth.

## Agent Instructions

---

### Step 1: Identify the Core Value Claim

Before designing phases, extract the system's **primary value claim** — the one thing it must do reliably for adoption to make sense.

Ask:
1. What is the single agent or mechanism most novel and differentiated in this system?
2. If only one component worked end-to-end against a real target, which delivers the most value?
3. What failure mode would make downstream teams abandon adoption?

The component that answers all three questions is Phase 1.

**Pareto principle:** Validate the 20% of the system that delivers 80% of the value before building the remaining 80%.

---

### Step 2: Design the Phase Structure

Each phase follows this pattern:

```
Phase N
  Focus:    [single agent or capability pair]
  Scope:    [what is real vs. still simulated]
  Gate:     [measurable success criteria — numbers, not feelings]
  Output:   [what artifact or signal proves the gate was met]
  Decision: [go / no-go / iterate]
```

**Standard phase sequence for agentic systems:**

| Phase | Typical Focus | Gate Example |
|---|---|---|
| 1 | Core agent — real input, real output | Agent produces valid output for ≥3 real targets with <N retries avg |
| 2 | Orchestrator + core agent — end-to-end | Natural language prompt → stored data in <X minutes reliably |
| 3 | Add resilience layer (monitoring/healing) | Measurable reduction in failure rate vs. baseline |
| 4 | Add validation layer (QA/audit) | Output accuracy meets defined threshold; feedback loop active |

Adapt phase count and focus to the specific system. Never add a new phase before the previous gate is met.

---

### Step 3: Define Platform Foundations

For systems that will be consumed by multiple teams, identify the **platform foundations** that must be hardened early — regardless of which phase the team is in:

| Foundation | Why It Can't Wait |
|---|---|
| **Durable state** | Teams cannot adopt a system whose task state is lost on restart |
| **Agent contracts** | Teams cannot integrate against agents with undocumented or unstable APIs |
| **Versioned prompts** | Teams cannot trust a system whose behavior changes without notice |
| **Basic HITL gate** | Teams cannot deploy a system that can't be stopped or overridden |

These are not Phase 4 concerns. They are Phase 1 prerequisites for platform readiness.

---

### Step 4: Define the Feedback Loop Per Phase

Each phase must produce a **learning signal** — not just a pass/fail:

| Signal Type | Example |
|---|---|
| Performance metric | Avg LLM retries per job, success rate per target |
| Quality metric | QA pass rate, field mismatch count |
| Cost metric | LLM calls per task, tokens per decision |
| Reliability metric | Crash recovery rate, uptime |

Instrument the signal in Phase 1. Don't retrofit observability.

---

### Step 5: Advise on Depth vs. Breadth

R&D teams building platforms are often tempted to demonstrate breadth (all agents working at once) over depth (one agent working perfectly).

**Advise depth first when:**
- The system is being presented for adoption by other teams
- Any component is still simulated
- Success criteria are not yet measured with real data
- The team cannot answer: "What is our baseline failure rate?"

**Breadth becomes appropriate when:**
- Phase 1 gate has been met and documented
- At least one downstream team has integrated Phase 1
- The team can demonstrate a real feedback loop (not a demo loop)

---

### Step 6: Write the Advisory Summary

Produce a summary suitable for sharing with the R&D team and their stakeholders:

1. **Reframe statement** — what the team is actually building (platform vs. demo)
2. **Phase table** — scope, gate, output for each phase
3. **Platform foundations** — what to harden regardless of phase
4. **Depth vs. breadth guidance** — one-line principle the team can repeat
5. **Immediate next actions** — 3–5 specific, executable items for their next sprint

---

## Output Format

1. Core value claim (one sentence)
2. Phase roadmap table (Phase / Focus / Gate / Output / Decision)
3. Platform foundations checklist
4. Feedback loop design per phase
5. Advisory summary (shareable with team and stakeholders)
