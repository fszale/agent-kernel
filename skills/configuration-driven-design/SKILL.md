---
name: configuration-driven-design
description: Design systems where behavior is controlled by external configuration files rather than hardcoded logic. Enables non-engineers to manage business rules, enables CI/CD of configuration, and reduces deployment risk.
when-to-use: Use when designing any system with configurable business rules, thresholds, or behavior. Use when business analysts or product owners need to control system behavior without engineering involvement.
principles: [Configuration-Driven Design, DevOps First, Systems Over Goals]
---

# Configuration-Driven Design Skill

## Purpose

Design systems where configuration is a first-class citizen — externalized, versioned, validated, and deployable independently of code.

## Agent Instructions

You are a software architect applying configuration-driven design principles.

### Core Principle

Separate what the system does (code) from how it behaves (configuration). Configuration includes:
- Business rules and thresholds
- Feature flags and switches
- Routing and workflow logic
- Environment-specific settings

### Step 1: Identify Configuration Candidates

Scan the system for values and behaviors that will change over time:
- Numeric thresholds (limits, targets, rates)
- Business rules (if X then Y)
- Routing logic (which handler for which case)
- Feature availability (who sees what)
- Environment settings (URLs, credentials, timeouts)

Each of these should be configuration, not code.

### Step 2: Design the Configuration Schema

For each configuration domain:
1. Define the schema (YAML or JSON) with types and validation rules
2. Document every field: what it controls, valid range, default value
3. Add comments explaining business context
4. Define which changes require system restart vs. hot-reload

Example structure:
```yaml
# Descriptive comment explaining this config block
feature_name:
  enabled: true               # boolean: toggle this feature
  threshold: 0.75             # float: 0.0–1.0, triggers decision logic
  max_items_per_day: 20       # int: rate limit
```

### Step 3: Externalize the Rules Engine

For complex conditional logic:
- Use a rules engine (or rules-as-data pattern) instead of if/else trees
- Rules defined in config/YAML → evaluated by a generic engine
- Non-engineers can add/modify/remove rules without code changes
- All rules are auditable and versioned in source control

### Step 4: CI/CD the Configuration

Treat configuration as a deployable artifact:
1. Store configuration in source control (not databases or wikis)
2. Add schema validation to CI pipeline (fail fast on invalid config)
3. Test configuration changes in staging before production
4. Enable rollback of configuration independently of code

### Step 5: Access Control and Audit

Define who can change what:
- Which config sections can non-engineers edit?
- Which require engineering review?
- How are config changes logged?
- Is there a review/approval gate for high-risk config changes?

## Output Format

Configuration design document:
1. Configuration inventory (all identified config candidates)
2. Schema design (with YAML/JSON examples)
3. Rules engine design (if applicable)
4. CI/CD integration plan
5. Access control matrix
6. Migration plan (moving hardcoded values to config)
