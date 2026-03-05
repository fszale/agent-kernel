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

## Step 4: Update README.md

Add the new prompt to the relevant row in the Quick Start table.

## Step 5: Run consistency check

`/run-consistency-check`
