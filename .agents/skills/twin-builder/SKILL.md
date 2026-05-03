---
name: twin-builder
description: Run a structured five-stage interview with a principal and synthesise a four-file `agent-kernel` twin package (agent-spec.yaml, identity.md, guardrails.md, curated skills). Use when a new principal needs a twin from scratch, when an existing twin needs a re-interview to refresh identity or guardrails, or when a partner wants to demonstrate the kernel methodology end-to-end.
---

# twin-builder

This skill captures how the kernel turns a conversation with a principal into a working twin package. The hosted wizard at `<DEPLOY_URL>/twin-portal/twin-builder` is the canonical implementation; this skill is the methodology and the contract.

## When to use

- A new principal needs a twin and has 10 minutes for an interview.
- An existing twin's `identity.md` or `guardrails.md` is stale and the principal wants to re-record their voice.
- A partner is evaluating the kernel and wants to walk through it with a real principal.

## When not to use

- The principal already has a working twin and only wants to add or remove a skill. Edit `agent-spec.yaml` directly.
- The change is purely operational (a new deployment target, a new audit hook). That belongs in `agent-factory`, not here.

## The five stages

The interviewer moves through these in order, but adaptively. Two-to-four high-signal questions per stage; one follow-up when the signal is thin.

1. **Identity and role** — name, current title, organisation, the few sentences they would use to introduce themselves to a new exec.
2. **Domain expertise** — the two or three subjects they are uncommonly good at, and the kinds of decisions only they get pulled into.
3. **Decision frameworks and mental models** — how they actually think when stakes are high. Push for concrete examples.
4. **Working style and communication preferences** — tone, brevity, formality, what they hate, what they love.
5. **Guardrails and operating principles** — what their twin must never do without checking in, and what it should always escalate.

The interviewer ends with `INTERVIEW_COMPLETE` on its own line when it has enough material across all five stages.

## Output contract

A successful run produces a strict-JSON envelope from the synthesis pass:

```json
{
  "twinId": "kebab-case slug",
  "name": "principal full name",
  "owner": "org or 'Independent'",
  "agentSpecYaml": "<full file contents>",
  "identityMd": "<full file contents>",
  "guardrailsMd": "<full file contents>",
  "skills": [{ "name": "skill-name", "rationale": "one sentence" }]
}
```

Validation rules enforced before the package is offered for download:

- `agentSpecYaml` must begin with `twin-id:` and contain `name:`, `owner:`, `description:`, `decision-style:`, `communication-style:`, `skills:`, `guardrails:`.
- `identityMd` must open with `# Identity`.
- `guardrailsMd` must open with `# Guardrails`.
- `skills` must contain 4 to 8 entries, all drawn from the canonical 22-skill catalog (see [`SKILLS.md`](../../twin-builder/SKILLS.md)).

## Per-section regeneration

Each of the three text sections has its own regenerate path. The regenerator gets the original transcript, the current value, and optional guidance from the principal ("punchier", "less corporate"). It returns a raw string, not JSON.

## Privacy stance

The wizard is local-first: transcript and synthesised package live in the principal's browser. The hosted endpoints are stateless and do not log transcript content. If you fork or self-host the wizard, preserve those properties.

## Handoff to `agent-factory`

The downloaded ZIP unpacks to:

```
your-twin-id/
  agent-spec.yaml
  identity.md
  guardrails.md
  README.md
```

This shape matches what `agent-factory import-kernel` expects. Three commands and the twin is live:

```bash
agent-factory import-kernel ./your-twin-id
agent-factory install your-twin-id
agent-factory serve your-twin-id
```

## Reference

- Live wizard: `<DEPLOY_URL>/twin-portal/twin-builder`
- Source mirror: [`twin-builder/`](../../twin-builder)
- Methodology notes: [`twin-builder/METHODOLOGY.md`](../../twin-builder/METHODOLOGY.md)
- Reference twin: <https://github.com/fszale/digital-twin-filip>
