# External Dependency Registry Template

Use this in `project-control/REGISTRIES/EXTERNAL_DEPENDENCY_REGISTRY.md`.

| Dependency ID | Type | Name | Local Path / URL | Required For Stage | Status | Validation Method | Last Checked | Notes |
|---|---|---|---|---|---|---|---|---|
| EXT-001 | folder | project-control | ./project-control | all | required | path exists + required files |  |  |
| EXT-002 | repo | backend | ./backend | backend | conditional | git repo + pointer file |  |  |
| EXT-003 | figma | main design file |  | design | conditional | registered link + baseline packet |  |  |
