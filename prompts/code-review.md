# Prompt: Code Review

## Purpose
Review code or a technical design using PPT and First Principles. Evaluate for correctness, maintainability, scalability, configuration-driven design, and CI/CD readiness.

## When to Use
- Reviewing a pull request or technical design
- Auditing existing code for quality issues
- Engineering standards validation

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{code_or_design}}` | The code, PR, or design document to review | (paste code) |
| `{{context}}` | What does this code do? What system does it belong to? | "Invoice processing module for the payments service" |
| `{{review_focus}}` | Any specific concerns or focus areas | "Focus on error handling and external API calls" |

## Prompt

```
You are a senior software engineer conducting a code review using First Principles and PPT analysis.

Code/Design: {{code_or_design}}
Context: {{context}}
Focus: {{review_focus}}

## 1. Correctness
- Does the code do what it claims to do?
- Are there edge cases not handled?
- Are all inputs validated? All error paths handled?
- List specific issues with line numbers or function names.

## 2. Configuration-Driven Design Check
- Are any thresholds, rules, or environment-specific values hardcoded?
- What should be externalized to configuration?
- Is business logic mixed with implementation logic?

## 3. Maintainability (People impact)
- Is the code readable to someone who didn't write it?
- Are functions/classes well-named and single-purpose?
- Is there adequate inline documentation for complex sections?
- What would make this code difficult to modify in 6 months?

## 4. Scalability and Reliability (Technology impact)
- What are the failure modes?
- Does this have appropriate retry logic / timeout handling?
- Does this scale horizontally without design changes?
- Are there resource leaks (connections, file handles, memory)?

## 5. CI/CD and DevOps Readiness
- Is this code testable (unit testable functions, injectable dependencies)?
- Are there tests? If not, what tests should exist?
- Are environment-specific settings externalized (no hardcoded prod URLs)?
- Can this be deployed independently without taking down adjacent systems?

## 6. First Principles Assessment
If you were designing this from scratch today:
- What would you design differently?
- What assumptions baked into this design could be wrong?
- What is the simplest possible implementation that meets the requirements?

## 7. Priority Issues
Rank all identified issues:
- 🔴 Must Fix: Correctness issues, security concerns, breaks CI/CD
- 🟡 Should Fix: Maintainability or scalability concerns
- 🟢 Consider: Minor improvements, style, optional refactors
```

## Expected Output
- Issue list by priority category (🔴 / 🟡 / 🟢)
- Configuration-driven design gaps
- First-principles alternative design (if significant gaps exist)
- Specific actionable fixes with examples
