---
description: how to inject the agent-kernel into a downstream project
---

# Inject Into Project Workflow

Follow these steps to inject the agent-kernel into a downstream project.

## Step 1: Add reference to the kernel

In the downstream project's `CONTEXT.md` or `AGENTS.md`, add a reference:

```markdown
## Agent Kernel

This project uses the [agent-kernel](https://github.com/fszale/agent-kernel) kit.

**Activate a skill:** Read the relevant `skills/*/SKILL.md` file from the kernel.
**Use a prompt:** Reference `prompts/*.md` from the kernel.
**Use a template:** Reference `templates/*.md` from the kernel.
```

## Step 2: Create project-specific CONTEXT.md

Copy the kernel's `CONTEXT.md` as the starter and customize:
- Update directory map to reflect the project's structure
- Add project-specific naming conventions
- Add any domain-specific vocabulary
- Add project-specific contribution rules

## Step 3: Configure which skills activate automatically

In the downstream project's agent spec (using `agent-spec-template.yaml`):

```yaml
skills:
  - "governance-hierarchy-design"   # Always include for any agent system
  - "confidence-and-experiment"     # Always include for measurement
  - "idea-evaluator"               # Include if agents evaluate ideas
  - "rate-of-improvement"          # Include if agents measure success
```

## Step 4: Set up the .agents/workflows directory

Create project-specific workflows that extend the kernel's patterns:
- Reference kernel workflows where they apply
- Add project-specific procedures for recurring tasks

## Step 5: Configure guardrails

Use `templates/agent-config-template.yaml` to create the project's guardrail configuration. Customize:
- `max_change_pct_per_action` for your domain
- `max_actions_per_day` for your operation scale
- `min_confidence_to_execute` for your risk tolerance

## Step 6: Verify activation

Test that an AI agent working on the downstream project can:
1. Find and read CONTEXT.md in <30 seconds
2. Navigate to a skill using the skill selection guide in AGENTS.md
3. Execute a prompt using the correct variable format
4. Apply the governance hierarchy when proposing actions

## Step 7: Enable GitHub Actions

Enable the kernel's GitHub workflows in the downstream project by copying `.github/workflows/` and updating the `GEMINI_API_KEY` secret.
