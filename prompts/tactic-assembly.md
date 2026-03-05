# Prompt: Tactic Assembly

## Purpose
Bundle two or more related actions into a coherent tactic — with a strong intent field, execution mode, and strategy alignment — when the combined effect in known or expected to be greater than the individual effects.

## When to Use
- When multiple actions share a logical dependency
- Before submitting a bundle for human approval
- When reviewing whether a set of proposed actions should be bundled or kept standalone

## Variables

| Variable | Description | Example |
|---|---|---|
| `{{strategy}}` | The linked strategy this tactic advances | "Reduce invoice processing time by 60%" |
| `{{proposed_actions}}` | List of actions being considered for bundling | "Pause manual review step + Activate AI classification + Notify team" |
| `{{context}}` | Why these actions are being considered together | "All touch the same invoice workflow and must happen in the same deployment window" |

## Prompt

```
You are a tactic architect. Evaluate whether the proposed actions should be bundled into a tactic, and if so, design the tactic completely.

Strategy: {{strategy}}
Proposed actions: {{proposed_actions}}
Context: {{context}}

## Step 1: Bundling Validation

Assess each potential bundling rationale:

| Type | Does it Apply? | Evidence |
|---|---|---|
| Sequential dependency (B requires A) | Y/N | |
| Risk mitigation (safer together) | Y/N | |
| Timing sensitivity (must happen same window) | Y/N | |
| Cross-domain coordination | Y/N | |

Verdict: Should these be bundled? If NO, explain which actions should be standalone and why.

## Step 2: Tactic Design (if bundling is justified)

**Tactic title**: [Clear, action-oriented name]

**Intent** (the most critical field — write this carefully):
WHY must these actions happen together? State the specific causal reason. What would go wrong if only some actions were executed?
Format: "[Action A] and [Action B] must happen together because [specific causal reason]. Without [A], [B] would cause [negative outcome]. Together, they achieve [combined goal]."

**Execution mode**: Sequential / Parallel / Phased
- Rationale for this mode selection

**Strategy alignment**: HOW does this tactic execute the linked strategy? Be specific.

**Component actions** (list each with):
- Action description
- Role in the tactic (tactic_alignment)
- Risk class: Low / Medium / High
- Estimated value

**Combined assessment**:
- Combined expected value (sum or explain synergistic effect)
- Combined risk class (highest individual, or escalate if compounding)

## Step 3: Approval Context

Write the 2-sentence summary a human approver will read to evaluate this tactic:
"This tactic [does what] by [combining which actions]. Approving it means [specific combined outcome] because [why they must go together]."
```

## Expected Output
- Bundling validation with evidence
- Complete tactic design (if justified)
- Strong intent field suitable for human review
- Approval context summary

## Tips
- If bundling rationale is not clear, the actions should stay standalone
- Always write the intent field last — it should synthesize everything else
- A rejected tactic (not approved) returns to individual actions, not to a redesigned tactic
