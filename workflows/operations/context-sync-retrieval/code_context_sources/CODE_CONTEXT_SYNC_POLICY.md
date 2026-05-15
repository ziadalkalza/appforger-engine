# Code Context Sync Policy

Code context sync updates derived maps, summaries, indexes, and staleness records. It must not silently modify source code.

## Sync modes

```yaml
sync_modes:
  manual:
    description: "User or approved agent explicitly runs a sync."

  local_git_hook:
    description: "Local hook marks context stale or regenerates changed-file summaries."

  remote_webhook:
    description: "Git provider webhook marks code context stale or triggers approved sync."

  ci_generated_context:
    description: "CI workflow publishes summary/map artifacts for AppForge to import."

  agent_after_approval:
    description: "Authorized tool refreshes context after approved task execution."
```

AppForge v1 may provide templates and validators. It must not pretend to have a live autonomous runner unless an external tool/model is actually executing the scripts.
