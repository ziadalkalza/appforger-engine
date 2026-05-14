# Validate Team Operations Backend

## Purpose
Validate configuration, schema, source-of-truth rules, and secret/document boundaries.

## Rules
- Do not store full docs, full meeting notes, source code, or secret values in the operations backend.
- project-control remains canonical.
- Write-back to project-control must happen through sync packets or PRs.
- Record warnings, conflicts, and audit events.
