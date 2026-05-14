# Create MCP Action Plan Skill

Use this skill when the model needs an AppForger command but the MCP must not execute it.

Steps:

1. Identify the workflow.
2. Use MCP resources/prompts to find the matching AppForger command.
3. Classify risk.
4. Return:
   - command
   - run location
   - expected outputs
   - required approvals
   - files likely affected
5. Never represent a high-risk command as safe to run automatically.
