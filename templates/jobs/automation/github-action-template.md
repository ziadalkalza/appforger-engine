# GitHub Action Template

Active workflow files are generated into `.github/workflows/` only when enabled.

```yaml
name: Appforger Job
on:
  workflow_dispatch:
  pull_request:
    paths:
      - 'project-control/**'
jobs:
  appforge-job:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Appforger validation
        run: python appforger-engine/validation/validate_automation_layer.py
```
