---
name: diagram-design
description: Design Mermaid diagrams to visualize workflows, relationships, governance structures, and system architectures. Select the right diagram type, write compatible syntax, and register diagrams for embedding.
when-to-use: Use whenever a concept would be clearer as a visual than as prose — governance flows, decision trees, architecture flows, timelines, and system evolution histories.
principles: [Configuration-Driven Design, Systems Over Goals, Moonshot Architecture]
---

# Diagram Design Skill

## Purpose

Create clear, maintainable Mermaid diagrams that render natively on GitHub, are diff-friendly in git, and can be automatically embedded into documentation using the marker system.

## Agent Instructions

You are a diagram architect. Your job is to produce Mermaid diagrams that are visually informative and syntactically compatible with common Mermaid renderers.

### Step 1: Choose the Right Diagram Type

| Use Case | Diagram Type | Mermaid Keyword |
|---|---|---|
| Process flows, state transitions | Flowchart | `graph LR` or `graph TB` |
| Architecture (component connections) | Flowchart with subgraphs | `graph LR` with `subgraph` |
| Sequences (A calls B, B calls C) | Sequence Diagram | `sequenceDiagram` |
| State machines (active states) | State Machine | `stateDiagram-v2` |
| Timelines, evolution stages | Flowchart left-right | `graph LR` |
| Decision trees | Flowchart top-bottom | `graph TB` |

**Compatibility rule:** Use `graph LR` / `graph TB` (not `flowchart`) for maximum renderer compatibility. Many GitHub-embedded renderers still run Mermaid 8.x.

### Step 2: Write Compatible Syntax

**Rules for cross-renderer compatibility:**
1. Use `graph LR` or `graph TB` — NOT `flowchart LR`
2. Quote node labels containing parentheses or brackets: `id["Label (extra)"]`
3. No HTML tags inside node labels
4. Avoid exotic Unicode symbols — stick to ASCII + common emoji
5. Style nodes at the bottom with `style id fill:... stroke:...`
6. Use `subgraph Name["Title"]` for grouping
7. Break long labels with `\n` inside the quote

**Node types:**
```
id["Rectangular node"]
id(["Rounded node"])
id{{"Diamond (decision)"}  — note: escape braces if using flowchart syntax
id[["Subroutine node"]]
id(["Stadium node"])
```

### Step 3: Apply Consistent Styling

Use a consistent color palette across all diagrams in the project:

| Purpose | Fill | Stroke |
|---|---|---|
| People/Human | `#1a3a5c` | `#4a9ede` |
| System/Process | `#1a4a2e` | `#4ade80` |
| AI/Automation | `#3a2a5c` | `#a78bfa` |
| Warning/Risk | `#3a3a1a` | `#facc15` |
| Danger/Stop | `#4a1a1a` | `#f87171` |
| Neutral | `#2a2a2a` | `#6b7280` |
| Constants/Math | `#1a1a3a` | `#a78bfa` |

Always set `color:#fff` (white text) on dark backgrounds.

### Step 4: Register the Diagram

Add an entry to `diagrams/registry.json`:

```json
{
  "id": "your-diagram-id",
  "file": "diagrams/your-diagram-id.mmd",
  "description": "One-sentence description of what the diagram shows",
  "used_in": ["file/that/embeds/it.md"]
}
```

### Step 5: Add Embedding Markers to Docs

In the target markdown file, add:

```markdown
<!-- DIAGRAM: your-diagram-id START -->
<!-- DIAGRAM: your-diagram-id END -->
```

Then run `python3 scripts/embed_diagrams.py` to fill in the content automatically.
Or run `make embed-diagrams`.

### Step 6: Validate

```bash
make validate-mermaid
```

Or for a single file:
```bash
npx @mermaid-js/mermaid-cli mmdc -i diagrams/your-diagram-id.mmd -o /dev/null
```

## Output Format

1. The complete `.mmd` file content (fenced for review)
2. The `registry.json` entry to add
3. The embedding marker pair to paste into the target doc
4. Any compatibility notes for the specific diagram type used
