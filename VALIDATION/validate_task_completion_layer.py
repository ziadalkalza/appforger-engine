from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'workflows/operations/task-completion-evidence/README.md',
    'workflows/operations/task-completion-evidence/task-completion-policy.md',
    'workflows/operations/task-completion-evidence/task-status-model.md',
    'workflows/operations/task-completion-evidence/checkpoint-commit-policy.md',
    'workflows/operations/task-completion-evidence/completion-commit-policy.md',
    'workflows/experience-design/task-completion-evidence/done-report-requirements.md',
    'workflows/experience-design/task-completion-evidence/completion-evidence-matrix.md',
    'workflows/operations/task-completion-evidence/task-closeout-checklist.md',
    'workflows/operations/task-completion-evidence/manual-override-policy.md',
    'skills/quality-assurance/close-task-with-evidence/SKILL.md',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('Missing task completion layer files:')
    for p in missing:
        print('-', p)
    raise SystemExit(1)
print('Task completion layer validation passed.')
