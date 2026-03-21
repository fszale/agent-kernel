# Downstream `AGENTS.md` Template

> Use this in a downstream repository that injects `agent-kernel` for Codex or other `AGENTS.md`-aware agents.

Read `.agent-kernel/CONTEXT.md` first, then `.agent-kernel/AGENTS.md`.

## Agent Kernel

This repository uses the [agent-kernel](https://github.com/fszale/agent-kernel) as its principal-operator layer.

Use the kernel for:

- strategic planning
- system and agent design
- code and artifact review
- governance, HITL, and autonomy decisions

## Required Startup

Before doing substantive work:

1. Read this repository's `CONTEXT.md` if present.
2. Read `.agent-kernel/CONTEXT.md`.
3. Read `.agent-kernel/AGENTS.md`.
4. Load the specific skill, prompt, template, or workflow required for the task.

## Review Tasks

When asked to review code, architecture, or other artifacts:

- use `.agent-kernel/.agents/workflows/review-project.md`
- use `.agent-kernel/prompts/code-review.md` for code and technical design review
- present findings first, ordered by severity
- include file references and missing tests
- apply First Principles and PPT before proposing refactors

## Consistency Rules

- maintain objective-to-action traceability where strategy or execution is proposed
- tag material recommendations to Revenue, Risk, and/or Cost
- address People, Process, and Technology impact for significant changes
- default new autonomous actions to low autonomy unless the repo explicitly says otherwise
