---
name: test-driven-development
description: Red-green-refactor cycle with meaningful coverage. Tests are written before implementation. Coverage is a side effect of good tests, not the goal.
category: test
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

TDD is the discipline of writing a failing test before writing implementation code. It forces you to think about the interface before the internals, produces tests that actually test behavior (not just coverage), and gives you a safety net for every refactor.

AI agents skip tests constantly. This skill makes tests non-optional.

## When to Use

- Starting any new feature or function
- Fixing any bug (write a test that reproduces the bug first)
- Refactoring existing code (ensure test coverage before you start)

## Process

### Step 1: Write a Failing Test (Red)

1. Write a test for the behavior you want — **before** writing implementation.
2. The test should describe **what** the code does, not **how**:
   - ✅ `test("returns 404 when user not found")`
   - ❌ `test("calls findById with the user id")`
3. Run the test. Confirm it **fails** for the right reason (not a syntax error — a missing implementation).

**Verify:** Test runs and fails with a clear "not implemented" or "undefined" error.

### Step 2: Write Minimum Code (Green)

4. Write the minimum implementation to make the test pass.
5. Do not write more than the test requires — resist the urge to add logic for future cases.
6. Run the test. Confirm it **passes**.

**Verify:** All tests pass. No new tests added yet.

### Step 3: Refactor (Refactor)

7. Now clean up the implementation — no new behavior, only improved structure.
8. Run tests after every refactoring step — do not batch refactors.
9. If tests break during refactor: revert immediately, refactor more carefully.

**Verify:** Tests still pass after refactor. Code is cleaner.

### Step 4: Repeat for Each Behavior

10. Repeat steps 1–3 for each distinct behavior of the feature.
11. Test pyramid: many unit tests, fewer integration tests, minimal end-to-end tests.

### Step 5: Coverage Sanity Check

12. Run coverage report. Flag any critical paths with 0% coverage.
13. Do NOT chase a coverage number — write tests for behaviors that matter.

**Verify:** All happy paths and key edge cases have tests. Coverage report reviewed.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "I'll add tests after" | After never comes. And after-the-fact tests test your implementation, not the behavior. |
| "This code is too simple to test" | Simple code breaks in unexpected ways when requirements change. |
| "Integration tests are enough" | Unit tests catch bugs faster, run faster, and localize failures better. |
| "We don't have time for TDD" | You have time for the bug investigation that comes without TDD? |

## Red Flags

- Tests were written after the implementation
- Tests test internal implementation details (private methods, DB queries) rather than behavior
- "Happy path only" test coverage
- Tests pass even when you break the implementation (mocked away the real behavior)
- Coverage target hit by testing trivial getters/setters

## Verification

- [ ] Tests written before implementation (or alongside for bug fixes)
- [ ] Each test describes a specific behavior
- [ ] Red-green-refactor cycle followed
- [ ] All tests pass
- [ ] Key edge cases covered (empty input, null, boundary values)
- [ ] Coverage report reviewed for critical path gaps

## References

- [debugging-methodology skill](../debugging-methodology/SKILL.md)
- [references/testing-patterns.md](../../references/testing-patterns.md)
