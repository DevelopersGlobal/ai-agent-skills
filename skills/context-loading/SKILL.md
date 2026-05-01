---
name: context-loading
description: Load minimum necessary context into agent context windows. Prevents token bloat, reduces cost, and improves focus. Only load what the current task needs.
category: plan
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

More context is not better context. Irrelevant context dilutes attention, increases cost, and slows inference. This skill enforces disciplined context loading: only the files, docs, and history that the current task requires.

## When to Use

- Before starting any complex agent task
- When designing system prompts for production agents
- When context windows are filling up

## Process

### Step 1: Identify Required Context

1. List the files/docs the agent needs to read to complete THIS specific task.
2. For each item, ask: *"Can the agent complete the task without this?"* If yes, don't include it.
3. Prioritize: system prompt → task definition → directly relevant code → supporting references.

**Verify:** Every item in context is directly necessary for the current task.

### Step 2: Summarize, Don't Dump

4. Long conversation history → summarize to key decisions and current state.
5. Large files → extract only the relevant functions/sections.
6. Entire docs → extract only the relevant sections.
7. Previous agent output → extract only the conclusions and next steps.

**Verify:** No item in context exceeds what's needed from that source.

### Step 3: Set Context Budgets

8. Define token allocation for each context section:
   - System prompt: ≤ 2,000 tokens
   - Task definition: ≤ 500 tokens
   - Code context: ≤ 4,000 tokens
   - Conversation history (summarized): ≤ 1,000 tokens
9. Stay well within model context limits (leave 30% buffer for output).

**Verify:** Total prompt fits within 70% of model context limit.

### Step 4: Refresh Context for New Tasks

10. Don't carry over context from a completed task to a new task.
11. Start each distinct task with a fresh, minimal context.
12. Re-introduce only what the new task genuinely needs.

## Verification

- [ ] Context items limited to task-required items only
- [ ] Long content summarized before inclusion
- [ ] Token budget defined and respected
- [ ] Context window at ≤70% capacity

## References

- [rag-and-memory skill](../rag-and-memory/SKILL.md)
- [multi-agent-orchestration skill](../multi-agent-orchestration/SKILL.md)
