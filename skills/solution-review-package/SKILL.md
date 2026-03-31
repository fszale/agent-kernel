---
name: solution-review-package
description: Review a proposed or existing product, workflow, or agentic solution by defining the desired outcome, current state, target state, gap analysis, implementation plan, and evaluation plan as a reusable artifact bundle.
when-to-use: Use when a team is eager to build or scale a solution but has not clearly defined the outcome, baseline, validation path, or readiness gaps. Use when you want a review package a team can use to learn, align, implement, and measure success over time.
principles: [Systems Over Goals, First Principles, Governance Hierarchy, Rate of Improvement, People Process Technology, Pareto, 30/60/90]
---

# Solution Review Package Skill

## Purpose

Turn a proposed or existing solution into an outcome-driven review package that a team can act on immediately.

The review package must answer five questions:

1. What outcome is this solution supposed to create?
2. What is true today?
3. What gap exists between today and the desired outcome?
4. What should be built or changed first?
5. How will the team know the solution is actually working over time?

## Agent Instructions

If an adjacent `agentic-playbook` repository exists, use these guides as helper context:

- `guides/engineering/implementation-execution-gap-analysis.md`
- `guides/engineering/analysis-gap-traceability.md`

Use them to reinforce the three-phase pattern:

- define the plan
- execute against the plan
- validate against the target state

### Step 1: Reframe the Work in Outcome Terms

Before reviewing architecture or implementation details, define:

- the desired business or operational outcome
- the primary beneficiary
- the primary value stream: Revenue, Risk, Cost, or a combination
- the decision the team is implicitly asking permission to make

If the team is presenting a go-forward design without a clear outcome, call that out explicitly.

### Step 2: Establish Current State

Document what exists today:

- current workflow, process, or product behavior
- current implementation maturity
- current bottlenecks or failure modes
- current baseline metrics, if any
- what is real vs. assumed vs. simulated

If the current state is under-documented, treat that as a gap, not as permission to skip it.

### Step 3: Define the Target State

Describe the future state in measurable terms:

- what “working” looks like
- which metric proves it
- which leading indicators suggest progress
- what constraints must still hold true

Require at least one primary outcome metric and at least two supporting metrics.

### Step 4: Perform the Gap Analysis

Map the difference between current state and target state across:

- outcome clarity
- user and stakeholder alignment
- process readiness
- technical readiness
- data and memory readiness
- eval and measurement readiness
- governance, HITL, and approval readiness

Separate:

- confirmed gaps
- assumptions
- unknowns that block confidence

### Step 5: Build the Implementation Plan

Translate the review into a pragmatic plan:

- immediate / soon / later horizons
- highest-value first
- prerequisites and dependencies
- acceptance criteria
- explicit risks and mitigations

Prefer depth before breadth. If the team is trying to validate too many things at once, narrow the plan to the smallest slice that proves the core value claim.

### Step 6: Build the Evaluation Plan

The evaluation plan must include:

- baseline definition
- primary outcome metric
- leading indicators
- review cadence
- go/no-go checkpoints
- failure signals that should trigger redesign

Do not accept “we will know by feel” as an evaluation plan.

### Step 7: Produce the Artifact Bundle

Produce a package of Markdown artifacts using these templates:

- `templates/review-summary-template.md`
- `templates/gap-analysis-template.md`
- `templates/implementation-plan-template.md`
- `templates/evaluation-plan-template.md`

Default file set:

1. `review-summary.md`
2. `gap-analysis.md`
3. `implementation-plan.md`
4. `evaluation-plan.md`

## Output Requirements

Every review package must include:

- explicit desired outcome
- explicit current state
- explicit target state
- explicit gap analysis
- explicit implementation sequence
- explicit evaluation and measurement plan
- highest-value next action
- open questions that still require human judgment

If any of those are missing, the review is incomplete.

## Output Format

Produce a package of Markdown artifacts:

1. `review-summary.md` — decision framing, verdict, artifact manifest, open questions
2. `gap-analysis.md` — current state, target state, confirmed gaps, assumptions, risks
3. `implementation-plan.md` — phased work, dependencies, decision points, definition of done
4. `evaluation-plan.md` — baseline, metrics, instrumentation, review cadence, go/no-go gates
