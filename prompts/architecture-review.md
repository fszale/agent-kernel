# Architecture & System Review

**Purpose:** Evaluate an existing prototype, repository, or multi-agent system for architectural integrity, production readiness, and strategic staging. 
**Output:** A structured gap analysis and a prioritized roadmap for adoption.

---

Please apply the contents of the agent-kernel to review the adjacent project in this workspace. 

From what I understand, this project is a {{project_description}}. 
The team working on this is {{team_charter}}.

Currently, the project is structured as a prototype or early build, but we need to know what it takes to make it a reliable platform.

### Part 1: Deep Architectural Review

Use the `agentic-system-review` skill to audit this repository. Specifically, identify any major gaps across these dimensions:

1. **Self-Improvement:** How is it learning or improving over time? Are LLM decisions fed back into the system?
2. **Memory & Context:** How is it managing state? Is there a shared context or just isolated memory?
3. **Guardrails & HITL:** Where is the human-in-the-loop that can quickly pause, override, or provide feedback to operations? 
4. **Simulation Boundaries:** Are there any mocked/simulated components masquerading as production readiness?

Please provide a prioritized list of findings (Critical, High, Medium, Low).

### Part 2: Strategic Advisory Roadmap

Based on the review above, assume the team is trying to focus on everything at once and looking for validation of their broad architecture. 

Use the `staged-validation` skill to advise this team on how to proceed. 

Please provide a phased validation roadmap that applies the Pareto principle (80/20) and helps them prove out the most valuable, highest-risk components first (depth), rather than trying to build the whole system at once (breadth).
