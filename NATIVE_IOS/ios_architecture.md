# iOS Architecture

## Default

Use feature-based MVVM for most apps.

For complex apps, use Clean Architecture with:

```text
Feature/
  Views/
  ViewModels/
  Models/
  Services/
  Repositories/
```

## Rules

- Views should stay presentational.
- ViewModels own UI state.
- Services/repositories own network/data access.
- API models map to domain/UI models where needed.
- Keep preview/mock data separate from production services.

## Unsupported architecture

TCA or other patterns require engine upgrade unless explicitly added.
