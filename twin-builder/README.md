# Twin Builder

The Twin Builder is the SolidCage `agent-kernel` companion that turns a 10-minute conversation with a principal into a working twin package: an `agent-spec.yaml`, `identity.md`, `guardrails.md`, and a curated selection from the kernel skill catalog. The output is shaped for the [`agent-factory`](https://github.com/fszale/agent-factory) installer so that twins built here can be deployed without manual translation.

The reference twin built around Filip Szalewicz (Head of Engineering, AI transformation) lives in [`digital-twin-filip`](https://github.com/fszale/digital-twin-filip). The Twin Builder uses that twin's structure as its target shape.

## How it works

A live AI interviewer moves the principal through five topic areas, in order, but adaptively:

1. **Identity and role** — name, role, organisation, the elevator paragraph.
2. **Domain expertise** — the two or three subjects they are uncommonly good at.
3. **Decision frameworks and mental models** — how they actually think when stakes are high.
4. **Working style and communication preferences** — tone, brevity, what they hate, what they love.
5. **Guardrails and operating principles** — what the twin must never do without checking in, and what it should always escalate.

The interviewer asks two-to-four high-signal questions per area, follows up only when a thin answer needs depth, and emits a sentinel marker (`INTERVIEW_COMPLETE`) when it has enough material across all five areas.

## What gets produced

A synthesis pass converts the transcript into a strict-JSON envelope which the client renders as four downloadable files:

- `agent-spec.yaml` — machine-readable twin definition (`twin-id`, `name`, `owner`, `description`, `decision-style`, `communication-style`, `skills`, `guardrails`)
- `identity.md` — 200-400 word first-person narrative
- `guardrails.md` — 6-10 explicit rules
- `README.md` — a short deploy guide that ships inside the ZIP

Each section is editable in the preview, and each section can be regenerated independently with optional guidance.

## Skill catalog

The twin builder maps interview material against the agent-kernel skill catalog. Skills selected by the synthesiser are recorded in `agent-spec.yaml` as a curated subset (typically 4-8 skills), each with a one-sentence rationale.

See [`SKILLS.md`](./SKILLS.md) for the full 22-skill catalog.

## Deploying

After downloading the ZIP from the builder, three commands take the package live on `agent-factory`:

```bash
agent-factory import-kernel ./your-twin-id
agent-factory install your-twin-id
agent-factory serve your-twin-id
```

## Privacy

The transcript is held in `localStorage` and is sent to the chat and synthesis endpoints only as model context for each call. The server is stateless and does not persist the conversation. No account is required.

## Live builder

The hosted version of the Twin Builder lives inside the Digital Twin Factory portal:

`<DEPLOY_URL>/twin-portal/twin-builder`

The implementation is published in the [`digital-twin-factory`](https://github.com/fszale/digital-twin-factory) repository, and `agent-factory` (the runtime) lives at <https://github.com/fszale/agent-factory>.

## Want it done for you?

Filip operates this end-to-end as part of his Head of Engineering and fractional-CTO engagements. Book a session at [solidcage.com](https://solidcage.com).
