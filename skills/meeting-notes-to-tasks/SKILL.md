---
name: meeting-notes-to-tasks
description: Converts unstructured meeting notes into structured, assigned, time-bounded action items. Never leave a meeting without knowing who does what by when.
category: everyday
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Meetings produce decisions and commitments. Without structure, these dissolve into vague memory. This skill transforms raw meeting notes into a concrete, actionable task list.

## When to Use

- After any meeting with decisions or commitments
- When processing meeting transcripts or notes
- When preparing follow-up communication

## Process

### Step 1: Extract Decisions

1. Read all notes.
2. List every **decision made**: `Decision: [what was decided]`
3. Distinguish decisions from discussions (decisions = agreed outcomes, not explorations).

**Deliver:** A numbered list of decisions made.

### Step 2: Extract Action Items

4. For each commitment made, write:
   ```
   Action: [specific deliverable]
   Owner: [person's name]
   Due: [specific date, not "soon" or "next week"]
   Context: [1-sentence background]
   ```
5. If an owner is not named: flag it — unowned actions are undone actions.
6. If a due date is not named: flag it — undated actions are undone actions.

**Deliver:** Structured action items with owner and due date for every commitment.

### Step 3: Identify Blockers and Dependencies

7. What action items are blocked by other action items?
8. What external dependencies exist (waiting on third party, requires approval, etc.)?
9. What open questions remain unresolved?

**Deliver:** Blocker list and open questions with owners.

### Step 4: Draft Follow-Up Summary

10. Compose a concise follow-up message:
    - Decisions (bullet list)
    - Action items (table: action | owner | due date)
    - Open questions (bullet list with owner)
    - Next meeting date (if applicable)

**Deliver:** Ready-to-send follow-up email/Slack message.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "Everyone knows what they need to do" | They don't. Write it down. |
| "The notes are good enough" | Notes describe what was said. Action items describe what will be done. |
| "We'll follow up informally" | Informal follow-up means things fall through the cracks. |

## Verification

- [ ] Every decision captured
- [ ] Every action item has: owner, due date, specific deliverable
- [ ] Unowned/undated items flagged
- [ ] Blockers and open questions identified
- [ ] Follow-up summary drafted and ready to send

## References

- [goal-driven-execution skill](../goal-driven-execution/SKILL.md)
