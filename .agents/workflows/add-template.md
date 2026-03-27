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
- Use `____________________` (25 underscores) for short fill-in fields
- Use `> ___` blockquote format for long-form responses
- Include section headers that match the expected output structure
- Add brief inline instructions as HTML comments where helpful
- Include a `## How to Use` section at the top

**For YAML templates:**
- Include inline comments explaining each field
- Use placeholder values that clearly show what to replace
- Group fields logically with section comment banners

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

For YAML templates, also validate:
```bash
npx js-yaml templates/your-template.yaml
```
