# Run Context Health Check

Purpose: Validate context backend health, freshness, source metadata, and forbidden indexing rules.

Rules:
- project-control remains canonical.
- Retrieved context must include source references.
- Stale context blocks high-risk completion.
- Raw code indexing requires explicit approval.
