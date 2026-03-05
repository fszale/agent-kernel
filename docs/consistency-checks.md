# docs/consistency-checks.md

# Consistency Check Rules

This document defines the rules used by the GitHub `skill-consistency-check.yml` workflow and the `/run-consistency-check` agent workflow.

## Required Frontmatter Fields (SKILL.md)

Every `skills/*/SKILL.md` must have all four fields:

| Field | Type | Rule |
|---|---|---|
| `name` | string | Must match the parent directory name (kebab-case) |
| `description` | string | One sentence, under 150 characters, must end with `.` |
| `when-to-use` | string | Must be specific — not "any time" or "as applicable" |
| `principles` | list | Must list at least one principle from PHILOSOPHY.md |

**Violation → CI failure.**

## Required Prompt Sections

Every `prompts/*.md` must have:

| Section | Required? |
|---|---|
| `## Purpose` | ✅ Yes |
| `## When to Use` | ✅ Yes |
| `## Variables` (with table) | ✅ Yes |
| `## Prompt` (fenced code block) | ✅ Yes |
| `## Expected Output` | ✅ Yes |
| `## Tips` | Optional |

**Missing section → CI failure.**

## Variable Format

All interpolated variables in prompts must use `{{double_curly_braces}}`.

| Pattern | Status |
|---|---|
| `{{variable_name}}` | ✅ Correct |
| `{single_braces}` | ❌ Invalid |
| `[VARIABLE]` | ❌ Invalid |
| `<VARIABLE>` | ❌ Invalid |

## README Index Completeness

`README.md` must reference every file in:
- `skills/` — at least one row in the Quick Start table
- `prompts/` — at least one reference
- `templates/` — at least one reference

**Missing entry → documentation-sync workflow flags it.**

## YAML Template Validity

All `.yaml` files in `templates/` and `.github/workflows/` must:
- Be valid YAML (tested with `npx js-yaml`)
- Have the required comment header block

## Cross-Reference Integrity

All internal markdown links `[text](path.md)` must point to a file that exists. Broken links are flagged by the consistency check.

## No Brand-Specific Content

The following patterns are banned in any non-seed file:
- Specific company or brand names in operational context
- Hardcoded credentials or API keys
- Environment-specific URLs (use `{{variable}}` format instead)

## Agent Spec Required Fields

Any `agent-spec-*.yaml` file must include:
- `decision_rationale.universal_required_fields` containing `justification` and `reasoning_summary`
- `discovery.capabilities` (at least one entry)
- `actions` (at least one entry with `risk_class` and `autonomy_level`)
- `hitl.approvals`
