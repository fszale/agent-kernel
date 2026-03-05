# Prompt: Workflow Design

## Purpose
Design a complete AI workflow blueprint for a specific use case, including triggers, processing steps, outputs, error handling, human review points, and deployment checklist.

## When to Use
- After use case selection and stakeholder alignment
- Before building anything — design first, then build
- When architecting any AI workflow from scratch

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{use_case}}` | What the AI workflow will do | "Auto-draft customer response emails based on inquiry type" |
| `{{target_metric}}` | The metric this improves | "Average response time to customer inquiries" |
| `{{current_tools}}` | Tools the business already uses | "Gmail, CRM, Spreadsheets" |
| `{{data_sources}}` | Available data to feed the AI | "Historical email threads, contact records, FAQ document" |
| `{{staff_roles}}` | Who interacts with this process | "Customer service rep (2 people), sales manager" |
| `{{constraints}}` | Any limitations | "Must reply within 4 hours; legal disclaimers required on quotes" |

## Prompt

```
You are an AI workflow architect designing a production deployment.

Use case: {{use_case}}
Target metric: {{target_metric}}
Existing tools: {{current_tools}}
Available data: {{data_sources}}
Staff involved: {{staff_roles}}
Constraints: {{constraints}}

Design a complete AI workflow blueprint:

## 1. Workflow Overview
- One-paragraph description of what the AI does
- Trigger: What starts the workflow (event, schedule, manual, API call)
- Output: What the workflow produces

## 2. Architecture
Design the workflow as a clear step sequence:
- Step 1: [Trigger / Input capture] → Tool: [X] | Time: [Y]
- Step 2: [Data retrieval / enrichment] → Tool: [X] | Time: [Y]
- Step 3: [AI processing / decision] → Model: [X] | Time: [Y]
- Step 4: [Output generation] → Format: [X] | Time: [Y]
- Step 5: [Human review point] → Interface: [X] | SLA: [Y]
- Step 6: [Action / delivery] → Tool: [X] | Time: [Y]

For each step: inputs, outputs, tools/systems, estimated processing time.

## 3. Integration Plan
- How does this connect to existing tools?
- What APIs, connectors, or automation tools are needed?
- What data access or permissions are required?
- Can any new tooling be avoided?

## 4. Human Review Layer (Required for v1)
- Which outputs require human review before action?
- What does the review interface look like?
- What is the fallback if AI confidence is low?
- What is the SLA for human review?

## 5. Error Handling
- What happens if the trigger fires but data is missing?
- What happens if the AI produces low-quality output?
- What happens if the integration fails?
- Alert mechanism for failures

## 6. Success Criteria
- How do we know this workflow is performing well?
- What data do we collect to feed the Rate of Improvement framework?
- What does "good enough to remove human review" look like?
- Baseline metric value: [establish before go-live]

## 7. Deployment Checklist
Provide a step-by-step go-live checklist.

Format the architecture section with a Mermaid sequence diagram if the flow has ≥3 steps.
```

## Expected Output
- Complete workflow blueprint with step-by-step architecture
- Integration specifications
- Human review layer design
- Error handling matrix
- Success criteria with Rate of Improvement baseline
- Deployment checklist

## Tips
- Start simple: Minimal Viable Automation
- Prefer existing tools over new platforms
- Always include human review in v1; earn the right to remove it later
