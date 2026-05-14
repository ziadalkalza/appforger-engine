CREATE CONSTRAINT appforge_node_id IF NOT EXISTS FOR (n:AppForgerNode) REQUIRE n.id IS UNIQUE;
CREATE INDEX appforge_node_type IF NOT EXISTS FOR (n:AppForgerNode) ON (n.type);
