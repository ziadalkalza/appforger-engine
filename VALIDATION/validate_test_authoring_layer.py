from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'validation/domains/test-authoring-execution/TEST_CASE_GENERATION_LIFECYCLE.md',
    'validation/domains/test-authoring-execution/TEST_CASE_WRITING_RULES.md',
    'validation/domains/test-authoring-execution/ACCEPTANCE_CRITERIA_TO_TEST_CASES.md',
    'skills/quality/testing-imports/TESTING_SKILL_IMPORT_PROTOCOL.md',
    'skills/quality/qa_skills/generate_test_cases/SKILL.md',
    'skills/quality/qa_skills/import_testing_skill/SKILL.md',
    'registries/TEST_CASE_REGISTRY.md',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('Missing test authoring files:')
    for m in missing:
        print('-', m)
    raise SystemExit(1)
print('Test authoring layer validation passed.')
