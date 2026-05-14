# Start Draft Experiment

## Purpose

Create and register a safe draft or sandbox experiment before modifying real project artifacts.

## Required context

- `AGENTS.md`
- `DRAFT_AND_SANDBOX_MODE/README.md`
- `project-control/REGISTRIES/DRAFT_REGISTRY.md` when available
- relevant epic/feature/story if known

## Rules

- Do not modify approved baselines directly.
- Do not write draft artifacts into `appforge-engine/`.
- Keep raw draft files in `local-only/` or a clearly marked draft branch.
- Update draft registries when the user wants the draft tracked.
- Ask before promotion.

## Steps

1. Clarify purpose and linked story/feature if known.
2. Choose local-only, sandbox, Figma draft, or draft branch.
3. Create draft metadata.
4. Identify expiry review date.
5. State what will not be touched.

## Output

Draft record and workspace location.
