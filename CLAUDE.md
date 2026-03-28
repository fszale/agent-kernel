# CLAUDE.md — Agent Kernel Entry Point

> This file is for Claude or Claude-style agents working in any project that injects the agent-kernel. Read `CONTEXT.md` first, then use this file as the activation guide.

## Purpose

`agent-kernel` is not a standalone runtime. It is an injectable principal-operator layer containing skills, prompts, templates, and workflows that should shape how you reason and operate inside another repository.

## Startup Sequence

When this kernel is available in a project:

1. Read `CONTEXT.md` to understand the project map and contribution rules.
2. Read `AGENTS.md` for the full skill-selection guide and activation hierarchy.
3. Use the relevant `skills/*/SKILL.md`, `prompts/*.md`, `templates/*.md`, or `.agents/workflows/*.md` artifact for the task at hand.

## Default Operating Lens

Run through this chain in order before acting:

1. PPT Analysis: Who is affected? What process changes? What technology enables it?
2. Pareto Filter: Which 20% of work delivers 80% of the value?
3. 30/60/90 Timeline: What is Immediate, Soon, or Later?
4. Value Stream: Does this drive Revenue, reduce Risk, or save Cost?
5. Rate of Improvement: How will success improve over time?
6. Governance: Does this require objective-to-action traceability?

## Common Task Routing

| If you need to... | Use... |
|---|---|
| Evaluate an idea or initiative | `skills/idea-evaluator/SKILL.md` + `prompts/idea-evaluator.md` |
| Plan a project or roadmap | `skills/30-60-90-planning/SKILL.md` + `templates/30-60-90-plan-template.md` |
| Diagnose a failure or constraint | `skills/firefighter/SKILL.md` or `skills/first-principles/SKILL.md` |
| Design an agent or multi-agent system | `skills/domain-agent-design/SKILL.md` or `skills/agent-factory-design/SKILL.md` |
| Review another repo or artifact | `.agents/workflows/review-project.md` + `prompts/architecture-review.md` |
| Review a multi-agent system | `skills/agentic-system-review/SKILL.md` + `prompts/architecture-review.md` |
| Plan R&D staged validation | `skills/staged-validation/SKILL.md` + `prompts/architecture-review.md` |
| Assess downstream or systemic consequences | `skills/second-order-effects/SKILL.md` + `prompts/second-order-effects-analysis.md` |

## Review Mode

When reviewing code, documents, or system artifacts:

- lead with findings, not summary
- order findings by severity
- use concrete file or artifact references
- call out missing tests, missing guardrails, and risky hidden assumptions
- apply First Principles and PPT, not style preferences

## Consistency Rules

All generated content should preserve the kernel rules:

- strategies and actions must be traceable
- outputs should be tagged to Revenue, Risk, and/or Cost where material
- significant recommendations should address People, Process, and Technology impact
- prompts must use `{{variable_name}}` format
- new skills must include required frontmatter

## Cross-Reference

Use [AGENTS.md](AGENTS.md) as the detailed operating guide and [PHILOSOPHY.md](PHILOSOPHY.md) when a decision requires principle-level grounding.
