# Code Context Sources

Code Context Sources extends the existing context sync and retrieval layer so Appforger can understand backend, frontend, mobile, iOS, and Android code without confusing derived context with source of truth.

This feature is used when a project has existing code, imported code, remote repositories, uploaded snapshots, or CI-generated code maps.

## Core model

```text
actual repo/folder/snapshot  -> canonical code truth when canonical: true
code source registry         -> where the code truth lives and who can access it
context index                -> derived summaries, maps, metadata, embeddings
execution packet             -> task-scoped, role-aware context for an acting model/human
```

The context backend may store summaries, maps, source metadata, embeddings, and retrieval logs. It must not be treated as the canonical code source.

## Required first-time bootstrap

When onboarding marks a project as ongoing or imports existing code, Appforger must run an initial code context bootstrap before code-aware implementation. Bootstrap creates the first repo summaries, source maps, access records, freshness state, and index records.

Planning can continue while bootstrap is incomplete, but implementation, refactoring, release, migrations, auth/security changes, CI/CD edits, and API contract changes require fresh context or inspection of actual code.

## Single private configuration file

Users should not manually spread sensitive values across many files. Appforger provides one local private file:

```text
local-only/.env.local
```

The user fills that file once. Appforger derives safe metadata, repo access registries, code-source records, `.env.example` files, and local `.env.local` files from it when allowed.

The private file must be gitignored, not indexed, not copied into project-control, not included in execution packets, and not reported with secret values.
