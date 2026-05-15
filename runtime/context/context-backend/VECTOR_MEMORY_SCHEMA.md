# Vector Memory Schema

Each vector point/chunk must include metadata:

```yaml
project_id:
artifact_id:
artifact_type:
source_path:
source_commit:
approval_status:
baseline_version:
is_current:
last_updated:
indexed_at:
chunk_id:
summary:
```

Never store secrets or environment values in vector payloads.
