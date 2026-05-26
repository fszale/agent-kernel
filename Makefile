# agent-kernel Makefile
# ──────────────────────────────────────────────────────────────────────────────
# Targets:
#   make validate-mermaid      Validate all .mmd files for syntax errors
#   make embed-diagrams        Embed .mmd content into Markdown files
#   make check-diagrams        Fail if embedded diagrams are out of date
#   make consistency-check     Run repository contract validation
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
		OUT="/tmp/agent-kernel-mermaid-$$(basename "$$f" .mmd).svg"; \
		if command -v mmdc >/dev/null 2>&1; then \
			if ! mmdc -i "$$f" -o "$$OUT" 2>/dev/null; then \
				echo "  ❌ Syntax error in: $$f"; \
				FAILED=1; \
			else \
				echo "  ✅ Valid: $$f"; \
			fi; \
		else \
			if ! npx --yes @mermaid-js/mermaid-cli -i "$$f" -o "$$OUT" 2>/dev/null; then \
				echo "  ❌ Syntax error in: $$f"; \
				FAILED=1; \
			else \
				echo "  ✅ Valid: $$f"; \
			fi; \
		fi; \
		rm -f "$$OUT"; \
	done; \
	if [ $$FAILED -ne 0 ]; then echo "❌ Mermaid validation FAILED"; exit 1; fi; \
	echo "✅ All Mermaid diagrams valid."

# ── Diagram Embedding ─────────────────────────────────────────────────────────

embed-diagrams:
	@echo "📊 Embedding diagrams into Markdown files..."
	@python3 scripts/embed_diagrams.py --verbose

check-diagrams:
	@echo "🔍 Checking diagram sync..."
	@python3 scripts/embed_diagrams.py --check --verbose

# ── Consistency Checks ────────────────────────────────────────────────────────

consistency-check:
	@echo "🔍 Running repository contract checks..."
	@python3 scripts/validate_contracts.py

# ── Full Suite ────────────────────────────────────────────────────────────────

all-checks: consistency-check validate-mermaid check-diagrams
	@echo "✅ All checks passed."
