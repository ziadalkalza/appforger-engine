# Google Drive Docs Workflow

Google Drive can be used as an external docs storage provider.

In this version, Appforger provides documented workflow and import packet support, not a full Google Drive connector.

Recommended process:
1. Store the document in an approved Google Drive folder.
2. Create a document import packet.
3. Register the document in `DOCUMENT_LIBRARY_REGISTRY.md` with the Drive link.
4. Create or upload a Markdown summary/extraction if indexing is allowed.
5. Index the summary, not the original binary document, unless a future connector supports safe extraction.
