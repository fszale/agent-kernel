# Agent Kernel — Project Context

> **For AI agents:** Read this file first before doing any work on this project. It gives you the project map, conventions, and rules for contributing.

## What This Project Is

A **config-driven, injectable knowledge kit** (Antigravity Kit) containing reusable skills, prompts, and templates that encode a proven design philosophy. It is injected into downstream projects to give AI agents consistent behavioral patterns, knowledge, and tooling.

**Key concept:** Everything in this kit traces back to one of four operating principles:
```
People · Process · Technology (PPT)
Pareto (80/20) — focus on the 20% that delivers 80% of value
30/60/90 — map all work to Immediate / Soon / Later
First Principles — decompose problems to base elements, rebuild
```

## Directory Map

```
agent-kernel/
├── CONTEXT.md                  ← You are here (read first)
├── README.md                   ← Human-readable overview
├── AGENTS.md                   ← Agent activation and skill selection guide
├── PHILOSOPHY.md               ← Full design principles reference
├── .agents/
│   ├── workflows/              ← Step-by-step agent procedures (slash commands)
│   └── skills/                 ← Project-specific knowledge for agents
├── skills/                     ← 22 injectable agent skills (SKILL.md per skill)
├── prompts/                    ← 16 structured prompt templates
├── templates/                  ← 10 reusable document templates
├── diagrams/                   ← 8 Mermaid .mmd sources + registry.json
├── scripts/                    ← embed_diagrams.py automation
├── Makefile                    ← validate-mermaid, embed-diagrams, consistency-check
├── docs/                       ← Contributing, injection, consistency, diagrams guides
│   ├── consistency-checks.md
│   ├── contributing.md
│   ├── injection-guide.md
│   ├── design-principles.md
│   ├── diagrams.md
│   └── antigravity-kit-architecture.md
└── .github/workflows/          ← 6 automated GitHub Actions
```

## Key Files (read these to understand the system)

| File | What It Contains |
|---|---|
| `PHILOSOPHY.md` | All design principles from all four sources |
| `AGENTS.md` | How agents select and activate skills |
| `skills/*/SKILL.md` | Per-skill instructions, when-to-use, agent instructions |
| `prompts/*.md` | Structured prompt templates with variables |
| `templates/*.md` / `*.yaml` | Reusable output document formats |
| `.agents/workflows/` | Step-by-step procedures you can invoke as slash commands |

## Naming Conventions

| Artifact | Convention |
|---|---|
| Skills | `skills/{skill-name}/SKILL.md` (kebab-case directory) |
| Prompts | `prompts/{purpose}.md` (kebab-case filename) |
| Templates | `templates/{purpose}.md` or `{purpose}.yaml` |
| Agent workflows | `.agents/workflows/{action}.md` |
| Agent skills | `.agents/skills/{topic}.md` |
| GitHub workflows | `.github/workflows/{purpose}.yml` |

## Slash Commands

When working with an AI agent, use these to trigger workflow procedures:

| Command | What It Does |
|---|---|
| `/add-skill` | Creates a new skill following the standard template |
| `/add-prompt` | Creates a new prompt with variables and expected output |
| `/add-template` | Creates a new document template |
| `/add-diagram` | Creates a new Mermaid diagram with registry + embedding |
| `/run-consistency-check` | Audits all files for missing fields, broken cross-refs |
| `/update-philosophy` | Extends PHILOSOPHY.md with a new principle |
| `/inject-into-project` | Injects this kit into a downstream project |

## Governance Vocabulary

| Term | Meaning |
|---|---|
| **PPT** | People · Process · Technology — the evaluation trifecta |
| **30/60/90** | Immediate (30 days) / Soon (60 days) / Later (90 days) |
| **Value stream** | Revenue Generation, Risk Mitigation, or Cost Savings |
| **Rate of Improvement** | The trajectory of a metric over time (S-curve = success) |
| **Governance hierarchy** | Objective → Strategy → Tactic → Action chain with reasoning fields |
| **Traceability** | Every action traceable to an objective via reasoning fields in <30 seconds |
| **Autonomy ladder** | L0 Observe → L1 Recommend → L2 Approve-to-execute → L3 Guardrailed auto |
| **HITL** | Human-in-the-loop approval gate |
| **Guardrail** | Hard limit on automated action scope (budget, change %, etc.) |

## Rules for Contributing

1. **Follow naming conventions** — kebab-case, consistent structure
2. **Maintain traceability** — every skill/prompt must link to at least one principle in PHILOSOPHY.md
3. **Use existing patterns** — check `.agents/workflows/` before creating new artifacts
4. **Run consistency checks** — validate with `/run-consistency-check` before committing
5. **No brand-specific content** — all content must be generalizable across any project
6. **All SKILL.md files require frontmatter** — `name`, `description`, `when-to-use` fields are mandatory
