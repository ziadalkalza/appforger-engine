# Task Completion Registry Template

Store task completion records in project-control, not inside the reusable engine.

Recommended location:

```text
project-control/REGISTRIES/TASK_COMPLETION_REGISTRY.md
```

## Entry Template

```yaml
task_id:
title:
owner:
status:
completion_type: checkpoint | completion | manual_override | reopened
repo:
branch:
commit:
pr:
source_of_truth:
completion_evidence:
  expected_output_exists:
  tests_recorded:
  visual_qa_recorded:
  registries_updated:
  done_report:
missing_evidence:
warnings:
follow_up_tasks:
approval:
updated_at:
```
