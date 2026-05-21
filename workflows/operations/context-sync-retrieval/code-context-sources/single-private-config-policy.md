# Single Private Configuration File Policy

Appforger must provide a single user-facing private configuration file for local secrets, repo access references, runtime environment variables, CI/CD secret names, hosting environment references, and code source access settings.

The default file is:

```text
local-only/.env.local
```

Users should not be required to manually spread sensitive variables across multiple Appforger files.

Appforger may derive safe metadata, registries, `.env.example` files, local `.env.local` files, and access reports from this private file.

The private file must be gitignored, excluded from context indexing, excluded from docs, excluded from execution packets, and excluded from reports.

Project-control may store only generated metadata and references, not actual secret values.

If the project needs real secret values in CI/CD or hosting, Appforger should generate setup instructions or secret-name manifests, not store those values itself.

## Derivation model

```text
local-only/.env.local
  -> project-control/access_and_secrets/*.yaml      # metadata only
  -> project-control/code_sources/*.yaml            # metadata only
  -> backend/.env.example / web/.env.example        # placeholders only
  -> backend/.env.local / web/.env.local            # generated locally only, gitignored
```
