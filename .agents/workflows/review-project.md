---
description: how to review a codebase or other project artifact using the agent-kernel principal-operator lens
---

# Review Project Workflow

Use this workflow when reviewing a repository, pull request, design, process document, or other operational artifact.

## Step 1: Establish Context

Define the review target:

- What is being reviewed?
- What system or workflow does it belong to?
- What is the review scope?
- What specific risks or concerns matter most?

If the repository has its own `CONTEXT.md` or `AGENTS.md`, read those first. If not, infer the minimum viable context from the available files.

## Step 2: Choose the Review Lens

Apply the kernel in this order:

1. First Principles: what is this trying to do, at its simplest?
2. PPT: who is affected, what process changes, and what technology assumptions exist?
3. Pareto: which issues matter most to correctness, trust, or throughput?
4. Governance: what decisions or actions need traceability, approvals, or guardrails?
5. Value Stream: is the main impact Revenue, Risk, Cost, or a combination?

## Step 3: Review the Artifact

For code and technical systems, use [`prompts/code-review.md`](../../prompts/code-review.md) as the baseline checklist.

Look for:

- correctness and broken edge cases
- hidden hardcoding or configuration drift
- unclear ownership boundaries
- missing tests or untestable design
- operational risks, cost traps, or reliability gaps
- places where the design violates the system's stated purpose

For non-code artifacts, apply the same structure:

- does it solve the right problem?
- are key assumptions explicit?
- are decision rights and escalation paths clear?
- are success metrics and review cadences defined?

## Step 4: Produce the Review Output

Default output structure:

1. Findings ordered by severity
2. Open questions or assumptions
3. Recommended fixes or next actions
4. Brief summary only after the findings

For each material finding, include:

- why it matters
- what could fail
- what should change
- where the issue exists

## Step 5: Escalate if Needed

Escalate immediately when you find:

- correctness defects that can corrupt output
- security or privacy exposures
- missing approvals around high-risk actions
- identity or governance drift in a digital twin or agent system
- evidence that the artifact cannot be safely deployed as designed

## Step 6: Tie Back to Improvement

End each review with:

- the highest-value next fix
- the expected value stream impact
- any tests, evals, or validation steps required to close the issue
