# agent-kernel Makefile
# ──────────────────────────────────────────────────────────────────────────────
# Targets:
#   make validate-mermaid      Validate all .mmd files for syntax errors
#   make embed-diagrams        Embed .mmd content into Markdown files
#   make check-diagrams        Dry-run diagram embed (shows what would change)
#   make consistency-check     Validate SKILL.md frontmatter + prompt sections
#   make all-checks            Run all validation targets
# ──────────────────────────────────────────────────────────────────────────────

.PHONY: validate-mermaid embed-diagrams check-diagrams consistency-check all-checks

# ── Mermaid Validation ────────────────────────────────────────────────────────
# Uses mmdc (mermaid-js/mermaid-cli) if installed globally, otherwise falls
# back to npx. Compiles each .mmd file to /dev/null; fails on syntax errors.

validate-mermaid:
	@echo "🔍 Validating Mermaid diagrams..."
	@FAILED=0; \
	for f in diagrams/*.mmd; do \
		if command -v mmdc >/dev/null 2>&1; then \
			if ! mmdc -i "$$f" -o /dev/null 2>/dev/null; then \
				echo "  ❌ Syntax error in: $$f"; \
				FAILED=1; \
			else \
				echo "  ✅ Valid: $$f"; \
			fi; \
		else \
			if ! npx --yes @mermaid-js/mermaid-cli mmdc -i "$$f" -o /dev/null 2>/dev/null; then \
				echo "  ❌ Syntax error in: $$f"; \
				FAILED=1; \
			else \
				echo "  ✅ Valid: $$f"; \
			fi; \
		fi; \
	done; \
	if [ $$FAILED -ne 0 ]; then echo "❌ Mermaid validation FAILED"; exit 1; fi; \
	echo "✅ All Mermaid diagrams valid."

# ── Diagram Embedding ─────────────────────────────────────────────────────────

embed-diagrams:
	@echo "📊 Embedding diagrams into Markdown files..."
	@python3 scripts/embed_diagrams.py --verbose

check-diagrams:
	@echo "🔍 Checking diagrams (dry run)..."
	@python3 scripts/embed_diagrams.py --dry-run --verbose

# ── Consistency Checks ────────────────────────────────────────────────────────

consistency-check:
	@echo "🔍 Running skill and prompt consistency checks..."
	@FAILED=0; \
	for f in skills/*/SKILL.md; do \
		for field in "^name:" "^description:" "^when-to-use:" "^principles:"; do \
			if ! grep -q "$$field" "$$f"; then \
				echo "  ❌ MISSING '$$field' in $$f"; \
				FAILED=1; \
			fi; \
		done; \
	done; \
	for f in prompts/*.md; do \
		for section in "## Variables" "## Expected Output"; do \
			if ! grep -q "$$section" "$$f"; then \
				echo "  ❌ MISSING '$$section' in $$f"; \
				FAILED=1; \
			fi; \
		done; \
	done; \
	if [ $$FAILED -ne 0 ]; then echo "❌ Consistency check FAILED"; exit 1; fi; \
	echo "✅ All consistency checks passed."

# ── Full Suite ────────────────────────────────────────────────────────────────

all-checks: consistency-check validate-mermaid
	@echo "✅ All checks passed."
