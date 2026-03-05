#!/usr/bin/env python3
"""
embed_diagrams.py

Reads diagrams/registry.json, then for each diagram and each file listed in
its `used_in` array, replaces content between diagram markers with a
Mermaid fenced code block built from the corresponding .mmd source file.

Marker format (HTML comments, safe in any Markdown renderer):
    <!-- DIAGRAM: <id> START -->
    <!-- DIAGRAM: <id> END -->

Usage:
    python3 scripts/embed_diagrams.py

Options:
    --dry-run   Print diffs but do not write files
    --verbose   Show per-file progress

Requirements: Python 3.8+, no external dependencies.
"""

import argparse
import json
import os
import re
import sys

REGISTRY_PATH = os.path.join(os.path.dirname(__file__), "..", "diagrams", "registry.json")
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def load_registry():
    with open(REGISTRY_PATH, "r") as f:
        return json.load(f)


def load_diagram(mmd_path):
    full_path = os.path.join(REPO_ROOT, mmd_path)
    if not os.path.exists(full_path):
        print(f"  ⚠️  Diagram file not found: {full_path}", file=sys.stderr)
        return None
    with open(full_path, "r") as f:
        return f.read().strip()


def build_block(diagram_id, mmd_content):
    """Build the full replacement block including markers."""
    return (
        f"<!-- DIAGRAM: {diagram_id} START -->\n"
        f"```mermaid\n"
        f"{mmd_content}\n"
        f"```\n"
        f"<!-- DIAGRAM: {diagram_id} END -->"
    )


def embed_diagram_in_file(file_path, diagram_id, mmd_content, dry_run=False, verbose=False):
    """Replace diagram markers in the given file with the current diagram content."""
    full_path = os.path.join(REPO_ROOT, file_path)
    if not os.path.exists(full_path):
        if verbose:
            print(f"  ⏭  Skipping (not found): {file_path}")
        return False

    with open(full_path, "r") as f:
        original = f.read()

    pattern = re.compile(
        rf"<!-- DIAGRAM: {re.escape(diagram_id)} START -->.*?<!-- DIAGRAM: {re.escape(diagram_id)} END -->",
        re.DOTALL,
    )

    replacement = build_block(diagram_id, mmd_content)
    updated = pattern.sub(replacement, original)

    if updated == original:
        if verbose:
            print(f"  ℹ  No markers found (skipping): {file_path}")
        return False

    if dry_run:
        print(f"  🔍 [DRY RUN] Would update: {file_path}")
    else:
        with open(full_path, "w") as f:
            f.write(updated)
        if verbose:
            print(f"  ✅ Updated: {file_path}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Embed Mermaid diagrams into Markdown files.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change without writing")
    parser.add_argument("--verbose", action="store_true", help="Print per-file progress")
    args = parser.parse_args()

    registry = load_registry()
    total_updates = 0

    for diagram in registry.get("diagrams", []):
        diagram_id = diagram["id"]
        mmd_path = diagram["file"]
        used_in = diagram.get("used_in", [])

        print(f"\n📊 Diagram: {diagram_id}")
        mmd_content = load_diagram(mmd_path)
        if mmd_content is None:
            print(f"  ❌ Skipping {diagram_id} — source file missing")
            continue

        for target_file in used_in:
            updated = embed_diagram_in_file(
                target_file, diagram_id, mmd_content, dry_run=args.dry_run, verbose=args.verbose
            )
            if updated:
                total_updates += 1

    print(f"\n✅ Done — {total_updates} embed(s) {'would be ' if args.dry_run else ''}updated.")


if __name__ == "__main__":
    main()
