# Done Report Requirements

Each task that claims completion must produce a done report.

## Done Report Must Include

```yaml
task_id:
task_title:
status:
actor:
repo:
branch:
commit:
pr:
source_of_truth:
  design_baseline:
  api_baseline:
  feature_registry_entry:
changed_files:
checks_run:
  build:
  unit_tests:
  integration_tests:
  visual_qa:
  accessibility:
post_actions_completed:
missing_evidence:
warnings:
follow_up_tasks:
user_override:
final_approval:
```

## Location

Store done reports outside the engine in project-control:

```text
project-control/templates/packets/code-agent-packets/providers/codex/done/
```

If project-control is unavailable, store a temporary copy in:

```text
local-only/task-done-reports/
```

and import it into project-control later.
