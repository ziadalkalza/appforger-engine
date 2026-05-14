# Setup Team Operations Backend

## Purpose
Set up the optional Team Operations Backend profile and config without storing documents or secrets.

## Rules
- Do not store full docs, full meeting notes, source code, or secret values in the operations backend.
- project-control remains canonical.
- Write-back to project-control must happen through sync packets or PRs.
- Record warnings, conflicts, and audit events.
