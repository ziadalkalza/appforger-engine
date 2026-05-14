# Android Architecture

## Default

Use feature-based MVVM for most apps.

For complex apps, use Clean Architecture with:

```text
feature/
  ui/
  viewmodel/
  domain/
  data/
```

## Rules

- Composables stay mostly presentational.
- ViewModels own UI state.
- Repositories own data access.
- Use coroutines/Flow where useful.
- Keep preview/mock data separate.

## Unsupported architecture

MVI or other patterns require engine upgrade unless explicitly added.
