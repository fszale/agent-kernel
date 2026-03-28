# Downstream `CLAUDE.md` Template

> Use this in a downstream repository that injects `agent-kernel` for Claude or Claude-style agents.

This repository uses the [agent-kernel](https://github.com/fszale/agent-kernel) as its principal-operator layer.

## Startup

Before doing substantive work:

1. Read this repository's `CONTEXT.md` if present.
2. Read `.agent-kernel/CONTEXT.md`.
3. Read `.agent-kernel/CLAUDE.md`.
4. Read `.agent-kernel/AGENTS.md` for the full skill-selection guide.
5. Load the specific kernel artifact needed for the task.

## Default Review Behavior

When reviewing code, designs, or operational artifacts:

- use `.agent-kernel/.agents/workflows/review-project.md`
- use `.agent-kernel/prompts/code-review.md` for individual code files and snippets
- use `.agent-kernel/prompts/architecture-review.md` for reviewing repositories, system architectures, and multi-agent pipelines
- lead with findings
- order findings by severity
- call out risky assumptions, missing tests, and missing guardrails

## Decision Analysis Behavior

When the task is to assess downstream consequences, systemic ripple effects, or perverse incentives:

- use `.agent-kernel/skills/second-order-effects/SKILL.md`
- use `.agent-kernel/prompts/second-order-effects-analysis.md`
- surface high-severity chains, monitoring indicators, and mitigation thresholds

## Operating Lens

Apply the kernel in this order:

1. People, Process, Technology
2. Pareto
3. 30/60/90
4. Value Stream
5. Rate of Improvement
6. Governance traceability

## Output Expectations

- keep conclusions concrete and evidence-based
- do not bury critical issues under summaries
- prefer explicit next actions over generic advice
