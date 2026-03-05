---
description: how to add a new Mermaid diagram to the agent-kernel
---

# Add Diagram Workflow

Follow these steps to create a new diagram and embed it into documentation.

## Step 1: Create the .mmd file

```bash
touch diagrams/{diagram-id}.mmd
```

Use kebab-case for the diagram ID. The ID should describe what the diagram shows (e.g., `agent-factory-evolution`, `confidence-scoring-flow`).

Write the diagram content using `graph LR` or `graph TB` syntax (not `flowchart`). See `skills/diagram-design/SKILL.md` for syntax rules and color conventions.

## Step 2: Register the diagram

Add an entry to `diagrams/registry.json`:

```json
{
  "id": "your-diagram-id",
  "file": "diagrams/your-diagram-id.mmd",
  "description": "One-sentence description of what this diagram shows",
  "used_in": ["path/to/file/that/embeds/it.md"]
}
```

## Step 3: Add markers to target documents

In each Markdown file listed in `used_in`, add the embedding markers at the appropriate location:

```markdown
## Diagram Title

<!-- DIAGRAM: your-diagram-id START -->
<!-- DIAGRAM: your-diagram-id END -->
```

The content between the markers will be replaced automatically by the embed script.

## Step 4: Embed the diagram

```bash
python3 scripts/embed_diagrams.py --verbose
# or
make embed-diagrams
```

## Step 5: Validate

```bash
make validate-mermaid
```

Or validate a single file:

```bash
npx @mermaid-js/mermaid-cli mmdc -i diagrams/your-diagram-id.mmd -o /dev/null
```

Fix any syntax errors before committing.

## Step 6: Verify rendering

Push to GitHub and verify the diagram renders correctly in the target Markdown files. GitHub renders Mermaid natively.

## Common Mistakes

- Using `flowchart LR` instead of `graph LR` (breaks older renderers)
- Forgetting to add the diagram to `registry.json` (CI will fail)
- Forgetting the markers in the target file (embed script skips files without markers)
- HTML tags inside node labels (breaks renderers)
