# Code Access Policy

AppForge uses a simple role model with configurable read depth.

## Default roles

```yaml
default_code_ownership:
  backend:
    writable_by: [backend_developer, admin]
  web:
    writable_by: [frontend_mobile_developer, admin]
  mobile:
    writable_by: [frontend_mobile_developer, admin]
  ios:
    writable_by: [frontend_mobile_developer, admin]
  android:
    writable_by: [frontend_mobile_developer, admin]
  ci_cd:
    writable_by: [admin]
  secrets_metadata:
    writable_by: [admin]
```

Frontend and mobile are treated as the same default role: `frontend_mobile_developer`.

## Access levels

```yaml
access_levels:
  no_access:
    can_read: false
    can_write: false

  read_only:
    can_read: true
    can_write: false
    allowed_views:
      - metadata_only
      - summaries_only
      - maps_only
      - raw_files_if_allowed

  write:
    can_read: true
    can_write: true
    write_scope:
      - owned_code_area
      - approved_task_branch
      - approved_files

  admin:
    can_read: true
    can_write: true
    can_configure_sources: true
    can_manage_access_policy: true
    can_approve_raw_code_indexing: true
```

## Read-only is not always raw-code access

Read-only means the user or agent cannot modify the repo. It does not automatically mean raw source files are visible.

A read-only role may receive only:

- metadata
- summaries
- maps
- task-scoped raw files
- full raw files, only if allowed

## Blocked access behavior

If a task needs raw code or write access and the current role does not have it, AppForge must generate an access request or blocked execution packet. It must not guess from incomplete context.
