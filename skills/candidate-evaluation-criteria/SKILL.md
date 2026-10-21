---
name: candidate-evaluation-criteria
description: Score a candidate by whether their work system shows an S-curve in velocity and throughput.
when-to-use: Use when evaluating an engineering or technical leadership candidate before the interview, or when the only evidence is a paid trial. Pair with rate-of-improvement for the curve and confidence-and-experiment for calibration.
principles: [Systems Over Goals, Rate of Improvement, Confidence Scoring and Experiment Design]
---

# Candidate Evaluation Criteria

## Purpose

Resumes, portfolios, and demo apps are easy to produce with AI tools. What is hard to fake is systems-over-goals thinking: a self-improvement loop around the candidate's own work, with a measured rate of improvement on velocity and throughput.

Value streams: Risk (a weak hire) and Cost (ramp time). People: the hiring principal and the team the candidate would join. Process: a pre-interview demonstration, or a paid trial when history is missing. Technology: the candidate's capture, measurement, and agent tooling.

## Agent Instructions

You are scoring evidence of a self-improving work system. Require written evidence for every score. Draft any message to the candidate for the hiring principal to approve. Do not send it.

Classify the curve with [rate-of-improvement](../rate-of-improvement/SKILL.md). Score honesty about the data with [confidence-and-experiment](../confidence-and-experiment/SKILL.md).

### Step 1: Send the pre-interview ask

Ask, before the interview:

> Show us how you organize your work, and prove your process delivers improvement in velocity and throughput. Bring real data from your own work (a job, side project, open source, or a 1-2 week trial task we give you). Show the rate of improvement over time, not just a before and after.

If they have no history, give a paid, time-boxed trial of about 5-10 working days on a realistic backlog, and ask them to instrument it from day 1.

### Step 2: Check what they must demonstrate

1. **The system.** How work is captured, prioritized, broken down, executed, and reviewed. Where AI agents and tools sit in the loop, and what is automated versus human-judged.
2. **The feedback loop.** What they measure after each cycle, how a lesson becomes a change to the system (prompts, checklists, skills, tooling, process), and how they know a change helped. A loop that never changes the system is a diary.
3. **The metrics.** A clear baseline, then per-cycle velocity (cycle time or lead time per item) and throughput (items or outcomes shipped per week), plus a quality guardrail (defects, rework, reverts) so speed is not bought with breakage.
4. **The curve.** Improvement plotted over time. The healthy shape is an S-curve or concave rise: rapid gains early, then slowing but still continuous improvement. They should explain why it slows (low-hanging fruit gone, a new bottleneck) and what they do at the plateau (name the next constraint and start a new curve).
5. **Honesty about the data.** Sample size, what is noise, and what they would not claim. Calibrated confidence beats a hockey stick.

### Step 3: Flag these patterns

- Only goals and outputs ("I shipped X"), with no system or loop.
- No baseline, or metrics invented after the fact.
- A straight line or an ever-accelerating curve with no explanation (usually measurement error or cherry-picking).
- Speed gains with no quality guardrail.
- AI tools used, but the candidate cannot say what they changed in their own process because of what they learned.
- Cannot name the current bottleneck in their own system.

### Step 4: Score 1-4 with written evidence

| Score | Meaning |
|---|---|
| 1 | Missing, or contradicted by the evidence |
| 2 | Partial, with weak or reconstructed evidence |
| 3 | Present and evidenced, with minor gaps |
| 4 | Matches the "4 looks like" column |

| Criterion | Weight | 4 looks like |
|---|---|---|
| System design | 1 | Explicit, repeatable loop; clear human versus AI roles |
| Feedback to change | 2 | Specific lessons turned into specific system changes, with results |
| Measurement | 1 | Real baseline, velocity, throughput, and a quality guardrail |
| Rate of improvement | 2 | Data shows a rapid early rise, then slowing continuous gains, and the slowdown is explained |
| Plateau handling | 1 | Names the next constraint and how they would start a new curve |
| Calibration | 1 | Separates signal from noise and does not overclaim |

Pass bar: weighted average of 3 or higher, and no score of 1. Rate of improvement and feedback to change carry double weight. Weighted average = sum of (score times weight) / 8.

### Step 5: Probe in the interview

- Walk me through the last change you made to how you work. What triggered it, and what did the numbers do after?
- Where is your curve flattening now, and what is the next bottleneck?
- If I removed your AI tools tomorrow, which part of your system would break first?
- How would you set this loop up for a 5-person team in their first 30 days?

## Output Format

1. System summary: capture, priority, execution, review, and human versus AI.
2. Metrics table: baseline, velocity, throughput, quality guardrail, and the time window. If none was provided, say so.
3. Curve classification from rate-of-improvement (S-curve, rise-decline, flat, unbounded, or missing) and the plateau plan.
4. Scored rubric: each criterion, score, weight, and the evidence.
5. Weighted average, pass or fail against the bar, and red flags seen.
6. Recommendation: hire, no-hire, or second-trial. Include `justification`, `decision_summary`, and `evidence`.
7. Confidence in the recommendation, with the calibration reducers from confidence-and-experiment applied to sample size and data freshness.
8. Value stream tag: Risk, and Cost when ramp time is material.
