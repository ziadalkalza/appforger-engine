from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'TEST_AUTHORING_AND_EXECUTION/TEST_CASE_GENERATION_LIFECYCLE.md',
    'TEST_AUTHORING_AND_EXECUTION/TEST_CASE_WRITING_RULES.md',
    'TEST_AUTHORING_AND_EXECUTION/ACCEPTANCE_CRITERIA_TO_TEST_CASES.md',
    'TESTING_SKILL_IMPORTS/TESTING_SKILL_IMPORT_PROTOCOL.md',
    'SKILLS/qa_skills/generate_test_cases/SKILL.md',
    'SKILLS/qa_skills/import_testing_skill/SKILL.md',
    'REGISTRIES/TEST_CASE_REGISTRY.md',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('Missing test authoring files:')
    for m in missing:
        print('-', m)
    raise SystemExit(1)
print('Test authoring layer validation passed.')
