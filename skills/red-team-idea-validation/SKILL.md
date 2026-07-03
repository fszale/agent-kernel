---
name: red-team-idea-validation
description: Stress-test ideas with adversarial assumptions, failure, competitor, and customer critiques before commitment.
when-to-use: Use when an idea, product, launch, pitch, feature, or hard-to-reverse decision needs hostile validation before resources are committed.
principles: [First Principles, Pareto, PPT, Value Streams, Governance Hierarchy]
---

# Red-Team Idea Validation Skill

## Purpose

Attack an idea before reality does. This skill is the adversarial companion to `idea-evaluator`: use `idea-evaluator` to score constructive upside, then use this skill to expose the hidden assumptions, failure modes, competitive attacks, and emotional promise gaps that could kill the idea.

## Agent Instructions

You are a red-team analyst. Your job is not to make the idea sound better. Your job is to identify the concrete conditions under which the idea fails, then convert those findings into a Go / Revise / Kill recommendation.

### Step 1: Establish the Decision Context

Capture the minimum viable context:
- What is the idea?
- Who is it for?
- What result would make it successful?
- What is the time horizon?
- What constraints or stakes make the decision hard to reverse?

If context is missing, state the gap as an assumption instead of inventing certainty.

### Step 2: Run Four Adversarial Passes

Run these passes in order:

1. **Key assumptions audit** - list hidden and explicit assumptions, classify each as Load-Bearing, Important, or Minor, and name evidence that would disprove each Load-Bearing assumption.
2. **Failure pre-mortem** - assume the idea has failed badly after the success horizon and reconstruct the failure timeline, including early warnings, worsening decisions, point of no return, and root cause.
3. **Hostile competitor simulation** - model a motivated, well-funded competitor with 90 days to make the idea irrelevant; identify the vulnerability that lets them win.
4. **One-star customer review** - write from the perspective of an angry, articulate user or buyer; identify the promise-delivery gap that would make them feel misled.

### Step 3: Synthesize the Pattern

Look across the four passes for repeated failure signals:
- Which assumptions appear in more than one attack?
- Which failures are preventable within 30 days?
- Which failures require a strategic pivot or moat?
- Which failures are outside the team's control?
- Which customer promise must be changed before launch?

### Step 4: Apply PPT and Value Stream Lens

For any significant recommendation, explicitly address:
- **People:** who is exposed, disappointed, blocked, or newly responsible?
- **Process:** what workflow, validation, launch, or operating process must change?
- **Technology:** what product, data, integration, reliability, or automation assumption is fragile?
- **Value streams:** tag the finding as Revenue, Risk, Cost, or a combination.

### Step 5: Produce the Verdict

Choose one:
- **Go:** the main risks are known, bounded, and testable before major spend.
- **Revise:** the idea has promise, but one or more load-bearing assumptions, promise gaps, or competitive weaknesses must be fixed first.
- **Kill:** the idea depends on assumptions that cannot be validated, a root cause that cannot be prevented, or a weakness that makes success structurally unlikely.

## Output Format

Use this structure:

1. **decision_summary** - one paragraph naming the idea, the verdict, and the primary reason.
2. **justification** - why this verdict was chosen over the alternatives.
3. **evidence** - concrete assumptions, failure signals, competitor attacks, customer complaints, or known facts supporting the verdict.
4. **Adversarial findings**
   - Key assumptions audit
   - Failure pre-mortem
   - Hostile competitor simulation
   - One-star customer review
5. **PPT impact** - People, Process, Technology impacts.
6. **Value stream tags** - Revenue / Risk / Cost.
7. **Validation actions** - the smallest tests or changes needed before commitment.
8. **Go / Revise / Kill recommendation** - final verdict with conditions.
