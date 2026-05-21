# Project Docs Library Policy

`docs/` is the shared document area for a project. It may be local, a GitHub repo, Google Drive, Supabase Storage, or another approved cloud storage provider.

Do not store full documents inside `project-control/`.

`project-control/REGISTRIES/DOCUMENT_LIBRARY_REGISTRY.md` tracks:
- document ID
- title
- type
- storage provider
- path or URL
- lifecycle status
- sensitivity
- indexing permission
- related Appforger entities
- summary/extraction path if available

Canonical documents remain in `docs/` or external storage. Registries make them discoverable and auditable.
