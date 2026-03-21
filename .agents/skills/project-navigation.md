# Project Navigation

> How to find what you need in the agent-kernel repository.

## Directory Map

```
agent-kernel/
├── README.md                   ← Start here (human overview)
├── CONTEXT.md                  ← AI agent project map
├── AGENTS.md                   ← Skill selection guide for agents
├── CLAUDE.md                   ← Claude-oriented entry point
├── PHILOSOPHY.md               ← All design principles reference
├── Makefile                    ← validate-mermaid, embed-diagrams, consistency-check
├── skills/                     ← 22 agent skills
│   ├── idea-evaluator/SKILL.md
│   ├── 30-60-90-planning/SKILL.md
│   ├── first-principles/SKILL.md
│   ├── firefighter/SKILL.md
│   ├── shake-the-box/SKILL.md
│   ├── configuration-driven-design/SKILL.md
│   ├── bias-towards-action/SKILL.md
│   ├── lead-with-empathy/SKILL.md
│   ├── radical-candor/SKILL.md
│   ├── knowledge-sprints/SKILL.md
│   ├── ai-use-case-scoring/SKILL.md
│   ├── business-data-analysis/SKILL.md
│   ├── outcome-probability/SKILL.md
│   ├── rate-of-improvement/SKILL.md
│   ├── governance-hierarchy-design/SKILL.md
│   ├── hitl-and-guardrails/SKILL.md
│   ├── autonomy-ladder/SKILL.md
│   ├── tactic-design/SKILL.md
│   ├── confidence-and-experiment/SKILL.md
│   ├── diagram-design/SKILL.md
│   ├── domain-agent-design/SKILL.md
│   └── agent-factory-design/SKILL.md
├── prompts/                    ← 16 prompt templates
│   ├── idea-evaluator.md
│   ├── 30-60-90-plan.md
│   ├── ppt-assessment.md
│   ├── code-review.md
│   ├── moonshot-architecture.md
│   ├── future-trends-analysis.md
│   ├── team-metrics-review.md
│   ├── process-audit.md
│   ├── bottleneck-identification.md
│   ├── workflow-design.md
│   ├── rate-of-improvement-analysis.md
│   ├── strategy-proposal.md
│   ├── tactic-assembly.md
│   ├── action-proposal.md
│   ├── domain-agent-spec.md
│   └── agent-factory-design.md
├── templates/                  ← 12 document templates
│   ├── downstream-agents-template.md
│   ├── downstream-claude-template.md
│   ├── idea-evaluator-scorecard.md
│   ├── 30-60-90-plan-template.md
│   ├── ppt-impact-assessment.md
│   ├── project-retrospective.md
│   ├── roi-report-template.md
│   ├── weekly-progress-report.md
│   ├── business-intake-questionnaire.md
│   ├── agent-config-template.yaml
│   ├── agent-spec-template.yaml
│   └── agent-spec-domain-template.yaml
├── diagrams/                   ← 9 Mermaid .mmd diagram sources
│   ├── registry.json
│   ├── governance-hierarchy.mmd
│   ├── autonomy-ladder.mmd
│   ├── rate-of-improvement-curve.mmd
│   ├── ppt-value-streams.mmd
│   ├── skill-selection-flow.mmd
│   ├── agent-architecture.mmd
│   ├── agent-factory-evolution.mmd
│   ├── oi-operating-model.mmd
│   └── antigravity-kit-architecture.mmd
├── scripts/
│   ├── embed_diagrams.py
│   └── validate_contracts.py
├── docs/                       ← Human-facing documentation
│   ├── consistency-checks.md
│   ├── contributing.md
│   ├── injection-guide.md
│   ├── design-principles.md
│   ├── diagrams.md
│   └── antigravity-kit-architecture.md
├── .agents/
│   ├── workflows/
│   │   ├── review-project.md
│   │   ├── add-skill.md
│   │   ├── add-prompt.md
│   │   ├── add-template.md
│   │   ├── add-diagram.md
│   │   ├── run-consistency-check.md
│   │   ├── update-philosophy.md
│   │   └── inject-into-project.md
│   └── skills/
│       ├── project-navigation.md    ← This file
│       └── schema-conventions.md
└── .github/workflows/
    ├── skill-consistency-check.yml
    ├── prompt-quality-review.yml
    ├── content-improvement.yml
    ├── documentation-sync.yml
    ├── pr-agent-review.yml
    └── validate-mermaid.yml
```

## Finding the Right Tool

| I need to... | Go to... |
|---|---|
| Evaluate something | `skills/idea-evaluator/` + `prompts/idea-evaluator.md` |
| Plan something | `skills/30-60-90-planning/` + `templates/30-60-90-plan-template.md` |
| Diagnose a problem | `skills/firefighter/` or `skills/first-principles/` |
| Score AI opportunities | `skills/ai-use-case-scoring/` + `prompts/bottleneck-identification.md` |
| Design an AI workflow | `prompts/workflow-design.md` |
| Measure impact | `skills/rate-of-improvement/` + `prompts/rate-of-improvement-analysis.md` |
| Design a domain agent | `skills/domain-agent-design/` + `templates/agent-spec-domain-template.yaml` |
| Design a multi-agent factory | `skills/agent-factory-design/` + `prompts/agent-factory-design.md` |
| Design an agent system | `skills/governance-hierarchy-design/` + `templates/agent-spec-template.yaml` |
| Create a Mermaid diagram | `skills/diagram-design/` + `.agents/workflows/add-diagram.md` |
| Review another repo or artifact | `.agents/workflows/review-project.md` + `prompts/code-review.md` |
| Add a new skill | `.agents/workflows/add-skill.md` |
| Add a new prompt | `.agents/workflows/add-prompt.md` |
| Add a new template | `.agents/workflows/add-template.md` |
| Add a new diagram | `.agents/workflows/add-diagram.md` |
| Audit the repo | `.agents/workflows/run-consistency-check.md` |
| Inject into a project | `.agents/workflows/inject-into-project.md` |
