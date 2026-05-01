<div align="center">

<img src="https://raw.githubusercontent.com/DevelopersGlobal/ai-agent-skills/main/docs/assets/banner.svg" alt="AI Agent Skills" width="100%"/>

# 🤖 AI Agent Skills

### *Production-grade AI agent skills for real-world applications — and everyday use*

[![GitHub Stars](https://img.shields.io/github/stars/DevelopersGlobal/ai-agent-skills?style=for-the-badge&logo=github&color=FFD700)](https://github.com/DevelopersGlobal/ai-agent-skills/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/DevelopersGlobal/ai-agent-skills?style=for-the-badge&logo=github&color=00BFFF)](https://github.com/DevelopersGlobal/ai-agent-skills/network)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)
[![GitHub Pages](https://img.shields.io/badge/Docs-GitHub_Pages-blue?style=for-the-badge&logo=github)](https://developersglobal.github.io/ai-agent-skills)

> **Inspired by [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) and [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)**

**🌐 [View the Interactive Skills Browser →](https://developersglobal.github.io/ai-agent-skills)**

</div>

---

## 🎯 What is this?

AI agents are only as good as the instructions they follow. **AI Agent Skills** is a curated, battle-tested library of skill files — structured markdown prompts — that transform AI coding agents (Claude, Gemini, Cursor, Copilot, etc.) into disciplined, production-ready engineers.

Unlike generic prompts, these skills encode **actual workflows** with steps, checkpoints, verification gates, and anti-pattern guards — the same discipline senior engineers bring to every production deployment.

```
THINK → PLAN → BUILD → TEST → REVIEW → HARDEN → SHIP
  ↓        ↓      ↓       ↓       ↓        ↓        ↓
Clarify  Break  Write  Verify  Quality  Security  Deploy
Goals    Down   Code   Output  Gates    Gates     Live
```

---

## 🏆 Why This Repo Goes Beyond the Rest

| Feature | This Repo | agent-skills | karpathy-skills |
|--------|-----------|--------------|-----------------|
| Production + Everyday use | ✅ | Production only | General |
| Multi-agent orchestration | ✅ | ❌ | ❌ |
| AI safety & hallucination guards | ✅ | ❌ | Partial |
| RAG / Memory skills | ✅ | ❌ | ❌ |
| Prompt injection defense | ✅ | ❌ | ❌ |
| GitHub Pages search UI | ✅ | ❌ | ❌ |
| 30+ curated skills | ✅ | 20 skills | 4 principles |
| Everyday productivity skills | ✅ | ❌ | ❌ |

---

## ⚡ Quick Start

### Claude Code
```bash
/plugin marketplace add DevelopersGlobal/ai-agent-skills
/plugin install ai-agent-skills@developers-global
```

### Cursor
Copy any `SKILL.md` into `.cursor/rules/`

### Gemini CLI
```bash
gemini skills install https://github.com/DevelopersGlobal/ai-agent-skills.git --path skills
```

### Any Agent (Universal)
```bash
# Copy a skill and paste into your agent's system prompt / context window
curl https://raw.githubusercontent.com/DevelopersGlobal/ai-agent-skills/main/skills/production-deployment/SKILL.md
```

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

---

## 🏛️ Skill Anatomy

Every skill follows the same battle-tested structure:

```
┌─────────────────────────────────────────────────────┐
│ SKILL.md                                            │
│                                                     │
│  ┌─ Frontmatter ────────────────────────────────┐  │
│  │  name:        kebab-case-name                │  │
│  │  description: One-line trigger description   │  │
│  │  applies-to:  [claude, gemini, cursor, ...]  │  │
│  │  category:    think|plan|build|test|...      │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  Overview      → What this skill accomplishes       │
│  When to Use   → Exact triggering conditions        │
│  Process       → Numbered, verifiable steps         │
│  Rationalizations → Common excuses + rebuttals      │
│  Red Flags     → Warning signs the skill is needed  │
│  Verification  → Non-negotiable evidence required   │
│  References    → Supporting checklists/docs         │
└─────────────────────────────────────────────────────┘
```

---

## 🤝 Contributing

We welcome contributions! The best skills are:
- **Specific** — Actionable steps, not vague principles
- **Verifiable** — Clear exit criteria with evidence
- **Battle-tested** — Based on real production experience
- **Minimal** — Only what the agent needs; no bloat

See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/skill-anatomy.md](docs/skill-anatomy.md).

---

## 🌐 GitHub Pages

The full skills library is browsable at **[developersglobal.github.io/ai-agent-skills](https://developersglobal.github.io/ai-agent-skills)** with:
- 🔍 Full-text search across all skills
- 🏷️ Filter by category and agent type
- 📋 One-click copy for any skill
- 📱 Mobile-friendly responsive design

---

## 📊 Inspiration & Credits

This project builds on and extends the ideas from:
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — Production engineering skills for AI agents
- [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) — Karpathy's observations on LLM coding pitfalls
- [DevelopersGlobal](https://github.com/DevelopersGlobal) — Community-driven developer tools

---

## 📄 License

MIT — Use these skills in your projects, teams, and tools. Attribution appreciated but not required.

---

<div align="center">

**⭐ Star this repo to help developers everywhere build better AI agents ⭐**

Made with ❤️ by [DevelopersGlobal](https://github.com/DevelopersGlobal)

</div>
