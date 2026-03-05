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

## Step 4: Add to README.md

Update the Skills section in `README.md` to include the new skill in the quick-start table. Run consistency check: `/run-consistency-check`.

## Step 5: Update .agents/skills/project-navigation.md

Add the new skill to the skills inventory in `.agents/skills/project-navigation.md`.
