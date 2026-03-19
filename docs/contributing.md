# docs/contributing.md

# Contributing to Agent Kernel

Thank you for contributing! This guide covers how to add skills, prompts, and templates to the agent-kernel.

## Before You Start

Read the following files in order:
1. `CONTEXT.md` — project map and conventions
2. `PHILOSOPHY.md` — design principles your contribution should align with
3. `AGENTS.md` — skill selection guide (to avoid duplicating existing coverage)

## How to Add a Skill

Follow the workflow at `.agents/workflows/add-skill.md`.

**Quick checklist:**
- [ ] Directory name is kebab-case
- [ ] `SKILL.md` has all required frontmatter fields (`name`, `description`, `when-to-use`, `principles`)
- [ ] `Agent Instructions` section is step-by-step and actionable
- [ ] `Output Format` explicitly describes the output
- [ ] Skill is cross-referenced in `README.md`
- [ ] Skill is added to `.agents/skills/project-navigation.md`
- [ ] `/run-consistency-check` passes

## How to Add a Prompt

Follow the workflow at `.agents/workflows/add-prompt.md`.

**Quick checklist:**
- [ ] Filename is kebab-case
- [ ] All input variables use `{{double_curly_braces}}`
- [ ] Variables table is complete
- [ ] Prompt body has numbered sections
- [ ] Expected Output is explicit
- [ ] Cross-referenced to relevant skill if applicable

## How to Add a Template

Create `templates/{purpose}.md` (or `.yaml` for config templates).

**Requirements:**
- Fillable fields use `____________________` (25 underscores)
- Long-form answers use `> ___` blockquote format
- Tables have empty data cells
- YAML templates have inline comments on every field

## Running Consistency Checks

Before submitting a PR:

```bash
make all-checks
```

## GitHub Actions (Optional Example Workflows)

The following workflows require a `GEMINI_API_KEY` secret:
- `prompt-quality-review.yml`
- `content-improvement.yml`
- `pr-agent-review.yml`

Set this in: **Repository Settings → Secrets and Variables → Actions → New repository secret**

## Design Principles for Contributions

All contributions should:
1. Align with at least one principle in `PHILOSOPHY.md`
2. Be generalizable — no brand-specific content
3. Include explicit "When to Use" guidance
4. Produce a concrete, formatted output (not just advice)
5. Connect to at least one value stream: Revenue / Risk / Cost
