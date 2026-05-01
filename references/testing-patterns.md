# Testing Patterns Reference

Supporting reference for [test-driven-development](../skills/test-driven-development/SKILL.md) and [integration-testing](../skills/integration-testing/SKILL.md).

## Test Pyramid

```
          ┌────────┐
          │  E2E   │  Few — slow, brittle, expensive
          ├────────┤
          │  Int.  │  Some — real boundaries, real data
          ├────────┤
          │  Unit  │  Many — fast, isolated, deterministic
          └────────┘
```

## Unit Test Patterns

### Arrange-Act-Assert
```
test("returns 404 when user not found", () => {
  // Arrange
  const repo = new UserRepo({ db: fakeDb });
  // Act
  const result = repo.findById("nonexistent-id");
  // Assert
  expect(result).toBeNull();
});
```

### Test naming: behavior, not implementation
- ✅ `"returns empty array when no results match"`
- ❌ `"tests the filter function"`

## Integration Test Patterns

- Use real database (match prod engine type)
- Use real HTTP client (not mock of axios)
- Wrap each test in a transaction, rollback after
- Test contract: what you send, what you get back, what state changed

## AI Output Test Patterns

- Test schema validation (valid JSON? correct fields?)
- Test edge cases: empty response, max-length response, special characters
- Test fallback behavior: what happens when AI returns unexpected format?

## Coverage Rules of Thumb

| Code type | Target |
|-----------|--------|
| Business logic | 90%+ |
| API handlers | 80%+ |
| Utility functions | 70%+ |
| UI components | 60%+ |
| Config/setup | As needed |

Coverage is a floor, not a goal. 100% coverage with bad tests is worse than 70% coverage with good tests.
