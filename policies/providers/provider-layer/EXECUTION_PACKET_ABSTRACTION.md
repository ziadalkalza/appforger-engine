# Execution Packet Abstraction

A packet is a structured handoff bundle for a provider/tool.

Generic packet fields:

- packet_id
- task_goal
- target_provider_type
- required_capabilities
- source_of_truth
- context_to_load
- allowed_actions
- forbidden_actions
- target_repo_or_tool
- expected_outputs
- tests_or_checks
- done_report_requirements
- post-actions
- risk_level
- approval_requirements

Provider-specific packets adapt this generic format to Codex, Claude Code, Figma, image generation, local code agents, or other tools.
