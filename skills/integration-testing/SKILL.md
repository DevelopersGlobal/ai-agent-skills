---
name: integration-testing
description: Test real system boundaries, not mocks of mocks. Integration tests verify that components work together, not that they work in isolation.
category: test
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Unit tests verify components work in isolation. Integration tests verify they work together. The gap between these two is where most production bugs hide. This skill ensures integration tests cover the real system boundaries.

## When to Use

- After unit tests are passing
- Before any feature ships to production
- When testing database, API, or third-party service interactions

## Process

### Step 1: Identify Real Boundaries

1. Map every boundary in the system: code ↔ database, code ↔ external API, service ↔ service, frontend ↔ backend.
2. Rank boundaries by failure impact.
3. Integration tests should cover the top 5 highest-impact boundaries.

**Verify:** Boundary map created. Top 5 prioritized.

### Step 2: Test Real, Not Mocked

4. Use a real test database (not SQLite in-memory if prod uses PostgreSQL).
5. Use contract tests for external APIs — test against a recorded real response.
6. Use test containers for services that would otherwise require mocking.
7. Mock only: third-party services you can't control, slow services with contract tests already in place.

**Verify:** No internal boundaries are mocked in integration tests.

### Step 3: Test the Happy Path AND Failure Cases

8. Happy path: the system works end-to-end for the primary use case.
9. Failure cases: database down, API returns 500, timeout, malformed response.
10. State verification: after each action, verify the state in the real database.

**Verify:** At least 1 failure case per boundary is tested.

### Step 4: Keep Tests Independent

11. Each test cleans up its own state (transactions rolled back, test data deleted).
12. Tests don't share state with each other.
13. Tests can run in any order.

**Verify:** Test suite passes when run in random order.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "Unit tests are enough" | Unit tests with mocks test that your mocks work, not your system. |
| "Integration tests are slow" | Slow tests are better than discovering bugs in production. Optimize the setup, not the coverage. |
| "We test in staging" | Staging is not a substitute for automated tests. It's too slow and too manual. |

## Verification

- [ ] Real boundaries identified and prioritized
- [ ] Integration tests use real dependencies (not mocks of internal components)
- [ ] Happy path and failure cases tested for each boundary
- [ ] Tests are independent (can run in any order)
- [ ] Test cleanup is reliable

## References

- [test-driven-development skill](../test-driven-development/SKILL.md)
- [references/testing-patterns.md](../../references/testing-patterns.md)
