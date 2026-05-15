# Review Draft Experiment

## Purpose

Evaluate whether a draft should be promoted, revised, archived, or discarded.

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

1. Inspect draft outputs and evidence.
2. Classify artifact type.
3. Compare against current project baselines.
4. List risks and missing checks.
5. Recommend promote/revise/archive/discard.

## Output

Draft review report.
