# Document Indexing Policy

The context backend indexes document summaries/extractions, not original DOCX/PDF binaries by default.

Every indexable document must have:
- document ID
- source path or URL
- storage provider
- sensitivity classification
- lifecycle status
- indexing permission
- related entities
- summary/extraction path

Do not index sensitive documents unless explicitly approved.
