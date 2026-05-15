# Skill: Run Operational Audit

## Purpose
Audit the complete AppForge engine for structural and rule compatibility before a stable release or before using the engine on an important project.

## Inputs
- AppForge engine folder.
- Optional generated sample workspace.
- Audit scenario list.
- Audit mode: report-only, safe-fixes, or full-fix-review.

## Required context
- `validation/audits/operational-audit/`
- `validation/`
- `templates/engine/`
- `AGENTS.md`

## Steps
1. Confirm audit mode.
2. Validate engine structure.
3. Validate source-of-truth boundaries.
4. Validate workflow compatibility.
5. Validate draft/sandbox isolation.
6. Validate flexible workflow overrides.
7. Validate context backend safety.
8. Validate team mode compatibility.
9. Validate automation safety.
10. Validate release readiness workflow.
11. Run scenario checks.
12. Produce audit report and safe-fix plan.

## Rules
- Apply only safe fixes automatically.
- Ask the user before behavior-changing fixes.
- Do not activate automations, integrations, context backend, or team mode during audit.
