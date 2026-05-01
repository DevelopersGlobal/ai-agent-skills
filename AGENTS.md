# AI Agent Instructions for This Repository

This repository contains AI agent skills — structured markdown skill files for production-grade AI-assisted development.

## When Working in This Repository

- **Reading skills**: Skills are in `skills/<name>/SKILL.md`. Read the full SKILL.md before making any edits.
- **Adding skills**: Follow the template in `docs/skill-template.md` exactly. Every section is required.
- **Editing skills**: Only edit the skill you're asked to change. Don't refactor adjacent skills.
- **Testing skills**: Test by applying the skill to a real agent session and verifying the output quality.

## Repository Structure

```
skills/          ← All 30 skill files (SKILL.md per directory)
agents/          ← Specialist agent persona definitions
references/      ← Supporting checklists (security, performance, etc.)
docs/            ← Setup guides, skill anatomy, template
.claude/         ← Claude Code slash commands
.gemini/         ← Gemini CLI commands
.github/         ← GitHub Actions workflows
docs/            ← GitHub Pages site (index.html)
```

## Key Principles

1. Skills are **workflows**, not prose — agents follow steps, not skim docs
2. Every step has a **verification gate** — "seems right" is never sufficient  
3. Skills include **anti-rationalization tables** — common excuses + rebuttals
4. Skills are **minimal** — only what's needed to guide the agent through the task

## When Adding a New Skill

1. Create directory `skills/<kebab-name>/`
2. Create `SKILL.md` using the template from `docs/skill-template.md`
3. Add to `skills/index.json` for the GitHub Pages search to pick it up
4. Update `README.md` skills table

## Validation

Before a skill is merged:
- [ ] Applied to at least one real agent session
- [ ] All sections filled (no "TODO" or empty sections)
- [ ] Verification criteria are concrete (not "make sure it works")
- [ ] Anti-rationalization table has at least 3 entries
- [ ] Added to `skills/index.json`
