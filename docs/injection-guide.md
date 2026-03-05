# docs/injection-guide.md

# Injection Guide

How to use the agent-kernel in any downstream project.

## What "Injection" Means

"Injecting" this kit means making its skills, prompts, and templates available to AI agents working on your project. The kit does not run standalone — it is a shared knowledge library referenced by other projects.

## Method 1: Git Submodule (Recommended)

Add the kernel as a submodule in your project:

```bash
git submodule add https://github.com/fszale/agent-kernel .agent-kernel
git submodule update --init --recursive
```

Reference skills and prompts from `.agent-kernel/skills/` and `.agent-kernel/prompts/` in your `CONTEXT.md` and `AGENTS.md`.

## Method 2: Direct Copy

Copy specific files into your project:

```bash
# Copy just the skills you need
cp -r .agent-kernel/skills/governance-hierarchy-design/ .agents/skills/
cp .agent-kernel/prompts/action-proposal.md .agents/prompts/

# Copy templates
cp .agent-kernel/templates/agent-spec-template.yaml ./
```

This approach is easier but requires manual updates when the kernel improves.

## What to Configure in Your Project

### 1. Create `CONTEXT.md`

Use the kernel's `CONTEXT.md` as a starting template, then customize for your project's directory structure and vocabulary.

### 2. Create `AGENTS.md`

Reference the kernel's `AGENTS.md` for the skill selection guide, then add project-specific agent activation rules.

### 3. Create `agent-config.yaml`

Use `templates/agent-config-template.yaml` as your starting point. Configure:
- Guardrail limits appropriate for your domain(s)
- HITL approval rules matching your team's capacity
- Autonomy levels for each action class (start at L1 for all)

### 4. Create agent specs

Use `templates/agent-spec-template.yaml` for each agent in your system. Pay attention to:
- `discovery.capabilities` — this enables agent routing
- `decision_rationale.universal_required_fields` — must include `justification` and `reasoning_summary`
- `actions` — start with L1 autonomy and promote from there

## Activation in `.agents/workflows/`

Copy (or link) the relevant `.agents/workflows/` files into your project to give AI agents access to the standard procedures:
- `add-skill.md` — so agents can create new skills in your project
- `run-consistency-check.md` — so agents can audit your project
- `inject-into-project.md` — for projects that further inject the kernel

## GitHub Actions Setup

To use the CI quality gates in your project:

1. Copy `.github/workflows/` from the kernel
2. Set `GEMINI_API_KEY` in your repository secrets
3. Adjust workflow triggers and thresholds as needed

## After Injection: First Steps

1. Run `/run-consistency-check` to establish baseline
2. Set up your first agent spec using `agent-spec-template.yaml`
3. Configure your first guardrails using `agent-config-template.yaml`
4. Start all new agents at L0 (Observe) or L1 (Recommend) autonomy

## Contact and Support

See `docs/contributing.md` to propose improvements to the kernel that benefit all downstream projects.
