# Prompt: Process Audit

## Purpose
Analyze a business process end-to-end to identify automation opportunities, inefficiencies, and data flow patterns.

## When to Use
- Before designing any AI or automation solution
- When a process is known to have problems but the root cause is unclear
- When establishing baseline metrics for the Rate of Improvement framework

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{business_name}}` | Name of the business or team | "Acme Services" |
| `{{process_name}}` | The process being audited | "Invoice reconciliation" |
| `{{process_description}}` | Brief description of what the process does | "Matching purchase orders to invoices and verifying amounts" |
| `{{staff_involved}}` | Roles involved in this process | "AP clerk, department managers" |
| `{{frequency}}` | How often this process runs | "200 invoices/week" |
| `{{known_pain_points}}` | Issues already identified | "Takes 14 hours/week, frequent errors cause payment delays" |

## Prompt

```
You are an operational analyst conducting a process audit.

Business: {{business_name}}
Process: {{process_name}}
Description: {{process_description}}
Staff involved: {{staff_involved}}
Frequency: {{frequency}}
Known pain points: {{known_pain_points}}

## 1. Process Map
Break down the process into sequential steps. For each step:
- What happens
- Who does it (role, not person)
- Estimated time per occurrence
- Tools/systems used
- Data inputs and outputs

## 2. Bottleneck Analysis
Identify steps where:
- Time accumulates disproportionately
- Errors are most likely to occur
- Manual effort is highest relative to value
- Handoffs between people/systems create delays
- Work queues form

## 3. Automation Opportunity Assessment
For each bottleneck:
- Could AI handle this step? (Yes / Partial / No)
- What type of AI capability is needed? (Classification, extraction, generation, prediction, routing)
- What data would AI need access to?
- Estimated time savings (hours/week)
- Estimated error reduction

## 4. Risk Factors
- Data quality issues that would impede automation
- Regulatory or compliance constraints
- Staff adoption risk (estimate: Low/Medium/High)
- Integration complexity

## 5. Recommendations
Rank the top 3 automation opportunities by:
- Expected impact (hours/week saved × quality improvement)
- Implementation feasibility
- Speed to first value

Format as: Priority 1 / Priority 2 / Priority 3 with rationale.
```

## Expected Output
- Step-by-step process map with time and role annotations
- Bottleneck heat map (table format, scored by impact)
- Ranked automation opportunities with feasibility scores
- Risk register
- Top 3 recommendations with rationale

## Tips
- Observe the process directly (Shadow Walk) before filling in the variables
- More raw detail in the variables → better analysis
- Re-run after deployment to compare before/after process maps
