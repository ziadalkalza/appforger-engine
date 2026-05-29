# Access and Secrets Metadata

This folder contains safe metadata derived from the single private local config file. It must not contain actual secret values.

User-filled sensitive values belong in:

```text
local-only/.env.local
```

or in approved external stores such as GitHub Actions Secrets, hosting env vars, OS keychains, Git credential managers, or cloud secret managers.
