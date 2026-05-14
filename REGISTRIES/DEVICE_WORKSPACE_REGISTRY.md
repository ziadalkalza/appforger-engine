# Device Workspace Registry

Track which local/remote workspaces are used by different devices or roles.

## Entry template

```yaml
workspace_id: DEVICE-WORKSPACE-001
owner_or_role:
device_name:
workspace_type: frontend | backend | designer | qa | operator | mixed
project_control_access: local_clone | remote_github | not_available
repos_available:
  backend: local_clone | remote_github | artifact_packet | not_available
  ios: local_clone | remote_github | artifact_packet | not_available
  android: local_clone | remote_github | artifact_packet | not_available
  web: local_clone | remote_github | artifact_packet | not_available
last_validated_at:
notes:
```
