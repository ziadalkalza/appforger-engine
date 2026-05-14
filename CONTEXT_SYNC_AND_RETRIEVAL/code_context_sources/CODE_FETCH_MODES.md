# Code Fetch Modes

Code may be available in different ways depending on project setup and user role.

```yaml
fetch_modes:
  local_checkout:
    description: "Repo exists locally or inside the workspace."
    supports_raw_file_access: true
    supports_write: true

  remote_git_readonly:
    description: "Repo is read remotely through GitHub/GitLab/Bitbucket API or read-only clone."
    supports_raw_file_access: true
    supports_write: false

  remote_git_write_branch:
    description: "Authorized user or agent may create a task branch and propose changes."
    supports_raw_file_access: true
    supports_write: true

  uploaded_snapshot:
    description: "User uploads a fixed repo snapshot."
    supports_raw_file_access: true
    supports_write: false

  ci_generated_context:
    description: "CI scans the private repo and publishes approved summaries/maps/index artifacts."
    supports_raw_file_access: false
    supports_write: false

  summary_only:
    description: "Only approved maps/summaries are available to the current role."
    supports_raw_file_access: false
    supports_write: false

  no_access:
    description: "The current role cannot fetch this source."
    supports_raw_file_access: false
    supports_write: false
```

CI-generated context is first-class in v1 because it supports private or non-local repositories without exposing raw code to every user or tool.
