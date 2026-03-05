---
description: how to run a consistency check on the agent-kernel repository
---

# Run Consistency Check Workflow

Use this workflow to audit the repository for missing fields, broken cross-references, and structural violations.

## Step 1: Verify all SKILL.md files have required frontmatter

Check every `skills/*/SKILL.md` for the required frontmatter fields:

```bash
# Find SKILL.md files missing 'name:' frontmatter
find skills -name "SKILL.md" | xargs grep -L "^name:"
# Should return empty

# Find SKILL.md files missing 'description:' frontmatter
find skills -name "SKILL.md" | xargs grep -L "^description:"
# Should return empty

# Find SKILL.md files missing 'when-to-use:' frontmatter
find skills -name "SKILL.md" | xargs grep -L "^when-to-use:"
# Should return empty
```

## Step 2: Verify all prompts have required sections

Check every `prompts/*.md` for required sections:

```bash
# Prompts missing Variables section
grep -rL "## Variables" prompts/
# Should return empty

# Prompts missing Expected Output section
grep -rL "## Expected Output" prompts/
# Should return empty
```

## Step 3: Check README index completeness

Verify every file in `skills/`, `prompts/`, and `templates/` is mentioned in `README.md`:

```bash
# List all skill directories
ls skills/
# Then confirm each appears in README.md
grep -c "skill-name" README.md
```

## Step 4: Check for broken cross-references

Scan for internal links that reference non-existent files:

```bash
# Find markdown links and check targets exist
grep -r "\[.*\](.*\.md)" . --include="*.md" | grep -v "^Binary"
```

Manually verify each cross-reference link points to a file that exists.

## Step 5: Validate YAML templates

```bash
# Validate YAML syntax in templates
npx js-yaml templates/agent-config-template.yaml
npx js-yaml templates/agent-spec-template.yaml
npx js-yaml .github/workflows/*.yml
# All should return without errors
```

## Step 6: Verify no brand-specific content

```bash
# Check for any brand-specific references that shouldn't be here
grep -r "lillinello\|brand_name_placeholder" . --include="*.md" --include="*.yaml"
# Should return empty
```

## Step 7: Report findings

List all issues found in each category with file names and line numbers. Priority:
- 🔴 **Must Fix:** Missing required frontmatter, broken internal links, invalid YAML
- 🟡 **Should Fix:** Missing sections, incomplete cross-references
- 🟢 **Consider:** Style improvements, optional enhancements
