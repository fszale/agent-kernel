---
description: generic Cowork task template for activating the agent-kernel digital twin across any task
---

# Cowork Task Template

Use this template as the starting point for any Cowork task that should operate with the agent-kernel digital twin active. Copy, fill in the `{{variables}}`, and run.

---

## Task Instruction (copy and fill in)

```
Kernel path: /Users/fszale/projects/agent-kernel

Step 1 — Activate the kernel
Read the following files in order before doing anything else:
1. /Users/fszale/projects/agent-kernel/CLAUDE.md
2. /Users/fszale/projects/agent-kernel/AGENTS.md
3. /Users/fszale/projects/agent-kernel/CONTEXT.md

Step 2 — Select the right skill
Use the skill selection guide in AGENTS.md to identify the best skill for this task.
Read the full SKILL.md for the selected skill before proceeding.

Step 3 — Execute the task
Task type: {{evaluate an idea | review a codebase | generate a document | other}}
Target: {{file path, URL, description, or idea statement}}
Goal: {{what a successful output looks like in one sentence}}
Constraints: {{time, scope, format, or audience — leave blank if none}}

Step 4 — Apply the operating lens
Run through these in order before producing output:
- PPT: who is affected, what process changes, what technology is involved?
- Pareto: what is the 20% of findings or actions that delivers 80% of value?
- Value stream: does the output drive Revenue, reduce Risk, or save Cost?

Step 5 — Produce output
Format: {{findings list | scorecard | plan | review report | other}}
Tag each major finding or recommendation to Revenue / Risk / Cost.
Lead with findings, not summary.
Order by severity or impact, highest first.
```

---

## Skill Quick-Reference

Fill in Step 2 faster using this map:

| Task type | Skill to activate | Prompt to use |
|---|---|---|
| Evaluate an idea or initiative | `skills/idea-evaluator/SKILL.md` | `prompts/idea-evaluator.md` |
| Review a codebase or artifact | `skills/first-principles/SKILL.md` | `prompts/code-review.md` |
| Diagnose a failure or blocker | `skills/firefighter/SKILL.md` | — |
| Plan a project or roadmap | `skills/30-60-90-planning/SKILL.md` | `prompts/30-60-90-plan.md` |
| Design an agent or system | `skills/domain-agent-design/SKILL.md` | `prompts/domain-agent-spec.md` |

---

## Filled Example — Idea Evaluation

```
Kernel path: /Users/fszale/projects/agent-kernel

Step 1 — Activate the kernel
Read the following files in order before doing anything else:
1. /Users/fszale/projects/agent-kernel/CLAUDE.md
2. /Users/fszale/projects/agent-kernel/AGENTS.md
3. /Users/fszale/projects/agent-kernel/CONTEXT.md

Step 2 — Select the right skill
Read: /Users/fszale/projects/agent-kernel/skills/idea-evaluator/SKILL.md
Use prompt: /Users/fszale/projects/agent-kernel/prompts/idea-evaluator.md

Step 3 — Execute the task
Task type: evaluate an idea
Target: Build an AI agent that automates weekly progress reports from Slack and Jira
Goal: Score the idea across PPT dimensions and produce a go/no-go recommendation

Step 4 — Apply the operating lens
- PPT: who is affected, what process changes, what technology is involved?
- Pareto: what is the 20% of the idea that delivers 80% of the value?
- Value stream: Revenue / Risk / Cost impact?

Step 5 — Produce output
Format: scorecard
Tag each dimension to Revenue / Risk / Cost.
Lead with the overall score and recommendation.
Order supporting findings by impact, highest first.
```

---

## Filled Example — Codebase Review

```
Kernel path: /Users/fszale/projects/agent-kernel

Step 1 — Activate the kernel
Read the following files in order before doing anything else:
1. /Users/fszale/projects/agent-kernel/CLAUDE.md
2. /Users/fszale/projects/agent-kernel/AGENTS.md
3. /Users/fszale/projects/agent-kernel/CONTEXT.md

Step 2 — Select the right skill
Read: /Users/fszale/projects/agent-kernel/skills/first-principles/SKILL.md
Use prompt: /Users/fszale/projects/agent-kernel/prompts/code-review.md
Also read: /Users/fszale/projects/agent-kernel/.agents/workflows/review-project.md

Step 3 — Execute the task
Task type: review a codebase
Target: /Users/fszale/projects/{{project-name}}
Goal: Identify the top issues by severity and produce a prioritized fix list

Step 4 — Apply the operating lens
- PPT: what process does this code support, who depends on it, what tech risks exist?
- Pareto: what are the 2-3 issues that account for 80% of the risk?
- Value stream: are failures here a Revenue, Risk, or Cost problem?

Step 5 — Produce output
Format: findings list
Tag each finding to Revenue / Risk / Cost.
Lead with the highest-severity finding.
End with the single highest-value next fix.
```

---

## Notes

- Always run Step 1 first — skipping kernel activation means the digital twin is not active
- If a skill referenced in Step 2 has a linked prompt template, read both before executing
- Constraints in Step 3 are optional but improve output quality significantly
- Output format in Step 5 should match how you will consume the result (e.g., paste into a doc vs. act on directly)
