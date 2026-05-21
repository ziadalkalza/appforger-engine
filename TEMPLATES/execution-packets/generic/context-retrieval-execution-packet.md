# Context Retrieval Execution Packet

Use for project-control, Qdrant, Supabase, or other context retrieval providers.

Retrieved context must include source metadata and must point back to canonical sources.

## Code context packet requirements

When a packet uses Code Context Sources, it must include source ids, access level used, freshness, and restrictions.

Exact files/commits/snapshots are required for implementation packets and source-review packets. Normal user-facing answers may use retrieved context without showing source metadata unless asked.

If required access is missing, set packet status to `blocked` and identify the responsible role or access request.
