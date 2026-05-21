# Project Docs and Context Example

Example workspace structure:

```text
my-app-workspace/
  project-control/
    REGISTRIES/DOCUMENT_LIBRARY_REGISTRY.md
    context-backend/indexes/context.jsonl
    context-backend/retrieval-packs/TASK-WEB-LOGIN-001.context.md
  docs/
    imports/client-brief.pdf
    summaries/client-brief.summary.md
  web/
  backend/
```

A document import packet registers `client-brief.pdf`, creates `client-brief.summary.md`, and allows the context backend to index the summary.

A retrieval pack for a login task may include:
- project-control user story
- API baseline
- docs/summaries/client-brief.summary.md
- latest QA report summary

Every retrieved item must include source path and current/superseded status.
