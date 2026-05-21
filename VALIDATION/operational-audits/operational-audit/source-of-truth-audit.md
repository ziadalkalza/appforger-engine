# Source of Truth Audit

Checks that Appforger consistently distinguishes truth, retrieval, mirrors, drafts, and implementation.

## Canonical model

- `project-control/` is the canonical app memory for decisions, registries, baselines, packets, evidence, approvals, and stage status.
- Figma or another approved visual source is the visual design source only after it becomes an approved visual baseline.
- Code repos are the implementation source of truth for live backend/frontend code.
- RAG/Qdrant/context backend is retrieval/indexing support and must point back to canonical sources.
- Trello/task apps are mirrors or task-board interfaces unless explicitly upgraded later.
- Drafts/sandboxes are not truth until promoted and approved.

## Required wording

Use “approved visual baseline” instead of “Figma required.”

Use “backend required unless an approved no-backend/backendless workflow is selected” instead of “backend always required.”

Use “context backend retrieves/indexes and cites canonical sources” instead of “RAG is project truth.”

## Code Context Sources audit checks

Audit must confirm:

- code sources marked `canonical: true` point to an actual repo, branch/commit, folder, or snapshot;
- context backend records are derived and not canonical;
- ongoing projects have an initial code context bootstrap status;
- stale/partial code context blocks implementation/refactor/release/high-risk work;
- private config files and secret values are not stored in project-control, docs, context indexes, reports, or execution packets;
- repo credentials are represented as metadata references only.
