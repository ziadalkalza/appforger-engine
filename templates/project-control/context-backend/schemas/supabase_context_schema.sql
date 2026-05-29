-- AppForge Supabase context schema starter
-- Run in Supabase SQL editor after reviewing security/RLS.

create table if not exists public.appforge_projects (
  id text primary key,
  name text not null,
  canonical_source text not null default 'project-control-github',
  created_at timestamptz default now()
);

create table if not exists public.appforge_artifacts (
  id text primary key,
  project_id text references public.appforge_projects(id) on delete cascade,
  artifact_type text not null,
  source_path text not null,
  approval_status text default 'unknown',
  baseline_version text,
  is_current boolean default true,
  source_commit text,
  metadata jsonb default '{}'::jsonb,
  updated_at timestamptz default now()
);

create table if not exists public.appforge_sync_runs (
  id bigserial primary key,
  project_id text references public.appforge_projects(id) on delete cascade,
  sync_mode text not null,
  status text not null,
  started_at timestamptz default now(),
  finished_at timestamptz,
  report jsonb default '{}'::jsonb
);

-- Enable RLS before multi-user use.
-- alter table public.appforge_projects enable row level security;
-- alter table public.appforge_artifacts enable row level security;
