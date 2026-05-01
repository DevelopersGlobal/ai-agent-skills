---
name: task-decomposition
description: Breaks features into atomic, independently verifiable tasks. No task should take more than 4 hours. Unblocks parallel work and reduces integration risk.
category: plan
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Large tasks fail in large ways. Decomposed tasks fail in small, fixable ways. This skill breaks any feature or project into atomic tasks — each independently implementable, testable, and deployable.

## When to Use

- Before starting any feature that takes more than half a day
- When a task feels overwhelming or unclear
- When multiple people need to work in parallel

## Process

### Step 1: Identify the Deliverable

1. State what "done" looks like for the whole feature.
2. List all the things that must be true when it's complete.
3. Identify dependencies: what must exist before any task can start?

**Verify:** You can state the full feature goal in 2 sentences.

### Step 2: Decompose Into Atomic Tasks

4. Break the feature into tasks where each task:
   - Can be completed in under 4 hours
   - Has a single, clear output
   - Can be verified independently
   - Can be reverted without breaking other tasks
5. Each task should be: `[verb] [noun] so that [outcome]`
   - ✅ "Add rate limiting to /api/login so that brute-force is prevented"
   - ❌ "Work on the login security stuff"

**Verify:** Every task is under 4 hours. Every task has a clear verify condition.

### Step 3: Order and Parallelism

6. Draw the dependency graph — what blocks what?
7. Identify tasks that can be done in parallel.
8. Sequence tasks so integration happens incrementally (not as one big bang at the end).

**Verify:** The dependency order is clear. No unnecessary sequential dependencies.

### Step 4: Estimate and Adjust

9. For each task, estimate: best case / worst case / expected.
10. If any task's worst case > 1 day: decompose further.
11. Total estimate sanity check: does it add up to a reasonable timeline?

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "I'll figure it out as I go" | Decomposition takes 30 minutes. Rework from poor planning takes days. |
| "It's too complex to break down" | Everything can be decomposed. Start with what you know, decompose the rest later. |
| "The tasks are too granular" | Granular tasks ship continuously. Coarse tasks ship never. |

## Verification

- [ ] Each task is under 4 hours
- [ ] Each task has a single verify condition
- [ ] Dependencies mapped — no circular dependencies
- [ ] Parallel work identified

## References

- [goal-driven-execution skill](../goal-driven-execution/SKILL.md)
- [multi-agent-orchestration skill](../multi-agent-orchestration/SKILL.md)
