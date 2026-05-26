# Twin Builder Methodology

This document explains the design choices behind the Twin Builder. It is intended for engineers extending the builder, partners reviewing the methodology, and anyone deploying agent-kernel-style twins for principals.

## Why a conversation, not a form

Forms over-collect and under-collect at the same time. Most fields go unused; the few that matter (decision style, communication style, guardrails) need follow-up to be useful. A free-form conversation, governed by a structured topic stack, lets the system ask exactly two-to-four high-signal questions per area and follow up only when the signal is thin.

## Five-stage interview

Stages are deliberately ordered to ride down a difficulty curve:

1. **Identity** — easiest. Establishes voice and warms the principal up.
2. **Domain expertise** — concrete. Surfaces examples and vocabulary.
3. **Decision frameworks** — abstract. Now that the principal is talking, they can articulate how they think.
4. **Working style** — preference-driven. Builds the writing voice the twin will inherit.
5. **Guardrails** — the strongest signal. By the time we get here, the principal has enough trust to be candid about what the twin must never do.

Stage progression is approximated client-side from the count of user turns, used only for the progress bar — the model controls the actual pacing.

## Conative profile input

When a principal has a Kolbe-style conative profile, treat it as source evidence for how the twin should act by default. It should not replace the interview; it should sharpen stages 3-5 by making the principal's natural action sequence explicit.

The synthesis pass should translate the profile into:

- a compact `conative-profile` block in `agent-spec.yaml`
- operating-sequence language for `identity.md`
- do / don't rules and delegation triggers for `guardrails.md`
- evaluation scenarios that catch inauthentic output under pressure

Conative evidence should stay distinct from cognitive expertise and affective preference. The profile says how the principal naturally takes action, not what they know or what they emotionally prefer.

## Sentinel marker for completion

The interviewer ends with `INTERVIEW_COMPLETE` on its own line when it has enough material. This gives the client a clean handoff signal without parsing model intent.

## Two-pass synthesis

Synthesis is a separate model call so that:

- The interview can stay in natural prose without the model trying to draft YAML mid-conversation.
- The synthesis model gets a clean, focused job: read the transcript, return strict JSON.
- The synthesis prompt can demand exact keys and ordering for `agent-spec.yaml`, while the chat model stays warm.

The JSON envelope is validated client-side: the YAML must start with `twin-id:` and contain the canonical key set; `identity.md` must open with `# Identity`; `guardrails.md` must open with `# Guardrails`. The user sees inline warnings before downloading.

## Section regeneration

Each of the three text sections has its own regenerate endpoint. The regenerator gets the original transcript, the current value, and optional guidance from the principal ("punchier", "less corporate"). It returns a raw string, not JSON, to keep the contract simple and the latency low.

## Local-first state

The transcript and the synthesised package live in `localStorage` under namespaced keys. The chat endpoint and the synthesis endpoint both receive the transcript as the model context for each call, but the server is stateless: it does not persist the conversation, the conversation id, or any package material. No transcript content is logged.

## Why these 23 skills

The catalog is intentionally biased toward technology-leadership twins — the audience SolidCage actually serves. It is broad enough to fit non-CTO principals (advisors, founders, operators) but narrow enough that the synthesiser can pick a coherent 4-8 skills without thrashing.

The catalog is not the final word on a twin. After deployment, principals add bespoke skills and remove ones that don't earn their keep.

The `conative-operating-system` catalog entry is selected when the principal provides Kolbe-style evidence or when the interview strongly surfaces a repeatable action pattern. It should produce prompt, tool, delegation, and evaluation changes, not just a personality summary.

## Output shape

The ZIP layout matches what `agent-factory import-kernel` expects:

```
your-twin-id/
  agent-spec.yaml
  identity.md
  guardrails.md
  README.md
```

This shape is the contract between the builder and the runtime. Changing it requires coordinated updates to both repositories.

## Observability

Every server call is logged with the conversation id (assigned client-side) and the operation (`chat`, `synthesize`, `regenerate`). No transcript content is logged; only counts and timings. This is enough to spot issues (rate limits, model errors) without holding sensitive principal material on the server.

## Failure modes and what we do about them

- **Model returns malformed JSON during synthesis** — the client falls back to defaults for missing fields and surfaces validation warnings; the user can always re-synthesise.
- **Stream interrupted mid-chat** — the client resumes from the saved transcript on the next turn; partial assistant chunks are dropped.
- **localStorage unavailable** — the builder still runs but cannot resume after a refresh. The synthesise step still works for the current session.

## Roadmap

- A second pass that interviews the principal's chief of staff or longtime collaborator to triangulate working-style claims.
- Pluggable skill catalogs so industry-specific kernels (legal, healthcare, finance) can ship their own catalogs without forking the builder.
- A diff view between successive synthesises so the principal can see what changed when they tweak answers and re-run.
