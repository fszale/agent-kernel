---
description: how to add a new prompt to the agent-kernel
---

# Add Prompt Workflow

Follow these steps to add a new prompt to the agent-kernel.

## Step 1: Create the prompt file

Create `prompts/{purpose}.md` using kebab-case. The filename should describe the prompt's primary output (e.g., `bottleneck-identification.md`, not `analysis.md`).

## Step 2: Use the standard prompt structure

```markdown
# Prompt: [Descriptive Title]

## Purpose
[What this prompt produces and why it exists]

## When to Use
- [Scenario 1]
- [Scenario 2]

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{variable_name}}` | What it represents | Example value |

## Prompt

```
[The actual prompt text with {{variable}} placeholders]
```

## Expected Output
[What the prompt produces: format, sections, required elements]

## Tips
[Usage guidance, common mistakes, follow-up actions]
```

## Step 3: Verify required fields

- [ ] All variables documented in the Variables table
- [ ] Variables use `{{double_curly_braces}}` format
- [ ] Expected Output section is specific (not "a good answer")
- [ ] Prompt body includes section headers (## 1. ## 2. etc.)
- [ ] Cross-referenced to relevant skill if one exists

## Step 4: Update Core Indexes

To ensure this new artifact is discoverable by other agents, you MUST update all of the following:

- [ ] `README.md` (Update Quick Start table and the skill count in the directory tree if applicable)
- [ ] `AGENTS.md` (Update the Skill Selection Guide table and Mermaid flow diagram)
- [ ] `CLAUDE.md` (Update the Common Task Routing table)
- [ ] `CONTEXT.md` (Update the total count of skills/prompts in the Directory Map)
- [ ] `.agents/skills/project-navigation.md` (Update the directory map and finding-the-right-tool table)
- [ ] `templates/downstream-*.md` (Update only if the addition creates a new fundamental review type or operational lens)

## Step 5: Run consistency check

Run the repository validation script to ensure all cross-references and frontmatter contracts are correct:

```bash
make consistency-check
# or
python3 scripts/validate_contracts.py
```
