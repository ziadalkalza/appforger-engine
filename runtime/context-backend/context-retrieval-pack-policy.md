# Context Retrieval Pack Policy

A retrieval pack is a structured context bundle created for a task, role, agent, or review.

Examples:
- frontend_context_pack
- backend_context_pack
- qa_context_pack
- release_context_pack
- agent_execution_context_pack

Retrieval packs may be generated manually, as draft packs after major state changes, or by an enabled automation/job runner. They remain draft until attached to a task or approved for use.

Every pack must include source references and indicate whether any context is stale, draft, superseded, sensitive, or unapproved.
