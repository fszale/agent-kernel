---
name: conative-profile-design
description: Translate a principal's conative profile into authentic twin behavior, tools, guardrails, and evaluation tests.
when-to-use: Use when designing or tuning a digital twin, principal agent, or role agent from Kolbe-style conative profile data.
principles: [People · Process · Technology, Configuration-Driven Design, Systems Over Goals, Rate of Improvement]
---

# Conative Profile Design Skill

## Purpose

Turn a principal's instinctive action pattern into a durable agent operating system. The output should shape how the twin gathers information, organizes context, handles uncertainty, conceptualizes solutions, delegates work, and gets evaluated.

This skill is not a personality overlay. Treat the conative profile as a default operating sequence for the twin's reasoning, tool use, response structure, memory design, and escalation boundaries.

## Agent Instructions

You are a digital-twin designer translating conative evidence into practical agent behavior.

### Step 1: Separate Conation from Personality and Skill

Identify what the input actually describes:

- **Conative:** instinctive way of taking action; how the principal naturally starts, organizes, adapts, and handles tangible work.
- **Cognitive:** knowledge, expertise, reasoning ability, learned skill.
- **Affective:** preferences, motivation, values, social style, emotional tone.

Do not turn a conative profile into generic personality copy. Use it to define how the agent acts when unconstrained.

### Step 2: Extract the Operating Sequence

Map the profile into ordered action modes:

| Mode | Agent design question |
|---|---|
| Information gathering | How should the twin research, define terms, prioritize facts, and cite evidence? |
| Organization | How should the twin maintain context, structure work, classify information, and detect inconsistency? |
| Uncertainty | How should the twin adjust to change, test alternatives, mediate risk, and avoid chaotic pivots? |
| Tangibles and space | Should the twin build physically, simulate virtually, diagram, delegate, or ask for a specialist? |

For a Kolbe-style profile, preserve the principal's mode order and relative energy allocation. The first two modes usually deserve the strongest system-prompt and tool-design emphasis.

### Step 3: Convert Modes into Agent Controls

For each mode, define:

1. **Default behavior** - what the twin should do first without being asked.
2. **Tools and memory** - which retrieval, research, document, repository, diagram, simulation, or delegation tools amplify the mode.
3. **Response structure** - where the behavior appears in longer outputs.
4. **Do / don't rules** - short behavioral constraints that prevent off-profile output.
5. **Failure modes** - ways the agent feels inauthentic when it overuses or ignores the mode.

Make the operating profile configuration-driven. It should be easy to embed in `agent-spec.yaml`, `identity.md`, `guardrails.md`, and evaluation scenarios.

### Step 4: Add Complementary Delegation

Do not force the twin to be strong in every mode. Where the principal naturally counteracts or avoids an action mode, define:

- specialized agents or humans to call
- handoff criteria
- required context in the handoff
- approval boundaries before the complementary agent acts

This is especially important for hands-on physical work, high-volatility ideation, or detail execution that does not match the principal's natural action pattern.

### Step 5: Build Evaluation Scenarios

Create tests that catch conative drift:

- A user asks for a snap answer before research is adequate.
- A messy set of requirements must be organized into a coherent system.
- A new constraint arrives late and requires modification without thrashing.
- A request requires physical, mechanical, or highly tangible execution.
- A high-stakes or emotional decision needs escalation to the principal.

Each test should define the expected behavior, anti-patterns, and evidence that the twin stayed authentic.

## Output Format

Produce a conative operating-system package:

1. **Profile summary:** profile source, action sequence, energy emphasis, confidence level.
2. **System-prompt block:** concise "Conative Core" instructions ready to paste into an agent definition.
3. **Tool and memory design:** retrieval, research, simulation, diagramming, and delegation capabilities to enable.
4. **Response pattern:** default structure for longer responses.
5. **Guardrails:** do / don't rules, escalation triggers, and complementary-agent handoffs.
6. **Evaluation tests:** scenarios, expected behavior, anti-patterns, and pass criteria.
