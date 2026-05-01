# 🤝 Contributing to Claude Skills

First off, thank you for considering contributing to Claude Skills! Every skill you add helps thousands of developers work smarter with AI.

## 📋 Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Submitting a New Skill](#submitting-a-new-skill)
- [Quality Standards](#quality-standards)
- [Pull Request Process](#pull-request-process)
- [Style Guide](#style-guide)

## Ways to Contribute

| Contribution | Description |
|---|---|
| 🆕 **New Skill** | Create a brand new skill file |
| 🔧 **Improve Existing** | Enhance a skill's prompt, add examples, or fix edge cases |
| 📝 **Documentation** | Fix typos, improve explanations, or add translations |
| 🧪 **Testing** | Test skills and report results or issues |
| 💡 **Skill Ideas** | Open an issue with a skill idea for others to implement |

## Submitting a New Skill

### 1. Check for Duplicates
Search the [existing skills](README.md#-skill-catalog) to make sure your idea isn't already covered.

### 2. Use the Template
Copy the [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md) file and fill in all sections:

```bash
cp SKILL_TEMPLATE.md skills/<category>/your-skill-name.md
```

### 3. Choose the Right Category

| Category | Use When... |
|---|---|
| `developer/` | Code-related tasks (review, generation, debugging) |
| `security/` | Security analysis, vulnerability scanning, threat modeling |
| `data/` | Data analysis, SQL, visualization, dataset manipulation |
| `writing/` | Documentation, content creation, communication |
| `architecture/` | System design, patterns, scalability |
| `devops/` | CI/CD, containers, infrastructure, deployment |
| `productivity/` | Workflow optimization, communication, learning |
| `creative/` | Design, naming, brainstorming, ideation |

### 4. Test Your Skill
Before submitting, test your skill by:
- Pasting the system prompt into Claude.ai
- Running at least 3 different inputs (easy, medium, edge case)
- Verifying the output matches your documented examples

## Quality Standards

Every skill **must** have:

- [ ] A clear, one-line description
- [ ] Complete metadata (category, difficulty, compatibility, token estimate)
- [ ] A well-structured system prompt using XML tags
- [ ] At least 2 example interactions with realistic inputs/outputs
- [ ] Tips & Variations section with at least 2 modification ideas
- [ ] System prompt under 1500 tokens (check with [token counter](https://platform.anthropic.com/tokenizer))

Every skill **should** have:
- [ ] Edge cases documented
- [ ] Error handling instructions in the prompt
- [ ] Clear scope boundaries (what it does AND doesn't do)

## Pull Request Process

1. **Fork** the repository
2. **Create** a new branch: `git checkout -b skill/your-skill-name`
3. **Add** your skill file in the correct category folder
4. **Update** `README.md` to add your skill to the catalog table
5. **Commit** with a descriptive message: `feat: add sql-query-optimizer skill`
6. **Push** and open a Pull Request

### PR Description Template
```markdown
## New Skill: [Skill Name]

**Category**: [e.g., Developer]
**Difficulty**: [e.g., ⭐⭐]

### What does this skill do?
[Brief description]

### Why is it useful?
[Real-world use case]

### Testing done
- [ ] Tested on Claude.ai
- [ ] Tested with Claude Code
- [ ] Tested via API
- [ ] Included example I/O in skill file
```

## Style Guide

### File Naming
- Use **kebab-case**: `code-reviewer.md`, `threat-modeler.md`
- Be descriptive but concise
- No version numbers in filenames

### Prompt Writing
- Use **XML tags** for structure: `<role>`, `<goal>`, `<constraints>`, `<output_format>`
- Write in **second person**: "You are...", "Your task is..."
- Be **specific** over vague: "List exactly 3 issues" > "List some issues"
- Include **uncertainty handling**: Tell Claude what to do when unsure

### Markdown Formatting
- Use proper heading hierarchy (`#` → `##` → `###`)
- Include a table of contents for skills longer than 100 lines
- Use code blocks with language identifiers

---

Thank you for making Claude Skills better for everyone! 🧠✨
