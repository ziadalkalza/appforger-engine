# Mobile Example

Example structure for a native mobile app:

```text
fitness-app-workspace/
  appforger-engine/
  project-control/
  backend/
  ios/
  android/
  design-assets/
  exports/
  local-only/
```

Example epic: Account onboarding
Example story: As a new user, I want to create an account, so that I can save my progress.

## Provider-routing example inside this mobile flow

Task: implement the approved login screen.

Required capabilities:

- repo_inspection
- code_editing
- test_execution
- visual QA evidence

Recommended provider type: `code_agent`.

Compatible providers can include Codex, Claude Code, or an approved local code agent, depending on project setup. ChatGPT/Claude chat may create the execution packet or review the result, but code produced directly in chat remains draft-only until applied and tested by a code agent.

Packet path example:

```text
project-control/templates/packets/code-agent-packets/providers/codex/TASK-IOS-LOGIN-001.md
```

The packet should now be understood as a provider-specific adaptation of a generic `CODE_AGENT_EXECUTION_PACKET`.

