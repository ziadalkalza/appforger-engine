# Source-of-Truth Audit Report — v20

## Result

Passed with warnings.

## Confirmed model

- `project-control/` remains canonical project memory.
- Code repos remain implementation truth.
- Approved visual baseline is required for production UI implementation, but it does not have to come from Figma.
- Context backend/RAG is retrieval/indexing support, not canonical truth.
- Trello is a task-board mirror/interface by default.
- Draft/sandbox artifacts are not truth until promoted.

## Safe fixes applied

- v1.0 audit docs define the updated source-of-truth language.

## Warnings

Future audits should continue scanning older wording for hardcoded Figma/backend assumptions when new files are added.
