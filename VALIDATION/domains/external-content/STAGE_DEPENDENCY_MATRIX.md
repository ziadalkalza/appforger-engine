# Stage Dependency Matrix

| Stage | Required external content |
|---|---|
| ideation | project-control exists |
| requirements | project-control registries exist |
| UX/UI/Figma | project-control + design-assets + exports |
| design baseline approval | Figma link/exports + baseline registry |
| backend | backend folder/repo + backend stack decision + env placeholder |
| API approval | API registry + backend baseline registry |
| iOS frontend | ios repo + iOS AGENTS + valid design/API baselines |
| Android frontend | android repo + Android AGENTS + valid design/API baselines |
| Web frontend | web repo + Web AGENTS + valid design/API baselines |
| integration | backend + selected frontend repos + API baseline |
| QA | exports + test registry + relevant repos |
| release docs | release registry + QA evidence + app store/web deployment docs |
