---
description: how to add a new skill to the agent-kernel
---

# Add Skill Workflow

Follow these steps to add a new skill to the agent-kernel.

## Step 1: Create the skill directory

```bash
mkdir -p skills/{skill-name}
```

Use kebab-case for the directory name. The name should be descriptive and action-oriented (e.g., `root-cause-analysis`, not `rca`).

## Step 2: Create SKILL.md with required frontmatter

Create `skills/{skill-name}/SKILL.md` with this template:

```markdown
---
name: skill-name-matches-directory
description: One sentence describing what this skill enables an agent to do.
when-to-use: Specific scenarios when an agent should activate this skill.
principles: [List, Of, Linked, Principles, From, PHILOSOPHY.md]
---

# Skill Title

## Purpose
...

## Agent Instructions
...

## Output Format
...
```

## Step 3: Verify required fields

Run a quick self-check:
- [ ] `name` field matches directory name (kebab-case)
- [ ] `description` is one sentence, under 150 characters
- [ ] `when-to-use` is specific (not "use when applicable")
- [ ] `principles` references at least one principle from PHILOSOPHY.md
- [ ] `Agent Instructions` section provides step-by-step guidance
- [ ] `Output Format` section describes what the skill produces

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
