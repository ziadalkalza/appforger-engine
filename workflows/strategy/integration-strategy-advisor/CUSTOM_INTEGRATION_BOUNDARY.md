# Custom Integration Boundary

Custom API/Python integrations are allowed only after the Integration Strategy Advisor has checked for official connectors, trusted MCPs/plugins, and existing AppForger built-in integrations.

Custom code requires approval when:

- a safe official connector exists but the user still wants custom code;
- write actions are involved;
- sensitive data may be indexed;
- raw code or private documents may be fetched;
- paid cloud resources may be used;
- the integration uses broad credentials or privileged scopes.

Custom code must be placed under `project-control/integrations/<integration-id>/` or the correct source-specific folder, not randomly in the workspace root.
