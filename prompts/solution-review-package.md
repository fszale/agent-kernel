# Prompt: Solution Review Package

## Purpose

Review a proposed or existing product, framework, workflow, or agentic system and produce a package of reusable Markdown artifacts that define the desired outcome, current state, gap analysis, implementation plan, and evaluation plan.

## When to Use

- When a team is asking for feedback on a proposal and appears to be jumping straight to implementation
- When reviewing an existing project that lacks a clear validation path
- When you want a package of artifacts a team can use to align, learn, implement, and measure progress

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{review_target}}` | The project, proposal, or repo being reviewed | "A multi-agent support automation prototype" |
| `{{desired_outcome}}` | The outcome the team says it wants | "Reduce Tier-1 manual handling by 40% without hurting CSAT" |
| `{{current_state}}` | What exists today | "Prototype with orchestration and mock QA, no baseline metrics" |
| `{{stakeholders}}` | Key people or roles affected | "Support lead, platform team, operations manager" |
| `{{constraints}}` | Constraints that must hold | "No irreversible actions, must use existing CRM, 8-week window" |
| `{{artifact_location}}` | Where the review package should be written | "`artifacts/review-package/`" |

## Prompt

```
Please review the adjacent project using the agent-kernel.

Review target: {{review_target}}
Desired outcome: {{desired_outcome}}
Current state: {{current_state}}
Stakeholders: {{stakeholders}}
Constraints: {{constraints}}
Artifact location: {{artifact_location}}

Use the `solution-review-package` skill as the primary frame.

Also draw on:
- `agentic-system-review` for system and architecture gaps
- `staged-validation` for depth-first sequencing
- `governance-hierarchy-design` for traceability
- `rate-of-improvement` for measurement design
- `second-order-effects` where downstream effects matter

Your job is to produce a reusable review package of Markdown artifacts.

The package must:
1. Reframe the work in terms of the desired outcome, not just the proposed implementation
2. Define the current state and target state clearly
3. Identify the gaps between the two
4. Provide a practical implementation plan
5. Provide an evaluation plan that proves whether the proposed solution is reaching the desired objective over time
6. Call out unknowns, assumptions, and highest-value next actions

Write these artifacts:
- `review-summary.md`
- `gap-analysis.md`
- `implementation-plan.md`
- `evaluation-plan.md`

Use the corresponding templates from `templates/`.

If the current state, baseline, or target outcome is unclear, make that a first-class finding rather than guessing it away.
```

## Expected Output

- `review-summary.md` with the verdict and package manifest
- `gap-analysis.md` covering current state, target state, and readiness gaps
- `implementation-plan.md` with a phased, outcome-driven plan
- `evaluation-plan.md` with baseline, metrics, instrumentation, review cadence, and go/no-go gates

## Tips

- Prefer systems over goals: focus on the mechanisms that will reliably produce the outcome
- If the team is trying to validate too many things at once, reduce scope to the core value claim
- If an `agentic-playbook` repo is available, use its implementation/gap-analysis guides as helper context
