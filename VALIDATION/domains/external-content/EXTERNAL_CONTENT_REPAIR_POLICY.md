# External Content Repair Policy

When validation fails, AppForge may repair only safe structural issues:

Safe to auto-create:

- missing `project-control/` starter files
- missing empty registries
- missing `exports/`, `design-assets/`, `local-only/` folders
- missing `APPFORGE_POINTER.md` placeholders
- missing repo `AGENTS.md` from templates

Do not auto-create without user approval:

- GitHub repos
- cloud resources
- Supabase projects
- databases
- paid services
- production secrets
- destructive migrations
- replacing existing source code

If a required code repo folder does not exist, create only a placeholder folder and pointer file unless the user explicitly asks to initialize a real code project.
