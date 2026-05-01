# Contributing to AI Agent Skills

Thank you for helping make AI agents better for everyone! 🎉

## What Makes a Great Skill?

A great skill is:

1. **Specific** — Not "write good code" but "here are the 5 concrete steps to review a PR"
2. **Verifiable** — Every step has a clear check: "Run tests. All green? Proceed."
3. **Battle-tested** — Based on real experience, not theory
4. **Minimal** — Only what the agent needs to follow the workflow. No bloat.
5. **Anti-rationalization** — Includes a table of excuses agents use to skip steps + rebuttals

## Skill Categories

| Category | When to Add Here |
|----------|-----------------|
| `think` | Before writing a single line of code |
| `plan` | Breaking work into tasks |
| `build` | Writing the actual implementation |
| `test` | Verifying correctness |
| `review` | Quality gates before merge |
| `harden` | Security, reliability, observability |
| `ship` | Deployment and release |
| `everyday` | Productivity for non-coding tasks |

## How to Submit a Skill

### 1. Fork and Clone

```bash
git clone https://github.com/DevelopersGlobal/ai-agent-skills.git
cd ai-agent-skills
```

### 2. Create Your Skill Directory

```bash
mkdir -p skills/your-skill-name
touch skills/your-skill-name/SKILL.md
```

### 3. Follow the Template

Copy from [docs/skill-template.md](docs/skill-template.md) and fill in every section. **Do not leave any section empty.**

### 4. Test Your Skill

Before submitting, test your skill by actually giving it to an AI agent and verifying it produces better results than without it. Document your test case.

### 5. Open a Pull Request

- Title: `feat(skills): add [skill-name] skill`
- Description: What problem does this skill solve? What was your test case?
- Link to any relevant discussions or issues

## Skill Template Quick Reference

```yaml
---
name: your-skill-name
description: One sentence: "Guides agents to [do X] when [condition Y]."
category: think|plan|build|test|review|harden|ship|everyday
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview
...

## When to Use
...

## Process
1. Step one — **verify:** [how to check]
2. Step two — **verify:** [how to check]
...

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "I'll do it later" | Later never comes. Do it now. |

## Red Flags
- [Warning sign that this skill is needed but not being followed]

## Verification
- [ ] Evidence item 1
- [ ] Evidence item 2

## References
- [Link to supporting material]
```

## Code of Conduct

- Be respectful and constructive
- Focus on quality over quantity
- If you see a skill that can be improved, open an issue or PR

## Questions?

Open an issue or start a discussion in the [GitHub Discussions](https://github.com/DevelopersGlobal/ai-agent-skills/discussions) tab.
