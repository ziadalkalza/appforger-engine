# Qdrant Context Profile

Qdrant is used as Appforger's semantic memory layer. It indexes summaries and approved project artifacts so Appforger can retrieve relevant context quickly.

One Qdrant collection per project is the v16 default.

## Stronger Profile Rules

Qdrant is an optional vector backend. It should index normalized context records with source metadata. One collection per project is recommended. Qdrant retrieves candidate context; docs/repos remain canonical.
