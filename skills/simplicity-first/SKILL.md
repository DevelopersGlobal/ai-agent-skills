---
name: simplicity-first
description: Prevents overengineering by enforcing minimum viable code. No speculative features, no premature abstractions, no unnecessary complexity.
category: build
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

AI agents trend toward complexity. They add abstractions "for flexibility," error handling for impossible cases, and configuration for things that will never change. Left unchecked, they turn 50-line solutions into 500-line systems.

This skill enforces a hard constraint: **write the minimum code that solves the stated problem and nothing more.**

Andrej Karpathy's observation: *"They really like to overcomplicate code and APIs, bloat abstractions, don't clean up dead code... implement a bloated construction over 1000 lines when 100 would do."*

## When to Use

- Starting any new implementation
- When you feel the urge to add "just one more abstraction"
- When reviewing your own generated code
- When a simple task balloons into a complex solution

## Process

### Step 1: Define the Minimum Viable Solution

1. State what the code **must** do — write it as a list of requirements.
2. For each potential addition, ask: *"Was this explicitly requested?"*
   - If no → do not add it.
3. Write the simplest possible implementation that satisfies each requirement.

**Verify:** You can trace every line of code back to a stated requirement.

### Step 2: Apply the Simplicity Test

4. After writing, read through the code and flag:
   - Abstractions used only once → inline them
   - Parameters never customized → hardcode them
   - Error handling for impossible scenarios → remove it
   - "Future-proofing" that wasn't asked for → delete it
   - Configuration flags for things that won't vary → remove them

5. Ask: *"Would a senior engineer call this overcomplicated?"* If yes, simplify.

**Verify:** Each abstraction is used in at least 2 places; each parameter is actually varied.

### Step 3: Count the Lines

6. If your solution is more than 3× the length you'd expect for the task, something is wrong.
7. Actively look for ways to reduce line count without sacrificing readability.

> Rule of thumb: If 200 lines could be 50, rewrite it.

**Verify:** You've made at least one active attempt to reduce complexity.

### Step 4: Verify Functional Correctness

8. Run the tests. All pass?
9. Manually check the primary use case.
10. Check that no pre-existing tests regressed.

**Verify:** All tests pass. No regressions.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "We might need this later" | YAGNI. Add it when you need it. Unused code is a liability. |
| "The abstraction makes it more flexible" | Flexibility you don't need adds complexity you always pay for. |
| "I'm following the existing patterns" | Don't cargo-cult complex patterns into simple contexts. |
| "It's only a few more lines" | Every extra line is a line to maintain, debug, and understand. |
| "This is more robust" | Robust against what? Name the failure mode you're defending against. |

## Red Flags

- You added a factory for a class that's instantiated once
- You added configuration for values that never change
- You wrote error handling for an operation that cannot fail
- The abstraction layer is larger than the code it abstracts
- You added a parameter "just in case"
- Your PR adds 400 lines but the feature is 40 lines of actual logic

## Verification

- [ ] Every line traces back to a stated requirement
- [ ] No speculative features added
- [ ] All abstractions used in 2+ places
- [ ] No error handling for impossible scenarios
- [ ] Line count is proportional to task complexity
- [ ] All tests pass

## References

- [surgical-changes skill](../surgical-changes/SKILL.md)
- [refactoring skill](../refactoring/SKILL.md)
- YAGNI principle — Martin Fowler
