# Context Backend Health Checks

Health checks should verify:
- backend mode is configured
- local JSONL index exists if enabled
- selected context storage app connection works if enabled
- collection/table exists
- last sync time is known
- stale context is detected
- forbidden files were excluded
- sensitive docs are excluded unless approved
- retrieval returns source metadata
- freshness validation passes for high-risk tasks
