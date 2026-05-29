# Future Feature Backlog

Tracks proposed Appforger engine features that are not yet implemented or approved for active workflow use.

Project/product backlog items belong in external `project-control/registries/product-backlog-registry.md`. This file is for global engine evolution.

| ID | Feature | Status | Priority | Scope | Notes |
|---|---|---|---|---|---|
| FFB-001 | Project-level and global-level logic separation | proposed | TBD | engine architecture | Add first-class handling for logic that can exist at both project level and global level. For example, templates may be project-specific or global/reusable, and the user should decide whether an artifact stays project-local, is promoted globally, or remains outside the engine. This should apply beyond templates wherever Appforger has reusable logic versus project-specific decisions. |
