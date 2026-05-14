# Script Extension Policy

Context scripts are expected to evolve as project needs grow.

Future scripts may add:
- document normalization
- provider-specific extraction
- Qdrant batch upsert
- Supabase pgvector indexing
- Tree-sitter code summary generation
- incremental reindexing
- stale context diffing

Any new script must follow:
- no secret indexing
- source metadata required
- sensitive docs excluded by default
- retrieval logs required
- project-control remains canonical
