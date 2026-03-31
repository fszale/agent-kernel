---
description: how to produce an outcome-driven review package for a proposed or existing solution using the agent-kernel
---

# Review Solution Package Workflow

Use this workflow when a team needs more than a review memo. This workflow produces a reusable package of Markdown artifacts that define:

- the desired outcome
- the current state
- the target state
- the gap analysis
- the implementation plan
- the evaluation plan

If the request is only for defects or findings, use [`review-project.md`](./review-project.md).

## Step 1: Establish the Outcome

Define:

- what the team wants to achieve
- who benefits
- what metric proves the outcome
- what decision is being requested

If the team is presenting a design without a clear outcome, make that the first finding.

## Step 2: Establish the Current State

Document:

- what exists today
- what is real vs. assumed vs. simulated
- what baseline metrics already exist
- what process or product behavior is currently happening

## Step 3: Identify the Gap

Use the `solution-review-package` skill and relevant supporting skills:

- `agentic-system-review`
- `staged-validation`
- `governance-hierarchy-design`
- `rate-of-improvement`
- `second-order-effects`

Map gaps across:

- outcome clarity
- process readiness
- technical readiness
- governance
- measurement

## Step 4: Produce the Artifact Bundle

Write these Markdown files using the templates:

1. `review-summary.md` → `templates/review-summary-template.md`
2. `gap-analysis.md` → `templates/gap-analysis-template.md`
3. `implementation-plan.md` → `templates/implementation-plan-template.md`
4. `evaluation-plan.md` → `templates/evaluation-plan-template.md`

## Step 5: Finish With Direct Guidance

End the package with:

- highest-value next action
- key open questions
- explicit go / no-go or proceed-with-conditions recommendation
