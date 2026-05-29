CREATE TABLE IF NOT EXISTS appforge_sync_runs (
  id SERIAL PRIMARY KEY,
  source_id TEXT NOT NULL,
  source_type TEXT NOT NULL,
  status TEXT NOT NULL,
  started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  finished_at TIMESTAMP NULL,
  details JSONB DEFAULT '{}'::jsonb
);
