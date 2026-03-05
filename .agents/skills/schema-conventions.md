# Schema Conventions

> Structural requirements for all files in the agent-kernel. Follow these conventions to ensure consistency checks pass and AI agents can reliably parse and use all artifacts.

## SKILL.md Frontmatter

Every `skills/*/SKILL.md` MUST begin with YAML frontmatter:

```yaml
---
name: kebab-case-skill-name       # REQUIRED — must match directory name
description: One sentence.        # REQUIRED — under 150 characters
when-to-use: Specific scenarios.  # REQUIRED — be specific, not generic
principles: [Principle1, Principle2]  # REQUIRED — link to PHILOSOPHY.md
---
```

**Required sections in the body:**
- `## Purpose` — what this skill enables
- `## Agent Instructions` — step-by-step guidance for the agent
- `## Output Format` — what the skill produces

## Prompt Template Format

Every `prompts/*.md` MUST have:

```markdown
# Prompt: [Title]

## Purpose
## When to Use
## Variables
| Variable | Description | Example |
## Prompt
` ` ` (fenced code block containing the prompt body)
## Expected Output
## Tips
```

**Variable format:** Always `{{double_curly_braces}}` for interpolated values.

## Template Format

Templates (`templates/*.md`) should include:
- Title with the template name
- Fill-in sections using `____________________` for short answers
- `> ___` for long-form responses
- Tables with empty cells for structured data

YAML templates (`templates/*.yaml`) should include:
- A comment block at the top explaining purpose and all sections
- Inline comments on all non-obvious fields
- Example values (not just `null` or empty)

## agent-spec-template.yaml Required Fields

Every agent spec derived from `agent-spec-template.yaml` must include:

```yaml
agent: {id, domain, description, owner_role, version, enabled}
discovery: {capabilities, requirements, provides}
schedule: {cron, cadence}
objectives: {primary_kpi}
skills: [list]
prompts: {task_name: {template, version, variant}}
decision_rationale: {universal_required_fields: [justification, reasoning_summary]}
actions: [{id, risk_class, autonomy_level, required_fields}]
hitl: {approvals}
logging: {emit_fields: [..., justification]}
```

## Naming Conventions Summary

| Artifact | Convention | Example |
|---|---|---|
| Skill directory | kebab-case | `rate-of-improvement/` |
| Prompt file | kebab-case | `rate-of-improvement-analysis.md` |
| Template file | kebab-case | `roi-report-template.md` |
| YAML template | kebab-case | `agent-spec-template.yaml` |
| Workflow file | kebab-case | `run-consistency-check.md` |
| GitHub Action | kebab-case | `skill-consistency-check.yml` |
