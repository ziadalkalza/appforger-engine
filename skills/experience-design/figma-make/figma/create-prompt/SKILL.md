# Create Figma Prompt

    ## Purpose
    Prepare high-context prompts for Figma/Figma Make so design/prototype work stays aligned with Appforger.

    ## When to use
    Use this skill only when the current Appforger stage requires this exact workflow. Do not use this skill as a shortcut around approval gates.

    ## Inputs
    - Product brief
- UX flows
- Visual direction
- Asset list
- Platform targets

    ## Outputs
    - Figma Make prompt
- Figma design instructions
- Prototype requirements
- Animation instructions

    ## Required context files
    - `integrations/design/figma-make/templates/prompts/master-prompt.md`
- `ai-models/chatgpt/docs/handoffs/chatgpt-to-figma.md`
- `workflows/experience-design/design-workflow/figma-workflow.md`

    ## Rules
    - Read `APPFORGER_PROJECT_STATUS.md`, `DECISION_LOG.md`, `PENDING_QUESTIONS.md`, and all relevant registries before acting.
    - If required information is missing, write it to `PENDING_QUESTIONS.md` or make an explicit assumption in `ASSUMPTION_LOG.md`.
    - Do not invent unsupported stacks, connectors, platforms, or architectures. Use `ENGINE_UPGRADE_PROTOCOL.md` first.
    - Update all affected registries after producing outputs.
    - Prefer small, reviewable changes over large unreviewable rewrites.
    - If a reusable pattern emerges, add it to `registries/project-control/pending-templates.md`.

    ## Steps

      1. Summarize product and UX context.
      2. Specify screen list and interactions.
      3. Specify design tokens and style constraints.
      4. Specify prototype and animation expectations.
      5. Specify what Figma should output back to Appforger.
      6. Update handoff file.


    ## Approval gates
    Figma output must be reviewed before design baseline approval.

    ## Failure handling
    - If the task cannot be completed, document the blocker, affected files, and next safe action in `APPFORGER_PROJECT_STATUS.md` and `PENDING_QUESTIONS.md`.

    ## Handoffs
    - Update the relevant provider/app handoff file when this skill produces an artifact another agent will consume.
