# Migration Policy

Schema changes require:
- migration description
- affected tables
- rollback plan
- data safety review
- project-control sync impact review
- approval if production/team-shared backend is affected

For SQLite, migration files should be versioned. For Supabase/Postgres, SQL migrations should be committed and reviewed.
