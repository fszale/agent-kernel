---
description: how to inject the agent-kernel into a downstream project
---

# Inject Into Project Workflow

## Method 1: Side-by-Side IDE Injection (For Reviews)

The fastest way to use the agent-kernel to review or advise on an existing project is to load it adjacent to your project in an IDE (like VS Code or Cursor).

1. Clone `agent-kernel` to your machine.
2. Open your IDE workspace and add **both** your project folder and the `agent-kernel` folder to the same window.
3. Open a new AI chat or agent session.
4. **Prompt the agent:** "Apply the contents of the `agent-kernel` to review the adjacent project in this workspace using `prompts/architecture-review.md`."

This gives the agent immediate access to the kernel's skills without requiring you to copy files into your project repository.

---

## Method 2: Full Project Integration

Follow these steps to permanently inject the agent-kernel directly into a downstream project's repository.

### Step 1: Add reference to the kernel

In the downstream project's `CONTEXT.md`, `AGENTS.md`, or `CLAUDE.md`, add a reference:

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
- Include `review-project.md` if the downstream repo will use the kernel for code or artifact review

## Step 5: Create downstream agent instruction files

Create the downstream instruction files from the kernel templates:
- `templates/downstream-agents-template.md` for `AGENTS.md`-aware tools
- `templates/downstream-claude-template.md` for Claude-style tools

Update the copied file so it points at the kernel location used by the downstream project, typically `.agent-kernel/`.

## Step 6: Configure guardrails

Use `templates/agent-config-template.yaml` to create the project's guardrail configuration. Customize:
- `max_change_pct_per_action` for your domain
- `max_actions_per_day` for your operation scale
- `min_confidence_to_execute` for your risk tolerance

## Step 7: Verify activation

Test that an AI agent working on the downstream project can:
1. Find and read CONTEXT.md in <30 seconds
2. Navigate to a skill using the skill selection guide in AGENTS.md
3. Execute a prompt using the correct variable format
4. Apply the governance hierarchy when proposing actions
5. Run a review flow using `review-project.md` and `prompts/code-review.md`

## Step 8: Enable GitHub Actions

Enable the kernel's GitHub workflows in the downstream project by copying `.github/workflows/`.
For optional LLM-powered workflows, configure these secrets:
- `LLM_API_KEY`
- `LLM_API_ENDPOINT` (OpenAI-compatible `/chat/completions` endpoint)
- `LLM_MODEL`
