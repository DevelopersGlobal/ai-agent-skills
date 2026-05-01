---
name: incremental-coding
description: Build in verifiable increments. Never implement more than can be tested right now. Ship partial working systems over complete broken ones.
category: build
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

The biggest risk in software development is building a lot of code that doesn't work. Incremental coding limits this risk: build a little, verify it works, build more. At every step, the system is in a known-good state.

## When to Use

- Any implementation that will take more than 2 hours
- When building in a complex domain you're uncertain about
- When multiple components need to integrate

## Process

### Step 1: Define the First Increment

1. What is the smallest possible thing you can build that provides value and can be verified?
2. It doesn't have to be feature-complete — just correct and verifiable.
3. Example: "Add the endpoint skeleton with hardcoded response" before adding business logic.

**Verify:** The first increment can be verified in under 5 minutes.

### Step 2: Build → Verify → Commit

4. Build only the first increment.
5. Run tests. Verify manually if needed. Confirm it works.
6. Commit this working state.
7. Repeat for the next increment.

**Verify:** There is a working commit after each increment.

### Step 3: Integration Continuously

8. Integrate with the real system as early as possible — not at the end.
9. Test against real dependencies (DB, API, etc.) as early as possible.
10. Fake integrations (mocks) should be replaced with real ones by the end.

**Verify:** By completion, all mocks replaced with real integration.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "I need to build it all to know if it works" | No. Build the first piece and test it. Uncertainty is always reducible. |
| "Integration is at the end" | Integration pain is proportional to time since last integration. Integrate continuously. |

## Verification

- [ ] Implementation built in verifiable increments
- [ ] Working commit exists after each increment
- [ ] No long stretches of "broken" state in git history
- [ ] All mocks replaced with real integrations by completion

## References

- [test-driven-development skill](../test-driven-development/SKILL.md)
- [task-decomposition skill](../task-decomposition/SKILL.md)
