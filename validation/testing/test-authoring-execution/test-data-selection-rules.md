# Test Data Selection Rules

Test data should include:

- normal users/items
- empty states
- boundary values
- invalid inputs
- permission/role variants
- network/API failure cases
- large or slow-response examples where relevant

Test data belongs in implementation repos or `project-control/validation/domains/test-data/`, not in the reusable engine.
