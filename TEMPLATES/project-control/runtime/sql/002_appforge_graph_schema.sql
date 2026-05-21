CREATE TABLE IF NOT EXISTS appforge_graph_nodes (
  id TEXT PRIMARY KEY,
  node_type TEXT NOT NULL,
  payload JSONB DEFAULT '{}'::jsonb
);

CREATE TABLE IF NOT EXISTS appforge_graph_edges (
  id TEXT PRIMARY KEY,
  from_id TEXT NOT NULL,
  to_id TEXT NOT NULL,
  edge_type TEXT NOT NULL,
  payload JSONB DEFAULT '{}'::jsonb
);
