# Document Import Policy

Every imported document should use a document import packet.

The import packet records:
- source provider: local, GitHub, Google Drive, Supabase Storage, generic cloud, other
- destination: `docs/` path or external storage URL
- document classification
- sensitivity level
- whether summary/extraction is required
- whether indexing is allowed
- related epic/feature/story/screen/API/release/decision

Original imported files must not be overwritten. Companion summaries/extractions may be regenerated.
