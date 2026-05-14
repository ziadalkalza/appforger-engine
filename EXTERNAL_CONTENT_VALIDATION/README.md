# External Content Validation

This folder contains rules and scripts that verify the folders and external project artifacts AppForge depends on actually exist.

AppForge should never assume external project-control or code repos are present. It must validate them.

Primary scripts:

```text
validate_external_workspace.py
bootstrap_project_control.py
```

Use this layer before starting a stage, before sending Codex to a repo, and before approving external artifacts.


## Remote context validation

Use `validate_remote_context.py` when frontend/backend/design/QA work may happen on different devices or when a required repo is not local.

Example:

```bash
python EXTERNAL_CONTENT_VALIDATION/validate_remote_context.py --workspace ./my-app-workspace --require ios,backend
```

If a required repo is not local, the task packet must specify an approved remote access mode or artifact packet before work continues.
