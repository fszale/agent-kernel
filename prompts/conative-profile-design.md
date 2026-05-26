# Prompt: Conative Profile Design

## Purpose

Convert a Kolbe-style conative profile, interview notes, or working-style evidence into a reusable operating profile for a digital twin or principal agent.

## When to Use

- Building a new digital twin and the principal has a conative profile.
- Updating an existing twin so it acts more authentically under pressure.
- Designing agent tools, memory, guardrails, and evaluation tests around a principal's natural action sequence.
- Creating complementary-agent handoffs for work the principal should not pretend to own.

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{principal_name}}` | Name of the principal or role the agent represents. | Filip Szalewicz |
| `{{profile_source}}` | Source material used for the conative profile. | Kolbe A report, interview notes, manager observations |
| `{{profile_summary}}` | Scores, modes, strengths, energy allocation, and known do/don't guidance. | 7-6-5-2: Specify, Maintain, Modify, Envision |
| `{{existing_agent_materials}}` | Current prompt, agent spec, identity, guardrails, or skill list to update. | agent-spec.yaml, identity.md, guardrails.md |
| `{{target_context}}` | Where the twin will operate. | sales discovery, strategy advisory, agentic workflow design |
| `{{known_constraints}}` | Boundaries, privacy concerns, human review needs, or implementation limits. | must escalate high-stakes client commitments |

## Prompt

```text
You are designing a conative operating profile for {{principal_name}}'s digital twin.

Source material:
{{profile_source}}

Profile summary:
{{profile_summary}}

Existing agent materials:
{{existing_agent_materials}}

Target operating context:
{{target_context}}

Known constraints:
{{known_constraints}}

Produce a reusable conative operating-system package. Do not treat the profile as personality copy. Translate it into action patterns, tool use, memory design, response structure, delegation boundaries, and evaluation tests.

## 1. Profile Interpretation
- Separate conative action pattern from cognitive expertise and affective preferences.
- Identify the natural sequence the twin should follow.
- State the strongest modes, support modes, and low-energy or delegation modes.
- Call out assumptions and confidence level.

## 2. Conative Core Prompt Block
Draft a concise system-prompt section that can be pasted into an agent definition. Include:
- default action sequence
- do / don't rules
- how to handle uncertainty
- what the twin should delegate or escalate
- how to stay authentic without becoming rigid

## 3. Tool, Memory, and Workflow Design
Map each mode to:
- required tools
- memory architecture
- response pattern
- workflow gates
- failure modes

## 4. Reusable Agent Spec Fields
Draft YAML-ready fields for an agent spec:
- conative_profile
- operating_sequence
- tool_priorities
- delegation_boundaries
- evaluation_scenarios

## 5. Evaluation Tests
Create 5-8 tests that would catch an inauthentic twin. For each test include:
- scenario
- expected behavior
- anti-pattern
- pass criteria

## 6. Integration Plan
Provide a 30/60/90 integration plan:
- 30: immediate prompt/spec updates
- 60: memory/tooling/evaluation improvements
- 90: rate-of-improvement review and calibration loop

Every recommendation must include justification, decision_summary, and evidence.
Tag each major recommendation with Revenue, Risk, Cost, or a combination.
Address People, Process, and Technology impacts for any significant recommendation.
```

## Expected Output

A reusable conative operating profile with:

- profile interpretation
- paste-ready system prompt block
- tool and memory architecture
- YAML-ready agent spec fields
- delegation and escalation boundaries
- evaluation scenarios
- 30/60/90 integration plan

## Tips

- Use the profile as an operating sequence, not a horoscope.
- Avoid overfitting: the profile should define defaults, not a prison.
- Use direct evidence from the source report or interview when available.
- When a mode is low-energy, design delegation and handoffs instead of pretending the twin can do everything.
