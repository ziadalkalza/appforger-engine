# Permission and Scope Policy

Use least privilege for all external tools.

For each connector/MCP, record:

```yaml
capability: ""
requested_scopes: []
why_needed: ""
read_access_required: true
write_access_required: false
production_access_required: false
owner_approval_required: true
```

If write access is not required, do not request it. If production access is not required, use sandbox/staging/test mode.
