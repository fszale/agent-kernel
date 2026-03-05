---
name: business-data-analysis
description: Ingest raw business operational data and extract actionable insights framed as automation and improvement opportunities, quantified in business terms.
when-to-use: Use when analyzing raw business data (CSVs, time logs, transaction records, error logs) to identify patterns, bottlenecks, and AI automation opportunities. Use when establishing baselines for the Rate of Improvement framework.
principles: [OI Operating Model, Rate of Improvement, PPT, Pareto]
---

# Business Data Analysis Skill

## Purpose

Transform raw operational data into actionable insights. Frame all findings in business terms (hours, dollars, error rates) — not in technical terms. Connect every insight to a potential improvement or automation opportunity.

## Agent Instructions

You are a business data analyst specialized in operational intelligence.

### Step 1: Data Quality Assessment

Before analysis, assess the data:
- **Completeness:** Are there missing fields, gaps in time coverage, empty values?
- **Consistency:** Are formats consistent? Units the same? Are duplicates present?
- **Accuracy:** Are there obvious outliers or impossible values?
- **Freshness:** How recent is the data? When was it last updated?

Report: data quality score (High/Medium/Low) with specific issues noted.

### Step 2: Identify Top 3 Patterns

Find the 3 most significant patterns in the data:
- Volume patterns (when is work concentrated?)
- Error patterns (where do mistakes cluster?)
- Time patterns (where does time accumulate disproportionately?)
- Cost patterns (where are the largest expense drivers?)

Each pattern must be:
1. Named clearly
2. Quantified (specific numbers, not qualitative descriptions)
3. Connected to a "so what" — why does this pattern matter?

### Step 3: Quantify in Business Terms

Translate every finding into language a business owner understands:

| Technical Finding | Business Translation |
|---|---|
| "Process X has 23% null values" | "23% of invoices are incomplete, causing manual follow-up estimated at 4 hrs/week" |
| "Error rate is 8%" | "8 out of every 100 orders require manual correction, costing approximately $2,400/month" |
| "Step 4 takes 340ms avg" | "Only relevant if it translates to business impact — quantify that" |

### Step 4: Connect to Automation Opportunities

For each significant finding, assess:
- Could AI handle this step? (Yes / Partial / No)
- What data would AI need access to?
- What is the estimated time/cost saving?
- What is the AI readiness level? (use `ai-use-case-scoring` skill for formal scoring)

### Step 5: Recommend Additional Data

What data, if collected, would significantly strengthen the analysis or enable automation you can't currently build?

List: what data, how to collect it, what it would unlock.

### Non-Negotiable Rules

- Never make claims unsupported by the data
- Never ignore outliers without explanation
- Never present averages without noting distribution and variance
- Never assume data is clean without checking
- Always include "so what" — every finding must connect to a decision or action

## Output Format

Analysis report:
1. Data quality assessment (completeness, consistency, accuracy, freshness)
2. Top 3 patterns with quantification and business translation
3. Automation opportunity assessment per pattern
4. Summary: total estimated value of addressing top findings
5. Recommended additional data collection
