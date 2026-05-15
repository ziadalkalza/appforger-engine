# Code Context Source Policy

Registered backend, frontend, mobile, iOS, and Android code sources may be local, remote, snapshot-based, CI-generated, or summary-only.

A code source becomes canonical only when marked `canonical: true`.

Canonical code truth remains the actual repo, branch, commit, folder, or approved snapshot. Context summaries, maps, embeddings, indexes, and retrieval records are derived context, not canonical code truth.

Users responsible for their own code area may write when authorized. Other roles are read-only by default. Admins may configure sources, access, indexing, and sync policies.

Read-only access may expose raw files, maps, summaries, or metadata depending on project policy.

Raw code indexing, repo write access, production branch changes, auth/security code, payment code, migrations, secrets, API contract changes, CI/CD edits, and role/access policy changes are high-risk and require explicit approval.

If code context is stale, planning may continue, but implementation, refactoring, release work, migrations, auth/security changes, CI/CD edits, and API contract changes require fresh code context or inspection of actual source files.

If a user or agent lacks required access, AppForge must generate a blocked execution packet or access request instead of guessing.
