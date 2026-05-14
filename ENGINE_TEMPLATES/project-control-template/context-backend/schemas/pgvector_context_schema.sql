-- Optional pgvector schema starter
create extension if not exists vector;

create table if not exists public.appforge_context_chunks (
  id text primary key,
  project_id text not null,
  artifact_id text,
  source_path text not null,
  chunk_text text not null,
  embedding vector(384), -- adjust dimension to embedding model
  metadata jsonb default '{}'::jsonb,
  indexed_at timestamptz default now()
);

create index if not exists appforge_context_chunks_embedding_idx
on public.appforge_context_chunks using ivfflat (embedding vector_cosine_ops);
