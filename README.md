<div align="center">

# 🧠 Claude Skills

### Ready-to-use skill files that transform Claude into specialized AI agents.

**No prompt engineering required. Just copy → paste → go.**

[![GitHub Stars](https://img.shields.io/github/stars/DhanushNehru/claude-skills?style=for-the-badge&logo=github&color=yellow)](https://github.com/DhanushNehru/claude-skills/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)
[![Skills](https://img.shields.io/badge/Skills-25+-purple?style=for-the-badge)](#-skill-catalog)

<br/>

> **Think of these as plugins for your brain's AI copilot.**
> Each skill is a self-contained instruction set — battle-tested, community-reviewed, and ready for production use.

<br/>

[Get Started](#-quick-start) · [Browse Skills](#-skill-catalog) · [Create a Skill](#-create-your-own) · [Contribute](#-contributing)

</div>

---

## 🤔 What Are Claude Skills?

A **Claude Skill** is a portable, copy-paste-ready instruction file that gives Claude a specialized capability. Unlike generic prompt collections, each skill is:

| Feature | Description |
|---|---|
| 🎯 **Purpose-built** | Designed for a specific real-world task, not a toy demo |
| 📋 **Structured** | Uses the proven `Role → Goal → Constraints → Output` contract format |
| 🧪 **Tested** | Every skill includes example inputs/outputs so you know what to expect |
| 🔌 **Plug-and-play** | Works with Claude.ai, Claude API, Claude Code (`CLAUDE.md`), and any Claude-powered tool |
| 🏷️ **Tagged** | Difficulty level, estimated token usage, and compatibility info included |

---

## ⚡ Quick Start

### Method 1: Claude.ai (Recommended for beginners)
1. Browse the [Skill Catalog](#-skill-catalog) below
2. Open the skill file (e.g., `skills/developer/code-reviewer.md`)
3. Copy the content inside the `<system_prompt>` tags
4. Paste it into **Claude.ai → Project Knowledge** or **Custom Instructions**
5. Start chatting — Claude now has that skill!

### Method 2: Claude Code (`CLAUDE.md`)
1. Copy the skill file to your project root as `CLAUDE.md` (or append to an existing one)
2. Run `claude` in your terminal — it auto-reads the file
3. Claude Code now operates with that specialized skill

### Method 3: API / SDK
```python
import anthropic

# Load the skill
with open("skills/developer/code-reviewer.md") as f:
    skill = f.read()

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    system=skill,  # ← The skill becomes the system prompt
    messages=[{"role": "user", "content": "Review this pull request: ..."}]
)
```

---

## 📚 Skill Catalog

### 🛠️ Developer Skills
| Skill | Description | Difficulty |
|-------|-------------|:----------:|
| [Code Reviewer](skills/developer/code-reviewer.md) | Production-grade code review with security, performance & maintainability analysis | ⭐⭐ |
| [Git Commit Crafter](skills/developer/git-commit-crafter.md) | Generate perfect conventional commits from diffs | ⭐ |
| [Bug Hunter](skills/developer/bug-hunter.md) | Systematic debugging agent that traces root causes | ⭐⭐⭐ |
| [API Designer](skills/developer/api-designer.md) | Design RESTful APIs following OpenAPI best practices | ⭐⭐ |
| [Regex Wizard](skills/developer/regex-wizard.md) | Build, explain, and test regular expressions in any flavor | ⭐ |

### 🔒 Security Skills
| Skill | Description | Difficulty |
|-------|-------------|:----------:|
| [Threat Modeler](skills/security/threat-modeler.md) | STRIDE-based threat modeling for any system architecture | ⭐⭐⭐ |
| [Dependency Auditor](skills/security/dependency-auditor.md) | Deep-dive analysis of package vulnerabilities and supply chain risks | ⭐⭐ |
| [Security Headers Checker](skills/security/security-headers-checker.md) | Analyze and fix HTTP security headers for web applications | ⭐ |

### 📊 Data & Analysis Skills
| Skill | Description | Difficulty |
|-------|-------------|:----------:|
| [SQL Query Optimizer](skills/data/sql-query-optimizer.md) | Analyze and optimize slow SQL queries with execution plan analysis | ⭐⭐ |
| [Data Storyteller](skills/data/data-storyteller.md) | Transform raw datasets into compelling narratives with visualizations | ⭐⭐ |
| [CSV Detective](skills/data/csv-detective.md) | Profile, clean, and analyze messy CSV/JSON datasets | ⭐ |

### ✍️ Writing & Content Skills
| Skill | Description | Difficulty |
|-------|-------------|:----------:|
| [Technical Writer](skills/writing/technical-writer.md) | Write clear, structured technical documentation and ADRs | ⭐⭐ |
| [README Generator](skills/writing/readme-generator.md) | Generate stunning, complete README files from codebases | ⭐ |
| [Changelog Author](skills/writing/changelog-author.md) | Generate human-readable changelogs from git history | ⭐ |

### 🏗️ Architecture & DevOps Skills
| Skill | Description | Difficulty |
|-------|-------------|:----------:|
| [System Design Coach](skills/architecture/system-design-coach.md) | Interactive system design interview prep and architecture review | ⭐⭐⭐ |
| [Dockerfile Optimizer](skills/devops/dockerfile-optimizer.md) | Analyze and optimize Dockerfiles for size, security, and build speed | ⭐⭐ |
| [CI/CD Pipeline Builder](skills/devops/cicd-pipeline-builder.md) | Generate production-ready GitHub Actions / GitLab CI pipelines | ⭐⭐ |

### 🧩 Productivity Skills
| Skill | Description | Difficulty |
|-------|-------------|:----------:|
| [Meeting Summarizer](skills/productivity/meeting-summarizer.md) | Extract action items, decisions, and key points from meeting transcripts | ⭐ |
| [Email Diplomat](skills/productivity/email-diplomat.md) | Craft professional emails for sensitive situations | ⭐ |
| [Learning Path Generator](skills/productivity/learning-path-generator.md) | Create personalized, structured learning roadmaps for any topic | ⭐⭐ |

### 🎨 Creative Skills
| Skill | Description | Difficulty |
|-------|-------------|:----------:|
| [Color Palette Generator](skills/creative/color-palette-generator.md) | Generate accessible, harmonious color palettes from any inspiration | ⭐ |
| [Naming Consultant](skills/creative/naming-consultant.md) | Generate memorable names for projects, products, and companies | ⭐ |

---

## 🧬 Skill Anatomy

Every skill follows a consistent structure:

```
skills/
├── developer/
│   └── code-reviewer.md        ← The skill file
├── security/
│   └── threat-modeler.md
└── ...
```

Each skill file contains:
```markdown
# 🔍 Skill Name
> One-line description

## Metadata
- **Category**: Developer | Security | Data | Writing | DevOps | Productivity | Creative
- **Difficulty**: ⭐ | ⭐⭐ | ⭐⭐⭐
- **Works With**: Claude.ai, Claude Code, API
- **Estimated Tokens**: ~500 system prompt tokens

## System Prompt
<system_prompt>
  ... the actual instruction set ...
</system_prompt>

## Example Usage
**User**: [example input]
**Claude**: [example output]

## Tips & Variations
- Modification ideas for different use cases
```

---

## 🔨 Create Your Own

Use our [Skill Template](SKILL_TEMPLATE.md) to create your own skill:

1. Fork this repo
2. Copy `SKILL_TEMPLATE.md` into the appropriate `skills/<category>/` folder
3. Fill in your skill following the template structure
4. Test it thoroughly (include real example I/O)
5. Submit a PR!

**Pro tips:**
- Use XML tags (`<context>`, `<constraints>`, `<output_format>`) for complex instructions
- Keep system prompts under 1000 tokens for optimal performance
- Include at least 2 example interactions
- Add edge cases in your "Tips & Variations" section

---

## 🤝 Contributing

We love contributions! Whether it's a new skill, an improvement to an existing one, or fixing a typo — every PR is welcome.

Please read our [Contributing Guide](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before submitting.

### What makes a great skill?
- ✅ Solves a **real problem** people encounter regularly
- ✅ Includes **tested examples** with realistic inputs/outputs
- ✅ Is **self-contained** — no external dependencies or setup
- ✅ Has a **clear, specific scope** — does one thing extremely well
- ✅ Uses **structured formatting** (XML tags, markdown) for reliability

---

## 🌟 Star History

If this repo helped you, please consider giving it a ⭐ — it helps others discover these skills!

[![Star History Chart](https://api.star-history.com/svg?repos=DhanushNehru/claude-skills&type=Date)](https://star-history.com/#DhanushNehru/claude-skills&Date)

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with 🧠 by the community, for the community.**

[⬆ Back to Top](#-claude-skills)

</div>
