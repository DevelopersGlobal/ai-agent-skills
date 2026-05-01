---
name: surgical-changes
description: Enforces minimal code modifications — touch only what you must. Prevents drive-by refactoring, comment deletions, and style changes unrelated to the task.
category: build
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Every changed line is a line the reviewer must inspect, a line that could introduce a regression, and a line that will appear in the git blame forever. Unnecessary changes are costly.

AI agents often "improve" adjacent code, reformat files, rename variables for consistency, or delete "dead" code — all without being asked. This creates noisy diffs, unexpected behavior changes, and broken trust.

This skill enforces a hard rule: **every changed line must trace directly to the user's request.**

## When to Use

- Any time you are modifying existing code (not creating new files)
- When your diff is larger than you expected
- When reviewing your own generated changes before presenting them

## Process

### Step 1: Establish the Change Boundary

1. Read the task carefully. Write down exactly which files and functions need to change.
2. Draw a mental boundary: *"Everything outside this boundary is out of scope."*
3. List what you will NOT change, even if you'd do it differently:
   - Adjacent functions
   - Variable naming conventions
   - Comment style
   - Import order
   - Formatting/whitespace (unless fixing a specific bug)

**Verify:** You can name the specific functions/lines that need to change.

### Step 2: Make Only the Required Changes

4. Make the changes — and only the changes — within the defined boundary.
5. If you notice something wrong outside the boundary:
   - **Mention it in a comment** — don't fix it silently
   - Example: *"Note: I noticed `fetchUser` has no error handling, but I'm leaving that for a separate PR."*
6. If your changes made imports/variables/functions unused: remove only those created by YOUR changes. Leave pre-existing dead code alone (unless asked).

**Verify:** No line changed that wasn't part of the defined scope.

### Step 3: Review Your Own Diff

7. Read through your diff line by line.
8. For each changed line, ask: *"Why did I change this?"*
   - If you can't answer → revert it
9. Flag any changes that are purely cosmetic and ask: *"Should I include this?"*

**Verify:** Every changed line has a clear reason directly tied to the task.

### Step 4: Document Scope Decisions

10. In your PR/commit message, explicitly note what you chose NOT to change and why:
    - *"Did not refactor the adjacent `parseDate` function — out of scope for this fix."*

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "I improved it while I was there" | That's a separate PR. Drive-by improvements hide bugs and inflate diffs. |
| "The old comment was wrong" | Fix comments related to your change. Leave others for a documentation PR. |
| "I made the code more consistent" | Consistency PRs should be standalone. Don't bundle them. |
| "It's just whitespace" | Whitespace changes cause merge conflicts and obscure real diffs in blame. |
| "The dead code is obviously wrong" | File an issue. Don't delete pre-existing code without explicit approval. |

## Red Flags

- Your diff is 3× larger than the feature size suggests
- You changed files that aren't related to the task
- You reformatted a file "while you were there"
- You renamed variables for consistency
- You deleted comments or code you didn't fully understand
- Your PR description says "and also fixed a few other things"

## Verification

- [ ] Every changed line traces to the task description
- [ ] No cosmetic-only changes bundled in (or explicitly approved)
- [ ] Pre-existing dead code left untouched (or flagged, not deleted)
- [ ] Changes to adjacent unrelated code: zero
- [ ] Diff size is proportional to task size

## References

- [simplicity-first skill](../simplicity-first/SKILL.md)
- [code-review skill](../code-review/SKILL.md)
- Karpathy: *"They still sometimes change/remove comments and code they don't sufficiently understand as side effects, even if orthogonal to the task."*
