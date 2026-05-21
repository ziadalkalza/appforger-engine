# Appforger Workspace Pointer

This file identifies how this local device connects to Appforger project-control and implementation repos.

## Workspace

```yaml
workspace_name:
device_owner:
role: frontend | backend | designer | qa | operator | mixed
created_at:
```

## Appforger engine

```yaml
engine_local_path: ../appforger-engine
engine_remote_url:
engine_version:
```

## Project control

```yaml
project_control_local_path: ../project-control
project_control_remote_url:
last_pulled_commit:
```

## Implementation repos

```yaml
repos:
  backend:
    local_path: ../backend
    remote_url:
    access_mode: local_clone | remote_github | artifact_packet | not_available
  ios:
    local_path: ../ios
    remote_url:
    access_mode:
  android:
    local_path: ../android
    remote_url:
    access_mode:
  web:
    local_path: ../web
    remote_url:
    access_mode:
```

## Notes

Do not store secrets in this file.
