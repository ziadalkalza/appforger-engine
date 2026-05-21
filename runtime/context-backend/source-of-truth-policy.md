# Source of Truth Policy

In v16, context backends never replace project-control.

Canonical hierarchy:

1. Approved project-control files in source-control app
2. Approved design baselines referenced by project-control
3. Approved code repos, commits, and PRs
4. SQL context backend records
5. Vector/RAG retrieved context
6. Draft/sandbox artifacts

RAG retrieval is evidence discovery, not truth.

## Retrieval Is Not Truth

RAG/vector retrieval is a candidate-finding layer. It must not replace canonical artifacts.

Canonical sources include:
- `project-control/` for state, registries, decisions, and baselines
- implementation repos for source code
- design baseline records for design truth
- `docs/` or external docs storage for source documents
- `design-assets/` for approved exported visual assets

If retrieval and canonical source disagree, Appforger must mark context as stale and create a reindex/update task before high-risk work continues.
