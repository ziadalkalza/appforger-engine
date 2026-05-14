# Required Questions

The minimal onboarding gate must collect these answers before real project work starts.

| ID | Question | Why it is required | Can be unknown? |
|---|---|---|---|
| Q1 | Project name? | Names project-control, repos, docs, registries, packets. | No |
| Q2 | New or existing project? | Chooses initializer vs import workflow. | No |
| Q2A | Is this an ongoing project? | Ongoing projects require initial code context bootstrap and staleness tracking. | No |
| Q3 | Single-user or team mode? | Activates team rules, PR rules, named approvers. | No |
| Q4 | Target app type? | Selects mobile/web/backend/release tracks. | Yes only if no implementation requested |
| Q5 | Starting point? | Chooses scratch/import/flexible workflow. | No |
| Q6 | Workflow preference? | Chooses standard/flexible/stage override defaults. | Yes, default to standard until changed |
| Q7 | Backend needed? | Blocks backend/frontend/API decisions. | Yes if UI-only or requirements phase |
| Q8 | Design workflow? | Chooses Figma/sandbox/imported baseline route. | Yes if not doing UI yet |
| Q9 | Tool consistency mode for linked tasks? | Controls whether dependent tasks should stay on one tool family or allow mixed tools with reconciliation. | No |
| Q10 | Preferred code provider? | Affects execution packet adaptation. | Yes: decide per task |
| Q11 | Docs storage location? | Determines where shared docs live and how they are referenced. | Yes: local docs/ default |
| Q12 | Context backend mode? | Determines retrieval/indexing behavior. | Yes: local JSONL/default file mode |
| Q13 | Automation level? | Determines jobs/packets/hooks/actions safety. | Yes: default local validation/reporting |
| Q14 | Public release expected? | Determines release readiness expectations. | Yes |
| Q15 | Likely integration needs? | Helps plan integrations without activating them. | Yes |
