# Code Indexing Policy

By default, Appforger indexes code summaries and code maps, not raw source code.

```yaml
summary_indexing: true
raw_code_indexing: false
```

Raw code indexing requires explicit approval and must be labeled high-risk.

## Default generated artifacts

Backend code sources should generate:

- repo summary
- architecture map
- API route map
- auth/security map
- database model map
- migration map
- integration map
- dependency map
- risky files list

Frontend/mobile code sources should generate:

- repo summary
- route/screen map
- component map
- state-management map
- API-client map
- theme/design-system map
- navigation-flow map
- dependency map
- risky files list

## Exclusions

Always exclude secrets, generated files, build artifacts, vendored packages, and binary caches unless an explicit policy says otherwise.

Recommended exclusions:

```yaml
exclude:
  - ".env"
  - ".env.*"
  - "node_modules/"
  - "venv/"
  - ".venv/"
  - "dist/"
  - "build/"
  - "__pycache__/"
  - "*.pem"
  - "*.key"
  - "secrets.*"
```
