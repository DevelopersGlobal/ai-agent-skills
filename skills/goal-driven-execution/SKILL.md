---
name: goal-driven-execution
description: Transforms imperative instructions into declarative goals with verifiable success criteria. Enables autonomous looping until verified completion.
category: think
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Andrej Karpathy's key insight: *"LLMs are exceptionally good at looping until they meet specific goals. Don't tell it what to do — give it success criteria and watch it go."*

This skill converts vague imperative instructions ("make the login work") into declarative goals with concrete, testable success criteria. Agents with clear goals self-correct autonomously. Agents with vague goals produce vague results and require constant intervention.

## When to Use

- Before starting any multi-step task
- When a task has been described imperatively ("do X, then Y, then Z")
- When you're unsure how you'll know when you're "done"
- For long-running or complex implementations

## Process

### Step 1: Extract the Underlying Goal

1. Read the full request.
2. Ask: *What is the user trying to achieve, not just what they asked for?*
3. Write the goal as: **"The task is complete when [observable, verifiable outcome]."**

Example transformation:
- ❌ Imperative: *"Add error handling to the API."*
- ✅ Goal: *"The task is complete when: all API endpoints return structured error responses for 4xx/5xx cases, error responses include a `code`, `message`, and `requestId`, and the existing tests pass."*

**Verify:** The goal statement is observable and testable by a third party.

### Step 2: Define Success Criteria

4. List 3–7 specific, binary success criteria:
   ```
   Success when:
   - [ ] All existing tests pass
   - [ ] New behavior X is demonstrated by test Y
   - [ ] No regressions in file Z
   - [ ] Manual check: [describe what to look for]
   ```
5. Each criterion must be **falsifiable** — you can clearly state when it passes or fails.

**Verify:** Every criterion can be checked without the original author.

### Step 3: Define the Execution Plan

6. Break the goal into ordered steps, each with its own verify check:
   ```
   1. [Step] → verify: [command or check]
   2. [Step] → verify: [command or check]
   3. [Step] → verify: [command or check]
   ```
7. Identify the **first failure mode** — what's most likely to go wrong? Plan for it.

**Verify:** The plan is readable and each step is independently verifiable.

### Step 4: Execute and Loop

8. Follow the plan step-by-step.
9. At each verify checkpoint — actually run the check. Do not skip.
10. If a check fails: diagnose, fix, re-verify. Do not proceed past a failing check.
11. When all checks pass: report completion with evidence.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "The goal is obvious" | Obvious goals still need explicit success criteria. What's obvious to you is ambiguous to an agent. |
| "I'll know when it's done" | That's not a verifiable criterion. Write it down. |
| "The tests will tell me" | Which tests? What do they cover? What don't they cover? |
| "It's too simple for a plan" | Simple tasks rarely fail. Complex tasks without a plan always do. |

## Red Flags

- The task is described as a to-do list, not a goal
- You don't know how you'll verify completion
- You're 80% through and realize the original framing was wrong
- "It seems to work" is your verification strategy

## Verification

- [ ] Goal is stated as an observable, testable outcome
- [ ] Success criteria are listed and binary (pass/fail)
- [ ] Execution plan has verify steps for each phase
- [ ] All verify checks have been run (not just assumed passing)
- [ ] Evidence of completion is documented

## References

- [think-before-coding skill](../think-before-coding/SKILL.md)
- [task-decomposition skill](../task-decomposition/SKILL.md)
