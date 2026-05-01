---
name: git-workflow
description: Trunk-based development with atomic commits, clean history, and meaningful commit messages. Every commit should be deployable.
category: ship
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Git is not just a backup system — it's a communication tool. Clean git history enables fast debugging (git bisect), clear attribution, and safe reverts. This skill enforces atomic commits, meaningful messages, and trunk-based development.

## When to Use

- Before making any commit
- When reviewing a PR's git history
- When setting up a new project

## Process

### Step 1: Atomic Commits

1. Each commit should represent ONE logical change — not a day's worth of work.
2. A commit should be: independently deployable, independently revertable.
3. Never commit "WIP" or partial implementations.

**Verify:** You could revert this commit without affecting adjacent functionality.

### Step 2: Commit Message Format

4. Follow Conventional Commits:
   ```
   type(scope): short summary (max 72 chars)
   
   Body: what changed and WHY (not how — the diff shows how).
   
   Closes: #issue-number
   ```
5. Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
6. The summary is imperative mood: "Add feature" not "Added feature"

**Verify:** Message passes: `feat|fix|docs|...(<scope>): <summary>` format.

### Step 3: Trunk-Based Development

7. Work directly on `main` for small changes (<1 day of work).
8. For larger features: short-lived feature branches (max 2 days), frequent merges to main.
9. Never let a branch live more than 3 days without merging or rebasing.
10. Use feature flags for incomplete features, not long-lived branches.

**Verify:** No branch is more than 2 days old without a merge/rebase plan.

### Step 4: Pre-Commit Gates

11. Before every commit: tests pass, linter passes, no secrets in diff.
12. Use pre-commit hooks to enforce automatically.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "I'll clean up the commits later" | You won't. Clean as you go. |
| "The commit message doesn't matter" | It matters in 6 months when you're bisecting a production bug. |
| "Feature branches protect main" | Long-lived branches cause merge nightmares. Trunk-based is safer. |

## Verification

- [ ] Commits are atomic and independently deployable
- [ ] Commit messages follow Conventional Commits format
- [ ] No long-lived branches (> 3 days)
- [ ] Pre-commit hooks in place

## References

- [ci-cd-pipelines skill](../ci-cd-pipelines/SKILL.md)
- [Conventional Commits](https://www.conventionalcommits.org/)
