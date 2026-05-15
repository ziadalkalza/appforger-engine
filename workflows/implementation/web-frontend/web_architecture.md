# Web Architecture

A web app must declare one architecture mode:

- `spa_separate_backend`
- `nextjs_fullstack`
- `public_marketing_site`
- `admin_dashboard`
- `shared_backend_web_mobile`

## Standard folders for web repos

```text
web/
  src/
    app/ or pages/
    components/
    features/
    lib/
    services/
    styles/
    tokens/
    tests/
```

The exact structure depends on the selected stack, but feature ownership, API clients, token mapping, and test location must be clear.
