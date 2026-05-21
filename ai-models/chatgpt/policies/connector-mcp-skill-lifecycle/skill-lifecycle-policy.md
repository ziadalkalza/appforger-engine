# Skill Lifecycle Policy

Appforger skill files define repeatable behavior. They do not guarantee the active Codex session has loaded or invoked them.

## Required tracking

For each skill, track:

```yaml
skill_name: ""
path: ""
status: generated | installed | validated | active | deprecated
intended_tasks: []
required_context_files: []
validation_method: "manual invocation or Codex session confirmation"
last_validated: ""
```

## Activation rule

Before relying on a skill, the task packet should explicitly reference the skill path and require Codex/ChatGPT to read it.
