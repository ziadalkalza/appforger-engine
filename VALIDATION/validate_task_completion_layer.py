from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'TASK_COMPLETION_AND_EVIDENCE/README.md',
    'TASK_COMPLETION_AND_EVIDENCE/TASK_COMPLETION_POLICY.md',
    'TASK_COMPLETION_AND_EVIDENCE/TASK_STATUS_MODEL.md',
    'TASK_COMPLETION_AND_EVIDENCE/CHECKPOINT_COMMIT_POLICY.md',
    'TASK_COMPLETION_AND_EVIDENCE/COMPLETION_COMMIT_POLICY.md',
    'TASK_COMPLETION_AND_EVIDENCE/DONE_REPORT_REQUIREMENTS.md',
    'TASK_COMPLETION_AND_EVIDENCE/COMPLETION_EVIDENCE_MATRIX.md',
    'TASK_COMPLETION_AND_EVIDENCE/TASK_CLOSEOUT_CHECKLIST.md',
    'TASK_COMPLETION_AND_EVIDENCE/MANUAL_OVERRIDE_POLICY.md',
    'SKILLS/qa_skills/close_task_with_evidence/SKILL.md',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('Missing task completion layer files:')
    for p in missing:
        print('-', p)
    raise SystemExit(1)
print('Task completion layer validation passed.')
