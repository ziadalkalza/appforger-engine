# Local JSONL Context Profile

Local JSONL is the default context backend mode. It requires no vector database and is useful for small projects, early setup, audits, and offline workflows.

It stores normalized context records as JSONL files under:

```text
project-control/context-backend/indexes/
```

Each record must include source metadata and a text body or summary.

This mode can support keyword/metadata retrieval and can later be migrated to Qdrant or Supabase pgvector.
