# Design System Conflict Resolution

Use this when AppForge, a project design system, an imported design system, the selected design tool, and platform defaults disagree.

## Default priority before design-tool approval

```text
1. User-provided direct instruction for this project
2. Project-specific design system
3. Approved imported design system
4. AppForge global design system
5. Platform defaults
```

## Default priority after design-tool approval

```text
1. Accessibility, security, privacy, performance, and platform constraints
2. Latest approved design baseline
3. Project-specific design system
4. Approved imported design system
5. AppForge global design system
6. Platform defaults
```

## Conflict record template

```text
Conflict ID:
Date:
Affected screen/component:
Rule A:
Rule B:
Impact:
Decision:
Decision owner:
Follow-up required:
```

## Rules

- The approved design tool baseline can override visual rules only after approval.
- Imported systems cannot bypass AppForge gates.
- Accessibility and platform constraints win over visual preference.
- If conflict affects API/data behavior, open a change request.
- If conflict affects only visuals, update the design baseline and visual QA checklist.
