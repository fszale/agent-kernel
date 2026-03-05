# 🧠 Agent Kernel

**A reusable Antigravity Kit — skills, prompts, templates, and automation injected into any project.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## What This Is

The Agent Kernel is a shared knowledge and tooling layer that encodes a proven design philosophy across four dimensions:

- **Skills** — Reusable agent behaviors (evaluating ideas, planning, diagnosing, designing systems)
- **Prompts** — Structured prompt templates for consistent AI-assisted workflows
- **Templates** — Reusable document formats for planning, retrospectives, ROI reporting
- **Automation** — GitHub workflows for continuous quality and improvement

## Core Philosophy

Every decision in this kit is evaluated through four lenses:

| Lens | Question |
|---|---|
| **People · Process · Technology** | Who is affected? What process changes? What tech enables it? |
| **Pareto (80/20)** | Which 20% of work delivers 80% of the value? |
| **30/60/90 Mindset** | Immediate / Soon / Later — map all deliverables to time horizons |
| **First Principles** | What are the base elements? Build from the ground up. |

All work connects to at least one value stream: **Revenue Generation · Risk Mitigation · Cost Savings**

→ See [PHILOSOPHY.md](PHILOSOPHY.md) for the full reference.

## Quick Start

| You want to… | Start here |
|---|---|
| **Evaluate an idea** | `skills/idea-evaluator/SKILL.md` + `prompts/idea-evaluator.md` |
| **Plan a project** | `skills/30-60-90-planning/SKILL.md` + `templates/30-60-90-plan-template.md` |
| **Diagnose an issue** | `skills/firefighter/SKILL.md` |
| **Score AI use cases** | `skills/ai-use-case-scoring/SKILL.md` + `prompts/bottleneck-identification.md` |
| **Design an autonomous system** | `skills/governance-hierarchy-design/SKILL.md` + `templates/agent-spec-template.yaml` |
| **Design a domain agent** | `skills/domain-agent-design/SKILL.md` + `templates/agent-spec-domain-template.yaml` |
| **Design a multi-agent factory** | `skills/agent-factory-design/SKILL.md` + `prompts/agent-factory-design.md` |
| **Measure AI impact** | `skills/rate-of-improvement/SKILL.md` + `prompts/rate-of-improvement-analysis.md` |
| **Create a diagram** | `skills/diagram-design/SKILL.md` + `.agents/workflows/add-diagram.md` |
| **Inject into a project** | [docs/injection-guide.md](docs/injection-guide.md) |
| **Add a skill or prompt** | [docs/contributing.md](docs/contributing.md) |
| **AI agent working here** | [AGENTS.md](AGENTS.md) and [CONTEXT.md](CONTEXT.md) |

## Repository Structure

```
agent-kernel/
├── README.md                   ← You are here
├── AGENTS.md                   ← Agent injection guide
├── CONTEXT.md                  ← AI-first project map
├── PHILOSOPHY.md               ← Full design principles reference
├── .agents/
│   ├── workflows/              ← Step-by-step agent procedures
│   └── skills/                 ← Project knowledge for agents
├── skills/                     ← 22 reusable agent skills
├── prompts/                    ← 16 structured prompt templates
├── templates/                  ← 10 reusable document templates
├── diagrams/                   ← 8 Mermaid .mmd sources + registry
├── scripts/                    ← embed_diagrams.py automation
├── Makefile                    ← validate, embed, consistency targets
├── docs/                       ← Contributing, injection, diagrams guides
└── .github/workflows/          ← 6 automated quality + improvement workflows
```

## Source Philosophy

This kit synthesizes principles from four sources:

- **Seed documents** — 30/60/90, PPT framework, Shake the Box, Firefighter, Config-Driven Design
- **[School of Titans](https://github.com/fszale/school-of-titans)** — First Principles, Systems over Goals, Lead with Empathy, Radical Candor, Knowledge Sprints
- **[Operational Intelligence Lab](https://github.com/fszale/operational-intelligence-lab)** — Rate of Improvement, AI Employee Model, OI Operating Model, ROI Modeling
- **Agentic OS** — Governance Hierarchy, HITL Design, Autonomy Ladder, Tactic Design, Experiment Design

## Automated Improvement

Six GitHub Actions continuously maintain and improve this kit:
- **Skill consistency check** — validates structure on every push
- **Prompt quality review** — weekly AI-driven review with suggestions
- **Content improvement** — weekly gap analysis across all four philosophies
- **Documentation sync** — keeps README indexes in sync with actual files
- **PR agent review** — AI reviews every PR for traceability and consistency
- **Mermaid validation** — validates diagram syntax on every push to `diagrams/`

## Contributing

See [docs/contributing.md](docs/contributing.md) for how to add skills, prompts, and templates.
