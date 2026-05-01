<div align="center">


# 🤖 AI Agent Skills

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

### Step 1 — Clone the repo
```bash
git clone https://github.com/DevelopersGlobal/ai-agent-skills.git
```

### Step 2 — Pick a skill and copy it into your agent

**Claude / Cursor / Copilot / any agent:**
Copy the contents of any `SKILL.md` file into your agent's system prompt, instructions file, or context window.

**For Claude Code** — add to your project's `CLAUDE.md`:
```bash
cat skills/think-before-coding/SKILL.md >> CLAUDE.md
```

**For Cursor** — copy into `.cursor/rules/`:
```bash
cp skills/security-hardening/SKILL.md .cursor/rules/security-hardening.mdc
```

**For Gemini CLI** — add to your project's `GEMINI.md`:
```bash
cat skills/goal-driven-execution/SKILL.md >> GEMINI.md
```

**One-liner (any skill, any agent):**
```bash
# View raw skill content, then paste into your agent
curl https://raw.githubusercontent.com/DevelopersGlobal/ai-agent-skills/main/skills/production-deployment/SKILL.md
```

> **Browse and copy skills visually →** [developersglobal.github.io/ai-agent-skills](https://developersglobal.github.io/ai-agent-skills)

---

## 📚 All 30 Skills

### 🧠 Think — Before You Code
| Skill | Description |
|-------|-------------|
| [think-before-coding](skills/think-before-coding/SKILL.md) | Surface assumptions, manage confusion, prevent hallucination |
| [goal-driven-execution](skills/goal-driven-execution/SKILL.md) | Transform tasks into verifiable goals with success criteria |
| [idea-to-spec](skills/idea-to-spec/SKILL.md) | Convert vague ideas into concrete, testable specifications |

### 📐 Plan — Break It Down
| Skill | Description |
|-------|-------------|
| [task-decomposition](skills/task-decomposition/SKILL.md) | Break features into atomic, independently verifiable tasks |
| [context-loading](skills/context-loading/SKILL.md) | Load minimum necessary context; avoid token bloat |
| [multi-agent-orchestration](skills/multi-agent-orchestration/SKILL.md) | Design and coordinate multi-agent pipelines |

### 🏗️ Build — Write Production Code
| Skill | Description |
|-------|-------------|
| [incremental-coding](skills/incremental-coding/SKILL.md) | Build in verifiable increments; never big-bang rewrites |
| [simplicity-first](skills/simplicity-first/SKILL.md) | Minimum code that solves the problem — nothing speculative |
| [surgical-changes](skills/surgical-changes/SKILL.md) | Touch only what you must; leave the rest untouched |
| [api-design](skills/api-design/SKILL.md) | Design stable, versioned, self-documenting APIs |
| [frontend-engineering](skills/frontend-engineering/SKILL.md) | Accessible, performant, responsive UI patterns |
| [rag-and-memory](skills/rag-and-memory/SKILL.md) | Retrieval-Augmented Generation and agent memory patterns |

### ✅ Test — Prove It Works
| Skill | Description |
|-------|-------------|
| [test-driven-development](skills/test-driven-development/SKILL.md) | Red-green-refactor with meaningful coverage |
| [debugging-methodology](skills/debugging-methodology/SKILL.md) | Systematic root cause analysis; never guess-and-check |
| [integration-testing](skills/integration-testing/SKILL.md) | Test real system boundaries, not mocks of mocks |
| [ai-output-validation](skills/ai-output-validation/SKILL.md) | Validate, parse, and sanitize AI-generated outputs |

### 🔍 Review — Quality Gates
| Skill | Description |
|-------|-------------|
| [code-review](skills/code-review/SKILL.md) | Structured review checklist; correctness over style |
| [performance-optimization](skills/performance-optimization/SKILL.md) | Measure first, optimize second; no premature optimization |
| [refactoring](skills/refactoring/SKILL.md) | Safe, behavior-preserving transformation with tests |
| [documentation](skills/documentation/SKILL.md) | Document decisions, not just implementations |

### 🔒 Harden — Security & Reliability
| Skill | Description |
|-------|-------------|
| [security-hardening](skills/security-hardening/SKILL.md) | OWASP Top 10, secrets management, least privilege |
| [prompt-injection-defense](skills/prompt-injection-defense/SKILL.md) | Guard AI agents against prompt injection attacks |
| [hallucination-prevention](skills/hallucination-prevention/SKILL.md) | Detect and mitigate LLM hallucinations in pipelines |
| [error-handling](skills/error-handling/SKILL.md) | Graceful degradation and meaningful error messages |
| [observability](skills/observability/SKILL.md) | Structured logging, tracing, and alerting for AI systems |

### 🚀 Ship — Deploy with Confidence
| Skill | Description |
|-------|-------------|
| [production-deployment](skills/production-deployment/SKILL.md) | Zero-downtime deploys with rollback plans |
| [ci-cd-pipelines](skills/ci-cd-pipelines/SKILL.md) | Automated quality gates from commit to production |
| [git-workflow](skills/git-workflow/SKILL.md) | Trunk-based development, atomic commits, clean history |

### 🌟 Everyday — Productivity Skills
| Skill | Description |
|-------|-------------|
| [code-explanation](skills/code-explanation/SKILL.md) | Get clear, layered explanations of unfamiliar code |
| [meeting-notes-to-tasks](skills/meeting-notes-to-tasks/SKILL.md) | Convert meeting notes into structured action items |
| [research-and-summarize](skills/research-and-summarize/SKILL.md) | Distill complex topics into actionable summaries |

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
