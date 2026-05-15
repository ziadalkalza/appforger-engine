# Secret Access Policy

Never store secret values in AppForge Markdown. Store only metadata, required locations, owners, and status.

## Single private config file

Users should fill sensitive/access/runtime variables in one local private file:

```text
local-only/.env.local
```

AppForge may derive safe metadata and templates from this file, but project-control must store only references and metadata. The private file must be gitignored, excluded from indexing, excluded from reports, and excluded from execution packets.
