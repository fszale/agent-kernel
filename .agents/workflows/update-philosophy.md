---
description: how to add or extend a design principle in PHILOSOPHY.md
---

# Update Philosophy Workflow

Follow these steps to add a new design principle or extend an existing one.

## Step 1: Identify the principle's source

Every principle must trace to a named source:
- **Seed documents** → Part 2 in PHILOSOPHY.md
- **School of Titans** → Part 3 in PHILOSOPHY.md
- **Operational Intelligence** → Part 4 in PHILOSOPHY.md
- **Agentic OS** → Part 5 in PHILOSOPHY.md
- **New source** → Create a new Part section

## Step 2: Write the principle entry

Follow the existing structure:

```markdown
### Principle Name

> One-sentence thesis (blockquote format)

**Process / Framework:**
1. Step 1
2. Step 2
...

*Source attribution in italics.*
```

**Rules:**
- No brand-specific references — all principles must be generalizable
- Include actionable application guidance, not just theory
- Reference related skills if they exist

## Step 3: Update cross-references

1. **AGENTS.md** — if the principle implies a new skill task, add a row to the Skill Selection Guide
2. **docs/design-principles.md** — add a one-line summary to the Principle Lookup table
3. **CONTEXT.md** — if the principle introduces new vocabulary, add to the Governance Vocabulary table

## Step 4: Consider a diagram

If the principle has a visual flow (hierarchy, cycle, decision tree):
1. Create a `.mmd` file in `diagrams/`
2. Register in `diagrams/registry.json`
3. Add embed markers to PHILOSOPHY.md at the insertion point
4. Run `make embed-diagrams`

See `.agents/workflows/add-diagram.md` for the full diagram workflow.

## Step 5: Consider a skill

If the principle is actionable enough to warrant step-by-step agent instructions, create a new skill:

See `.agents/workflows/add-skill.md` for the full skill creation workflow.

## Step 6: Run consistency check

```bash
make consistency-check
```
