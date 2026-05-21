# Runtime Context

Context runtime guidance is split by scope:

- `context-backend/` contains generic context backend policy and architecture.
- `apps/` contains context backend profiles for specific storage apps.

---

<!-- merged from runtime/context-backend/README.md during structure cleanup -->

# Context Backend

The context backend is optional. It helps Appforger retrieve, search, and validate project memory for larger apps.

Default mode remains file/source-control app/project-control only.

When enabled, context backend data is derived from approved project-control files, approved baselines, reports, and summaries. It is not canonical truth in v16.

## Stronger Context Backend Update

The default context mode is a local JSONL index. vector database, SQL vector storage, and generic vector DB profiles are optional upgrades.

The context backend retrieves and indexes context. It is not the canonical source of truth. All retrieved items must point back to project-control, docs, design tool, source-control repos, design-assets, or other approved sources.

## Code context source support

The context backend may index derived code summaries, maps, and metadata from registered Code Context Sources. It must not treat retrieved code context as canonical truth.

Raw source code indexing remains disabled by default and requires explicit approval. CI-generated code summaries/maps are a first-class option for private or non-local repositories.
