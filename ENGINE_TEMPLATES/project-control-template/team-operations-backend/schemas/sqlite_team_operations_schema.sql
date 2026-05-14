-- AppForge Team Operations Backend starter schema
-- Canonical documents remain in docs/project-control/repos/Figma/storage.
-- This schema stores operational state and metadata links only.

create table if not exists team_members (
  member_id text primary key,
  display_name text not null,
  email text,
  status text not null default 'active',
  source_path text,
  created_at text default CURRENT_TIMESTAMP,
  updated_at text default CURRENT_TIMESTAMP
);

create table if not exists role_assignments (
  assignment_id text primary key,
  member_id text references team_members(member_id),
  role_name text not null,
  status text not null default 'active',
  source_path text,
  created_at text default CURRENT_TIMESTAMP
);

create table if not exists operational_tasks (
  task_id text primary key,
  title text not null,
  status text not null,
  owner_member_id text,
  owner_role text,
  source_packet_path text,
  source_registry_path text,
  blocked_by text,
  next_action text,
  risk_level text default 'medium',
  updated_at text default CURRENT_TIMESTAMP
);

create table if not exists approvals (
  approval_id text primary key,
  artifact_type text not null,
  artifact_id text not null,
  status text not null,
  approver_member_id text,
  approver_role text,
  source_path text,
  approved_at timestamp,
  created_at text default CURRENT_TIMESTAMP
);

create table if not exists handoffs (
  handoff_id text primary key,
  from_role text,
  to_role text,
  related_task_id text,
  status text not null,
  source_packet_path text,
  created_at text default CURRENT_TIMESTAMP,
  completed_at timestamp
);

create table if not exists conflicts (
  conflict_id text primary key,
  conflict_type text not null,
  severity text not null,
  status text not null,
  affected_artifacts text,
  resolution_path text,
  source_path text,
  created_at text default CURRENT_TIMESTAMP,
  resolved_at timestamp
);

create table if not exists reviews (
  review_id text primary key,
  artifact_id text not null,
  reviewer_member_id text,
  status text not null,
  source_path text,
  created_at text default CURRENT_TIMESTAMP
);

create table if not exists release_blockers (
  blocker_id text primary key,
  release_id text,
  severity text not null,
  status text not null,
  owner_member_id text,
  source_path text,
  created_at text default CURRENT_TIMESTAMP,
  resolved_at timestamp
);

create table if not exists agent_runs (
  agent_run_id text primary key,
  agent_id text,
  provider text,
  brand_family text,
  status text not null,
  packet_path text,
  output_report_path text,
  warnings text,
  started_at timestamp,
  finished_at timestamp
);

create table if not exists job_runs (
  job_run_id text primary key,
  job_id text,
  trigger_type text,
  status text not null,
  output_report_path text,
  warnings text,
  started_at timestamp,
  finished_at timestamp
);

create table if not exists workflow_stage_state (
  stage_id text primary key,
  stage_name text not null,
  status text not null,
  current_baseline text,
  source_path text,
  updated_at text default CURRENT_TIMESTAMP
);

create table if not exists secret_metadata (
  secret_name text primary key,
  environment text not null,
  stored_in text not null,
  allowed_roles text not null,
  status text not null,
  last_rotated timestamp,
  value_stored_here integer not null default 0
);

create table if not exists audit_events (
  audit_event_id text primary key,
  actor_id text,
  action text not null,
  entity_type text not null,
  entity_id text not null,
  risk_level text default 'low',
  source_path text,
  created_at text default CURRENT_TIMESTAMP
);

create table if not exists sync_events (
  sync_id text primary key,
  direction text not null,
  status text not null,
  source text,
  target text,
  report_path text,
  conflicts text,
  created_at text default CURRENT_TIMESTAMP
);
