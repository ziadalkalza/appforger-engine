# Qdrant Stale Context Policy

If retrieved payload metadata disagrees with project-control, mark the index as stale.

When stale:

- Do not use retrieved result as final authority.
- Reindex affected files.
- Record stale context event in CONTEXT_SYNC_REGISTRY.
