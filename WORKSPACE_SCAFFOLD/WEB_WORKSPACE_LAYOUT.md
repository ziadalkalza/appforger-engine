# Web Workspace Layout

For web projects, use one of these layouts.

## Web-only or web + external backend

```text
my-webapp-workspace/
  appforge/
  web/
  design-assets/
  exports/
  local-only/
```

## Web + separate backend

```text
my-webapp-workspace/
  appforge/
  web/
  backend/
  design-assets/
  exports/
  local-only/
```

## Shared product with mobile + web

```text
my-product-workspace/
  appforge/
  web/
  backend/
  ios/
  android/
  design-assets/
  exports/
  local-only/
```

Production web code belongs in `web/` or `web-app/`, not inside `appforge/`.
