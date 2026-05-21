# Team Operations State Sync Policy

Write-back to project-control must happen through a controlled sync packet or PR. Direct silent writes are forbidden.

Supported sync directions:
- project-control → operations backend: sync approved state into queryable tables.
- operations backend → project-control: generate sync packet/PR for review.

Every sync must record source paths, timestamps, affected records, warnings, and conflict status.
