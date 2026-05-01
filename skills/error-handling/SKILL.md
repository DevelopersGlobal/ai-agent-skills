---
name: error-handling
description: Graceful degradation and meaningful error messages. Errors are first-class citizens, not afterthoughts. Every error path is designed, not discovered.
category: harden
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Error handling is not defensive programming — it's a user experience. When things go wrong (and they will), the system should degrade gracefully, give users actionable information, and leave enough telemetry to diagnose and fix the problem.

## When to Use

- When writing any code that can fail (I/O, network, parsing, user input)
- When reviewing error handling in existing code
- Before any service goes to production

## Process

### Step 1: Design Error Paths Explicitly

1. For every operation, list: what can fail? What does failure look like?
2. Classify failures:
   - **Transient**: Retry likely to succeed (network blip, temporary unavailability)
   - **Client error**: Bad input from the caller (4xx) — don't retry
   - **System error**: Internal failure (5xx) — alert, investigate
3. Design the failure path for each class before writing the happy path.

**Verify:** Error classes defined for every external operation.

### Step 2: Meaningful Error Messages

4. Every error message answers: what went wrong? How can the caller fix it?
   - ✅ "Invalid email format. Expected: user@domain.com"
   - ❌ "Validation error"
5. User-facing errors: friendly language, no stack traces.
6. Developer-facing errors (logs): full context, request ID, stack trace.
7. Never expose internal system details (DB schema, file paths) in user-facing errors.

**Verify:** Each error message would help a user or developer understand and fix the problem.

### Step 3: Retry with Backoff

8. Transient errors: retry with exponential backoff + jitter.
9. Maximum retries: 3 (not infinite).
10. After max retries: fail with a clear error, log the final failure.
11. Non-transient errors (validation, auth): never retry.

**Verify:** Retry logic has a maximum. Non-transient errors don't retry.

### Step 4: Graceful Degradation

12. Identify non-critical dependencies. If they fail, degrade — don't crash.
13. Example: recommendation engine fails → show default content, not 500.
14. Circuit breaker pattern for failing dependencies: fail fast after threshold, recover automatically.

**Verify:** Every non-critical dependency has a defined degraded state.

### Step 5: Structured Error Responses (APIs)

15. API errors return consistent structure:
    ```json
    {
      "error": {
        "code": "INVALID_EMAIL",
        "message": "The email address format is invalid.",
        "requestId": "req_abc123"
      }
    }
    ```
16. HTTP status codes used correctly: 400 (client error), 404 (not found), 429 (rate limited), 500 (server error).

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "I'll add error handling later" | Later means in production, under pressure, while users are impacted. |
| "This can't fail" | Everything can fail. Network calls, disk writes, parsing — all can fail. |
| "The error message doesn't matter" | It matters when a developer is debugging at 2am. |

## Verification

- [ ] Error classes defined for every external operation
- [ ] Error messages answer: what went wrong? How to fix?
- [ ] Transient errors retry with max limit
- [ ] Non-critical dependencies have graceful degraded states
- [ ] API errors return consistent structured format
- [ ] No internal system details in user-facing errors

## References

- [observability skill](../observability/SKILL.md)
- [debugging-methodology skill](../debugging-methodology/SKILL.md)
