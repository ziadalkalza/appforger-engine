from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'validation/testing/test-authoring-execution/test-case-generation-lifecycle.md',
    'validation/testing/test-authoring-execution/test-case-writing-rules.md',
    'validation/testing/test-authoring-execution/acceptance-criteria-to-test-cases.md',
    'skills/quality-assurance/testing-imports/testing-skill-import-protocol.md',
    'skills/quality-assurance/generate-test-cases/SKILL.md',
    'skills/quality-assurance/import-testing-skill/SKILL.md',
    'registries/project-control/test-case-registry.md',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('Missing test authoring files:')
    for m in missing:
        print('-', m)
    raise SystemExit(1)
print('Test authoring layer validation passed.')
