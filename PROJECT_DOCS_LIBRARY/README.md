# Project Docs Library

The Project Docs Library is a global workspace folder/repo named `docs/`. It stores shared project documents outside `project-control/`.

`project-control/` remains the canonical registry and decision/state layer. It stores document metadata and links only. It must not store full DOCX/PDF files or long-form document bodies.

## Default workspace

```text
my-app-workspace/
  appforge-engine/
  project-control/
  docs/
  design-assets/
  backend/
  ios/
  android/
  web/
  exports/
  local-only/
```

## Rule

Documents live in `docs/` or an approved external docs storage provider. AppForge indexes summaries/extractions and always points retrieval results back to original sources.
