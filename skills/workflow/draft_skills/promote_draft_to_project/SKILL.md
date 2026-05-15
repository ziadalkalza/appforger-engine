# Promote Draft to Project

## Purpose

Convert approved draft output into a real project artifact without bypassing AppForge gates.

## Required context

- `AGENTS.md`
- `workflows/operations/draft-sandbox/README.md`
- `project-control/registries/DRAFT_REGISTRY.md` when available
- relevant epic/feature/story if known

## Rules

- Do not modify approved baselines directly.
- Do not write draft artifacts into `appforge-engine/`.
- Keep raw draft files in `local-only/` or a clearly marked draft branch.
- Update draft registries when the user wants the draft tracked.
- Ask before promotion.

## Steps

1. Confirm user approval.
2. Determine promotion target.
3. Run artifact-specific checks.
4. Update affected registries.
5. Create candidate baseline or execution packet if needed.

## Output

Promotion record and updated project-control files.
