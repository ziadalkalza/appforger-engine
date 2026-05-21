-- AppForge generic Postgres context schema starter
create table if not exists appforge_projects (
  id text primary key,
  name text not null,
  canonical_source text not null default 'project-control-github',
  created_at timestamptz default now()
);

create table if not exists appforge_artifacts (
  id text primary key,
  project_id text references appforge_projects(id),
  artifact_type text not null,
  source_path text not null,
  approval_status text default 'unknown',
  baseline_version text,
  is_current boolean default true,
  source_commit text,
  metadata jsonb default '{}'::jsonb,
  updated_at timestamptz default now()
);

create table if not exists appforge_sync_runs (
  id bigserial primary key,
  project_id text references appforge_projects(id),
  sync_mode text not null,
  status text not null,
  started_at timestamptz default now(),
  finished_at timestamptz,
  report jsonb default '{}'::jsonb
);

create table if not exists appforge_retrieval_logs (
  id bigserial primary key,
  project_id text references appforge_projects(id),
  query text not null,
  filters jsonb default '{}'::jsonb,
  result_count int default 0,
  created_at timestamptz default now()
);
