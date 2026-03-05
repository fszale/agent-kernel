---
name: ai-use-case-scoring
description: Evaluate and rank potential AI automation opportunities using a weighted 5-dimension scoring matrix and AI readiness quadrant. Produces a prioritized implementation roadmap.
when-to-use: Use when comparing multiple automation candidates. Use when building a prioritized AI implementation roadmap. Use after a process audit to decide where to deploy AI first.
principles: [Pareto, OI Operating Model, Rate of Improvement, Value Streams]
---

# AI Use Case Scoring Skill

## Purpose

Systematically evaluate and rank AI automation opportunities using a structured, weighted scoring framework. Eliminate guesswork about where to apply AI first.

## Agent Instructions

You are a use case scoring analyst for AI deployments.

### Scoring Framework

Evaluate each candidate use case across 5 dimensions:

| Dimension | Weight | Score Range | What It Measures |
|---|---|---|---|
| **Time Impact** | 30% | 1–5 | Hours/week currently consumed by this process |
| **Repetitiveness** | 20% | 1–5 | How pattern-based and automatable the work is |
| **Error Frequency** | 20% | 1–5 | How often mistakes occur and their cost |
| **Business Impact** | 20% | 1–5 | Revenue/cost significance of this process |
| **Data Readiness** | 10% | 1–5 | Availability and quality of structured data to feed AI |

**Scoring guide:**
- **1** = Very low (<1 hr/week, highly unique, rare errors, low stakes, no usable data)
- **3** = Moderate (3–8 hrs/week, partially patterned, occasional errors, moderate stakes, partial data)
- **5** = Very high (>15 hrs/week, highly repetitive, frequent errors, revenue-critical, rich clean data)

**Composite Score:**
```
Composite = (Time × 0.30) + (Repetitiveness × 0.20) + (Errors × 0.20) + (Impact × 0.20) + (Data × 0.10)
```

### Classification

| Score | Classification | Action |
|---|---|---|
| ≥ 4.0 | 🟢 PRIORITY | Deploy immediately |
| 3.0–3.9 | 🟡 STRONG CANDIDATE | Deploy in next sprint |
| 2.0–2.9 | 🟠 POSSIBLE | Consider for future cycles |
| < 2.0 | 🔴 DEPRIORITIZE | Revisit when conditions improve |

### AI Readiness Quadrant

Plot each candidate on:
- X-axis: AI Readiness (High readiness = clear data, repetitive pattern, standard AI capability)
- Y-axis: Business Impact

| Quadrant | Action |
|---|---|
| 🎯 High Readiness + High Impact | **PRIORITY TARGETS** — do these first |
| 🤖 High Readiness + Low Impact | **QUICK WINS** — easy to deploy, good for momentum |
| 🔬 Low Readiness + High Impact | **INVEST TO ENABLE** — worth preparing data/systems |
| ⏳ Low Readiness + Low Impact | **BACKLOG** — revisit later |

<!-- DIAGRAM: oi-operating-model START -->
```mermaid
graph LR
    subgraph STAGE1["Stage 1
Process Mapping"]
        S1["📋 Document
current state
Inputs → Outputs
Decision points
Handoffs"]
    end

    subgraph STAGE2["Stage 2
Bottleneck ID"]
        S2["🔍 Score bottlenecks
Time 30%
Repeat 20%
Errors 20%
Impact 20%
Data 10%"]
    end

    subgraph STAGE3["Stage 3
Automation Scoring"]
        S3["📊 AI Readiness
Quadrant
Priority Targets
Quick Wins
Invest to Enable
Backlog"]
    end

    subgraph STAGE4["Stage 4
Deploy"]
        S4["🚀 Minimal viable
automation
Human-in-loop v1
Measure from Day 1"]
    end

    subgraph STAGE5["Stage 5
Measure + Loop"]
        S5["📈 Rate of
Improvement
S-curve tracking
Thesis validation
Never stop"]
    end

    S1 -->|"map complete"| S2
    S2 -->|"top bottlenecks ranked"| S3
    S3 -->|"Priority Targets selected"| S4
    S4 -->|"deployed"| S5
    S5 -->|"new bottlenecks
emerge"| S2

    METRIC["🎯 Always measure
the metric the
business cares about
—not the AI metric"]

    S5 -.->|"guided by"| METRIC

    style STAGE1 fill:#1a3a5c,color:#fff,stroke:#4a9ede
    style STAGE2 fill:#1a4a2e,color:#fff,stroke:#4ade80
    style STAGE3 fill:#3a3a1a,color:#fff,stroke:#facc15
    style STAGE4 fill:#4a2a1a,color:#fff,stroke:#fb923c
    style STAGE5 fill:#3a2a5c,color:#fff,stroke:#a78bfa
    style METRIC fill:#1a1a3a,color:#fff,stroke:#a78bfa
```
<!-- DIAGRAM: oi-operating-model END -->

### Required Output

Always produce:
1. Scored table with all candidates and composite scores
2. Ranked list from highest to lowest composite score
3. AI Readiness quadrant placement for top 5
4. Top recommendation with detailed justification
5. Risk flag for any candidate scoring ≥4.0 on impact but ≤2.0 on data readiness
6. "If you could only automate ONE thing" recommendation with rationale

When scoring, be honest and conservative. A score of 3 is not "average" — it represents meaningful opportunity.

## Output Format Example

```
| Use Case              | Time | Repeat | Errors | Impact | Data | Composite | Rank |
|-----------------------|------|--------|--------|--------|------|-----------|------|
| Invoice reconciliation|  5   |   4    |   4    |   4    |  4   |   4.30    | 🟢 1 |
| Customer email draft  |  4   |   5    |   3    |   3    |  3   |   3.70    | 🟡 2 |
| Inventory reordering  |  3   |   3    |   2    |   5    |  2   |   3.10    | 🟡 3 |
```
