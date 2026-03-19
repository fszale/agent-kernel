#!/usr/bin/env python3
"""
Repository-level contract validation for the agent-kernel.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

SKILL_FIELDS = ("name", "description", "when-to-use", "principles")
PROMPT_SECTIONS = ("## Purpose", "## When to Use", "## Variables", "## Prompt", "## Expected Output")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)#]+\.md)\)")
SKILL_ITEM_PATTERN = re.compile(r'^\s*-\s*"([^"]+)"')
PROVIDER_MODEL_PATTERN = re.compile(r'"(gemini|gpt|claude|llama)[^"]*"', re.IGNORECASE)
COUNT_CLAIM_PATTERN = re.compile(r"(\d+)\s+Mermaid\s+\.mmd")


def repo_glob(*patterns: str) -> list[Path]:
    results: list[Path] = []
    for pattern in patterns:
        results.extend(sorted(REPO_ROOT.glob(pattern)))
    return results


def rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def add_issue(issues: list[str], path: Path, message: str, line_no: int | None = None) -> None:
    location = rel(path)
    if line_no is not None:
        location = f"{location}:{line_no}"
    issues.append(f"{location}: {message}")


def validate_skills(issues: list[str]) -> None:
    for skill_file in repo_glob("skills/*/SKILL.md"):
        text = skill_file.read_text()
        for field in SKILL_FIELDS:
            if not re.search(rf"^{re.escape(field)}:", text, flags=re.MULTILINE):
                add_issue(issues, skill_file, f"missing frontmatter field '{field}'")
        for section in ("## Agent Instructions", "## Output Format"):
            if section not in text:
                add_issue(issues, skill_file, f"missing section '{section}'")


def validate_prompts(issues: list[str]) -> None:
    for prompt_file in repo_glob("prompts/*.md"):
        text = prompt_file.read_text()
        for section in PROMPT_SECTIONS:
            if section not in text:
                add_issue(issues, prompt_file, f"missing section '{section}'")


def validate_links(issues: list[str]) -> None:
    for path in repo_glob("*.md", "docs/**/*.md", "skills/**/*.md", "prompts/*.md", "templates/*.md", ".agents/**/*.md"):
        in_code_block = False
        for line_no, raw_line in enumerate(path.read_text().splitlines(), start=1):
            line = raw_line
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue
            line = re.sub(r"`[^`]*`", "", line)
            for match in MARKDOWN_LINK_PATTERN.finditer(line):
                target = match.group(1)
                if "://" in target:
                    continue
                target_path = (path.parent / target).resolve()
                if not target_path.exists():
                    add_issue(issues, path, f"broken markdown link to '{target}'", line_no)


def validate_provider_neutral_template(issues: list[str]) -> None:
    template = REPO_ROOT / "templates/agent-spec-template.yaml"
    for line_no, line in enumerate(template.read_text().splitlines(), start=1):
        if PROVIDER_MODEL_PATTERN.search(line):
            add_issue(issues, template, "provider-specific model ID in generic template", line_no)


def validate_skill_lists(issues: list[str]) -> None:
    valid_skills = {path.parent.name for path in repo_glob("skills/*/SKILL.md")}
    for path in repo_glob("templates/agent-spec*.yaml"):
        in_skills_block = False
        for line_no, line in enumerate(path.read_text().splitlines(), start=1):
            stripped = line.strip()
            if stripped.startswith("skills:"):
                in_skills_block = True
                continue
            if in_skills_block and re.match(r"^[A-Za-z_][A-Za-z0-9_]*:", stripped):
                in_skills_block = False
            if not in_skills_block:
                continue
            match = SKILL_ITEM_PATTERN.match(line)
            if not match:
                continue
            value = match.group(1)
            if "{{" in value:
                continue
            if "/" in value:
                add_issue(issues, path, f"skill reference must use bare skill ID, found '{value}'", line_no)
                continue
            if value not in valid_skills and value != "relevant-domain-skill":
                add_issue(issues, path, f"unknown skill reference '{value}'", line_no)


def validate_rationale_contract(issues: list[str]) -> None:
    files = repo_glob(
        "README.md",
        "AGENTS.md",
        "PHILOSOPHY.md",
        "docs/**/*.md",
        ".agents/**/*.md",
        "skills/**/*.md",
        "prompts/*.md",
        "templates/*",
        "diagrams/*.mmd",
    )
    banned_patterns = (
        r"\breasoning_summary\b",
        r"chain-of-thought",
        r"chain of thought",
        r"shared/",
        r"\bguardrail_evaluation\b",
    )
    allowed_guardrail_paths = {
        REPO_ROOT / "PHILOSOPHY.md",
        REPO_ROOT / "prompts/action-proposal.md",
        REPO_ROOT / "skills/hitl-and-guardrails/SKILL.md",
        REPO_ROOT / "templates/agent-config-template.yaml",
        REPO_ROOT / "templates/agent-spec-template.yaml",
        REPO_ROOT / "templates/agent-spec-domain-template.yaml",
    }

    for path in files:
        for line_no, line in enumerate(path.read_text().splitlines(), start=1):
            for pattern in banned_patterns:
                if pattern == r"\bguardrail_evaluation\b" and path in allowed_guardrail_paths:
                    continue
                if re.search(pattern, line):
                    add_issue(issues, path, f"deprecated contract pattern '{pattern}'", line_no)


def validate_diagram_count_claims(issues: list[str]) -> None:
    actual_count = len(repo_glob("diagrams/*.mmd"))
    files_to_check = (
        REPO_ROOT / "README.md",
        REPO_ROOT / "CONTEXT.md",
        REPO_ROOT / ".agents" / "skills" / "project-navigation.md",
    )
    for path in files_to_check:
        for line_no, line in enumerate(path.read_text().splitlines(), start=1):
            match = COUNT_CLAIM_PATTERN.search(line)
            if not match:
                continue
            claimed_count = int(match.group(1))
            if claimed_count != actual_count:
                add_issue(
                    issues,
                    path,
                    f"diagram count claim is {claimed_count}, actual is {actual_count}",
                    line_no,
                )


def validate_template_authoring_policy(issues: list[str]) -> None:
    add_template = REPO_ROOT / ".agents" / "workflows" / "add-template.md"
    contributing = REPO_ROOT / "docs" / "contributing.md"
    add_template_text = add_template.read_text()
    contributing_text = contributing.read_text()

    requires_placeholders = "{{variable_name}}" in add_template_text
    requires_blanks = "____________________" in add_template_text
    contributing_requires_blanks = "____________________" in contributing_text

    # We standardize markdown templates on blank-fill sections.
    if requires_placeholders:
        add_issue(
            issues,
            add_template,
            "markdown template policy should use blank-fill sections, not '{{variable_name}}' placeholders",
        )
    if not requires_blanks:
        add_issue(
            issues,
            add_template,
            "missing explicit blank-fill guidance for markdown templates",
        )
    if not contributing_requires_blanks:
        add_issue(
            issues,
            contributing,
            "missing blank-fill guidance for markdown templates",
        )


def validate_diagram_drift(issues: list[str]) -> None:
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "embed_diagrams.py"), "--check"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        output = (result.stdout + result.stderr).strip().splitlines()
        issues.append(f"diagrams: {output[-1] if output else 'diagram drift detected'}")


def main() -> int:
    issues: list[str] = []
    validate_skills(issues)
    validate_prompts(issues)
    validate_links(issues)
    validate_provider_neutral_template(issues)
    validate_skill_lists(issues)
    validate_rationale_contract(issues)
    validate_diagram_count_claims(issues)
    validate_template_authoring_policy(issues)
    validate_diagram_drift(issues)

    if issues:
        print("Contract validation failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("All contract checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
