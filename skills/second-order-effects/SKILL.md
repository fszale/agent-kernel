---
name: second-order-effects
description: Map the downstream consequences of any decision, action, or system change across two causal layers — what the first effect triggers, and what that triggers in turn.
when-to-use: Use before finalizing high-stakes decisions, deploying agents to new domains, approving strategies with broad organizational reach, or any time unintended consequences could materially affect Revenue, Risk, or Cost.
principles: [First Principles, PPT, Governance Hierarchy, Pareto]
---

# Second-Order Effects Skill

## Purpose

First-order thinking asks "what will happen?" Second-order thinking asks "and then what?" Third-order thinking asks "and what does that trigger?"

This skill produces a layered effects map that surfaces non-obvious consequences before they become costly surprises. It is not a replacement for primary analysis — it is a mandatory follow-on step for any decision with broad reach, long time horizons, or systemic interdependencies.

## Agent Instructions

You are a systems analyst mapping causal chains. Your job is to follow consequences outward — not to predict them with certainty, but to surface them with enough specificity that decision-makers can monitor, mitigate, or prepare for them.

---

### Step 1: Anchor the First-Order Outcome

State the **direct, intended outcome** of the action or decision in one sentence:

> "If [action], then [immediate intended result] within [timeframe]."

This is the first-order effect. Do not proceed to Step 2 until this is unambiguous.

---

### Step 2: Map Second-Order Effects

For each of the 4 axes below, identify effects that are caused by the first-order outcome — not by the original action directly.

#### Axis 1: Stakeholders
Who changes their behavior, priorities, or expectations *because* the first-order outcome occurred?
- Which groups benefit unexpectedly?
- Which groups are disadvantaged by the same change?
- What competitive or political dynamics shift?

#### Axis 2: Adjacent Systems
Which systems, workflows, or processes are affected *because* the first-order change propagates into them?
- What depends on what changed?
- What upstream or downstream system now behaves differently?
- What integration points become stressed or broken?

#### Axis 3: Incentives & Behaviors
How do individual or team behaviors change *because* of the new outcome?
- Does this create a new incentive (positive or perverse)?
- Does this make previously undesirable behavior rational?
- Does this reduce motivation for something that was previously rewarded?

#### Axis 4: Feedback Loops
What self-reinforcing or self-correcting dynamics does the first-order outcome activate?
- **Reinforcing loop**: The effect amplifies itself over time (growth or collapse spiral)
- **Balancing loop**: The effect generates pressure that limits or reverses itself

For each second-order effect, score it:
- **Likelihood**: H (>60%), M (30–60%), L (<30%)
- **Magnitude**: H (material impact on Revenue/Risk/Cost), M (moderate), L (minor)

---

### Step 3: Map Third-Order Effects

For each **high-severity second-order effect** (Likelihood ≥ M AND Magnitude ≥ M):
- What does this second-order effect itself cause?
- Follow the same 4 axes
- Apply the same Likelihood × Magnitude scoring

Do not enumerate every possible third-order effect — focus only on those descending from high-severity second-order effects.

---

### Step 4: Classify Each Effect

Tag each effect with:
- **RRC**: Revenue / Risk / Cost (or multiple)
- **PPT axis**: People / Process / Technology (or multiple)
- **Timeline**: 0–30 days / 31–90 days / 91–180 days / 180+ days

---

### Step 5: Flag High-Severity Chains

A chain is **high-severity** if:
- A reinforcing feedback loop exists in the second or third layer
- A third-order effect has higher magnitude than the first-order outcome
- An effect crosses organizational or system boundaries in a way the original decision-maker did not anticipate

For each high-severity chain:
- Name the monitoring indicator that would signal the chain is activating
- Specify the decision threshold: "If [indicator] reaches [value], escalate to [owner]"
- Recommend a mitigation or guardrail that addresses the chain at its second-order point (earlier = cheaper)

---

### Step 6: Produce the Effects Map

Output the structured map using the [second-order-effects-map.md](../../templates/second-order-effects-map.md) template.

---

## Output Format

1. First-order outcome statement (one sentence)
2. Second-order effects table (Axis / Effect / Likelihood / Magnitude / RRC / PPT / Timeline)
3. Third-order effects table (same structure, only for high-severity second-order effects)
4. Feedback loops identified (type: reinforcing or balancing, description)
5. High-severity chain flags (chain summary, monitor indicator, decision threshold, mitigation)
6. Recommended monitoring indicators (what to watch, how often, who owns it)
