---
description: how to add a new document template to the agent-kernel
---

# Add Template Workflow

Follow these steps to create a new reusable template.

## Step 1: Choose the format

- Use `.md` for document templates (scorecards, plans, reports, questionnaires)
- Use `.yaml` for configuration or specification templates (agent configs, agent specs)

## Step 2: Create the file

```bash
touch templates/{purpose}.md
# or
touch templates/{purpose}.yaml
```

Use kebab-case. Name should describe the output document, not the skill that uses it.

## Step 3: Write the template content

**For Markdown templates:**
- Use `{{variable_name}}` placeholders for all fillable fields
- Include section headers that match the expected output structure
- Add brief inline instructions as HTML comments where helpful
- Include a `## How to Use` section at the top

**For YAML templates:**
- Include inline comments explaining each field
- Use placeholder values that clearly show what to replace
- Group fields logically with section comment banners

## Step 4: Link from AGENTS.md

Add a row to the appropriate Skill Selection Guide table in `AGENTS.md`:

```markdown
| Your use case | relevant-skill | relevant-prompt.md | your-new-template.md |
```

## Step 5: Update project-navigation.md

Add the template to the directory listing in `.agents/skills/project-navigation.md`.

## Step 6: Run consistency check

```bash
make consistency-check
```

For YAML templates, also validate:
```bash
npx js-yaml templates/your-template.yaml
```
