# Sensitive Document Policy

Sensitive documents are excluded from indexing and retrieval by default.

Sensitive examples:
- contracts
- legal/private client material
- credentials screenshots
- financial documents
- incident reports
- documents containing personal data

To index a sensitive document, the user must explicitly approve indexing scope and risk. Until AppForge has a stronger authenticated MCP/server layer, role-gated sensitive retrieval should not be assumed.
