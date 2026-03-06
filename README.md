# 🧠 Agent Kernel

**A reusable Antigravity Kit — skills, prompts, templates, and automation injected into any project. This is my Digitial Twin working at one of my Agentic AI Factories.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## Why This Project Exists

I have been building and observing software systems since the early home-computing era: Sinclair Spectrum, Atari, Commodore, and Amiga. Long before today’s AI wave, I was already fascinated by how machines evolve, how tools shape thinking, and how new computational layers eventually change what humans can do.

One of the early ideas that stayed with me came from GANs: the generator–discriminator dynamic showed how intelligence-like systems can improve through structured iteration, tension, and critique. That concept pushed me to experiment with rapidly evolving systems of digital intelligence long before the current generation of frontier models.

I built several incarnations of that idea over the years with mixed results. The missing ingredient was model capability. Recent advances in LLMs changed that. The quality, speed, and adaptability of modern models made it possible to move from interesting prototypes to systems that can actually perform useful work.

That led me to build a series of AI employee factories: multi-agent environments where specialized agents collaborate, critique, research, recommend, schedule, summarize, and execute recurring workflows. The latest iteration includes a digital twin — an agentic version of me that captures my working style, decision patterns, frameworks, and operating assumptions.

Agent Kernel is the reusable core of that system.
It is the portable layer of skills, prompts, templates, context, and automation that lets a digital twin operate consistently across projects.

This project is based on a simple observation: AI systems are becoming increasingly agentic, and the artifacts they produce are becoming more machine-legible, structured, and reusable. Software documentation, plans, prompts, and workflows are no longer only for humans. They are becoming operating surfaces for agents.

I also believe multi-agent systems will accelerate this shift. Recent products are starting to expose that dynamic directly, using cooperating and adversarial agents to improve outputs through critique and refinement. That pattern strongly reinforces what I have observed in practice: well-structured agent collaboration can produce better reasoning, better edge-case coverage, and better operational outcomes.

My view is that the most durable role for humans is not to compete with agents task by task, but to design, guide, and deploy systems that reflect their judgment. Build your own digital twin. Give it tools, context, memory, and operating principles. Then let it work inside an ecosystem of other agents.

This exists to help you build yours.

If you’re building toward a future of multi-agent systems, digital twins, or AI-native companies, reach out. I’m looking to connect with people who see agentic factories not as a trend, but as a new industrial layer.

All my contact information can be found at https://github.com/fszale

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
