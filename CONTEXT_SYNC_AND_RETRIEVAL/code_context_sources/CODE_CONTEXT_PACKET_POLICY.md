# Code Context Packet Policy

Execution packets that use code context must state what code access was used.

Example:

```yaml
execution_packet_context:
  task: "Connect frontend login form to backend auth endpoint"
  code_sources:
    - source_id: frontend-main
      access_used: task_scoped_raw_files
      files:
        - web/src/pages/LoginPage.tsx
        - web/src/api/authClient.ts
    - source_id: backend-main
      access_used: api_map_only
      files_exposed: false
      context:
        - project-control/code_sources/backend-main/api-route-map.md
  restrictions:
    - "Do not modify backend code."
    - "Do not invent backend endpoints."
```

If required access is missing, the packet status must be `blocked` and must include the needed access or responsible role.
