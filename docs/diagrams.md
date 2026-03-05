# docs/diagrams.md

# Diagrams

We use **Mermaid** diagrams stored as `.mmd` files and embed them into Markdown docs automatically.

**Why Mermaid:**
- Renders natively on GitHub and most Markdown viewers
- Stays diff-friendly in git (plain text)
- Can be pre-rendered to SVG via the CLI if needed

**How embedding works:**
Each document contains markers:
```
<!-- DIAGRAM: <id> START -->
<!-- DIAGRAM: <id> END -->
```
The embed script replaces everything between markers with a Mermaid fenced block from the corresponding `.mmd` source file.

**Registry:** [`diagrams/registry.json`](../diagrams/registry.json)

**Run embedding:**
```bash
python3 scripts/embed_diagrams.py
# or
make embed-diagrams
```

**Validate syntax:**
```bash
make validate-mermaid
# or
npx @mermaid-js/mermaid-cli mmdc -i diagrams/your-diagram.mmd -o /dev/null
```

**CI/CD:** `.github/workflows/validate-mermaid.yml` validates all `.mmd` files on every push/PR to `diagrams/`.

---

## Diagram Inventory

| ID | Description | Used In |
|---|---|---|
| `governance-hierarchy` | Four-tier governance model: Objective→Strategy→Tactic→Action | PHILOSOPHY.md, governance-hierarchy-design SKILL.md |
| `autonomy-ladder` | L0–L3 autonomy with promotion and demotion flows | PHILOSOPHY.md, autonomy-ladder SKILL.md |
| `rate-of-improvement-curve` | S-curve shapes and diagnostic patterns | PHILOSOPHY.md, rate-of-improvement SKILL.md |
| `ppt-value-streams` | PPT × Revenue/Risk/Cost evaluation matrix | PHILOSOPHY.md, idea-evaluator SKILL.md |
| `skill-selection-flow` | Decision tree to find the right skill | AGENTS.md, CONTEXT.md |
| `agent-architecture` | Single agent runtime: inputs → safety → outputs | domain-agent-design SKILL.md |
| `agent-factory-evolution` | Era 1–4: Single agent → Agent Factory → Hybrid → Factory of Factories | agent-factory-design SKILL.md |
| `oi-operating-model` | Five-stage OI operating model cycle | PHILOSOPHY.md, ai-use-case-scoring SKILL.md |
| `antigravity-kit-architecture` | Five-layer Antigravity Kit architecture | docs/antigravity-kit-architecture.md |

---

## Compatibility Notes

Some Markdown renderers ship older Mermaid builds (e.g., 8.x). To maximize compatibility:
- Use `graph LR` or `graph TB` — NOT `flowchart LR`
- Avoid HTML tags inside node labels
- Quote labels containing parentheses: `id["Label (extra)"]`
- Avoid exotic Unicode symbols inside node labels
- Always apply `style` declarations at the end of the diagram block

---

## Adding a New Diagram

See `.agents/workflows/add-diagram.md` for step-by-step instructions.

Use the `diagram-design` skill to write compatible syntax and choose the right diagram type.
