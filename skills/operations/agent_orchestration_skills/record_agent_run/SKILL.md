# Record Agent Run

Use this skill for AppForge sub-agent orchestration.

Required inputs:
- related feature/story/task
- current workflow variant
- provider/brand-family preference if relevant
- target repo/stage
- dependencies and baselines
- risk level

Rules:
- Use `policies/operations/parallel-agent-work/`.
- Do not dispatch parallel work without a parallel work plan.
- Do not allow baseline approval by an agent unless explicitly authorized.
- Record audit output in the relevant project-control registry.
- In team mode, project-control changes must use PR-based workflow.
