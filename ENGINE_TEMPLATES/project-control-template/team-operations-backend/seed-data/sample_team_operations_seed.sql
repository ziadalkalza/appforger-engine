insert into team_members(member_id, display_name, email, status, source_path)
values ('TM-001', 'Project Owner', 'owner@example.com', 'active', 'REGISTRIES/TEAM_MEMBER_REGISTRY.md');

insert into role_assignments(assignment_id, member_id, role_name, status, source_path)
values ('RA-001', 'TM-001', 'AppForge Operator', 'active', 'REGISTRIES/ROLE_ASSIGNMENT_REGISTRY.md');

insert into operational_tasks(task_id, title, status, owner_role, source_packet_path, next_action)
values ('TASK-SAMPLE-001', 'Review login API baseline', 'blocked', 'Backend Lead', 'EXECUTION_PACKETS/TASK-SAMPLE-001.md', 'Approve or revise API baseline');
