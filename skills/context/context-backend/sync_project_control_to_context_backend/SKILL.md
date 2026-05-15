# Skill: Sync Project-Control to Context Backend

## Purpose
Run a controlled sync after project-control changes.

## Steps
1. Detect changed canonical files.
2. Reindex changed files.
3. Mark superseded chunks stale or non-current.
4. Write sync log.
5. Update registries.
6. Warn if sync fails and fall back to file mode.
