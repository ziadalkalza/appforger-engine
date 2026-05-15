from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'workflows/operations/task-completion-evidence/README.md',
    'workflows/operations/task-completion-evidence/TASK_COMPLETION_POLICY.md',
    'workflows/operations/task-completion-evidence/TASK_STATUS_MODEL.md',
    'workflows/operations/task-completion-evidence/CHECKPOINT_COMMIT_POLICY.md',
    'workflows/operations/task-completion-evidence/COMPLETION_COMMIT_POLICY.md',
    'workflows/operations/task-completion-evidence/DONE_REPORT_REQUIREMENTS.md',
    'workflows/operations/task-completion-evidence/COMPLETION_EVIDENCE_MATRIX.md',
    'workflows/operations/task-completion-evidence/TASK_CLOSEOUT_CHECKLIST.md',
    'workflows/operations/task-completion-evidence/MANUAL_OVERRIDE_POLICY.md',
    'skills/quality/qa_skills/close_task_with_evidence/SKILL.md',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('Missing task completion layer files:')
    for p in missing:
        print('-', p)
    raise SystemExit(1)
print('Task completion layer validation passed.')
