# Context Keeping Rules

## Goal

Keep ChatGPT, Codex, Figma, GitHub, and external tools aligned.

## Source-of-truth hierarchy

### Product truth

- `PRODUCT_OVERVIEW.md`
- `FEATURE_REGISTRY.md`
- `DECISION_LOG.md`

### Visual truth

Before Figma approval:

1. User-provided design references.
2. Project-specific design rules.
3. Global Appforger design system.
4. Platform defaults.

After Figma approval:

- Approved Figma baseline becomes the current visual source of truth.
- It can be superseded by a newer approved baseline.

### Backend truth

- `API_REGISTRY.md`
- `DATA_MODEL_REGISTRY.md`
- Backend repo code.
- Migration files.
- Environment registry.

### Implementation truth

- GitHub repos.
- PRs/branches.
- Test results.
- Change request registry.

## Baselines

Use version labels:

- `DESIGN_BASELINE_V1`
- `API_CONTRACT_V1`
- `BACKEND_SCHEMA_V1`
- `IOS_IMPLEMENTATION_V1`
- `ANDROID_IMPLEMENTATION_V1`

## Handoff rule

Every external handoff must record:

- Source artifact.
- Destination tool.
- Inputs.
- Outputs.
- Review state.
- Next consumer.
