# Tool Boundary Matrix

| Area | AppForger role | AI planning provider | Asset/design tool | Code agent | Source-control app | Runtime/cloud app |
|---|---|---|---|---|---|---|
| Product decisions | source of truth | assists | no | no | records issues optional | no |
| Visual concepts | records | prompts/reviews | creates or refines drafts | implements only | stores assets optional | no |
| UI implementation | packets | reviews | design source after approval | edits code repo | source of truth for code | no |
| Backend | specs/packets | reviews | informs needs | edits backend repo | source of truth for code | runtime |
| Release docs | records | drafts | creates visuals | no | stores release code | deploy target |
