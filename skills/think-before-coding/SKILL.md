---
name: think-before-coding
description: Forces explicit reasoning before writing any code. Surfaces assumptions, manages confusion, and prevents hallucination by demanding clarity upfront.
category: think
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

AI agents default to writing code immediately — even when the request is ambiguous, the context is incomplete, or multiple valid interpretations exist. This skill forces a deliberate thinking phase before any implementation begins.

The result: fewer rewrites, fewer wrong-direction implementations, and fewer "I assumed X" surprises.

## When to Use

Activate this skill **before writing any code** when:
- The request is ambiguous or underspecified
- Multiple valid implementations exist
- You are unsure about an existing system's constraints
- The task touches security, data integrity, or public APIs
- You feel the urge to "just start coding" to make progress

## Process

### Phase 1: Understand the Request

1. **Read the full request** — Do not skim. Re-read once.
2. **Identify ambiguities** — List every decision you would have to make silently:
   - What counts as "success"?
   - What are the inputs and expected outputs?
   - What should NOT change?
   - Are there existing patterns to follow?
3. **Surface assumptions** — Write them out: *"I am assuming X because Y."*
4. **Check for contradictions** — Does the request contradict itself or existing code?

**Verify:** Can you state the goal in one clear sentence? If not, ask before proceeding.

### Phase 2: Clarify Before Acting

5. If **genuinely ambiguous**, ask a focused clarifying question — not a list of 10 questions. Pick the one blocker.
6. If multiple valid approaches exist, **present 2–3 options with tradeoffs**, then ask which to proceed with.
7. If something seems wrong with the request, **say so directly** — don't silently work around it.

**Verify:** You have a clear, agreed-upon interpretation of the task.

### Phase 3: State Your Plan

8. Before writing code, state:
   - What you will build
   - What you will NOT touch
   - What success looks like (your verification criteria)
9. For multi-step tasks, write a brief plan:
   ```
   1. [Step] → verify: [check]
   2. [Step] → verify: [check]
   3. [Step] → verify: [check]
   ```

**Verify:** The plan is agreed upon, or you have received approval to proceed.

### Phase 4: Code

10. Now write the code — following the plan exactly.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "I'll figure it out as I go" | Unknown unknowns compound. 5 minutes of thinking saves 50 minutes of rewriting. |
| "The request is clear enough" | If you can't state the goal in one sentence, it's not clear enough. |
| "Asking questions slows things down" | Wrong direction is infinitely slower than a 30-second clarifying question. |
| "I'll handle edge cases later" | Edge cases not considered upfront become bugs found in production. |
| "I can always refactor" | You almost never will. Design now. |

## Red Flags

- You're already writing code and you haven't stated what success looks like
- You made a silent assumption about what the user wants
- You chose between two approaches without mentioning the tradeoff
- You're solving a problem the user didn't ask about
- You're 100 lines in and realize you misunderstood the goal

## Verification

Before leaving this phase, confirm:
- [ ] The goal is stated in one clear sentence
- [ ] All major assumptions are explicitly named
- [ ] Ambiguities are resolved (or flagged for the user)
- [ ] A brief plan exists with verification criteria per step
- [ ] You know what you will NOT touch

## References

- [Andrej Karpathy on LLM coding pitfalls](https://x.com/karpathy/status/2015883857489522876)
- [goal-driven-execution skill](../goal-driven-execution/SKILL.md)
- [idea-to-spec skill](../idea-to-spec/SKILL.md)
