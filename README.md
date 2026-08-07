# Agentic Education:<br>Using Antigravity IDE to Teach Antigravity IDE

[![v0.1.0-mvp](https://img.shields.io/badge/version-0.1.0--mvp-blue)](#)

## TL;DR

Learn [Antigravity IDE](https://antigravity.google/docs/home) by building a real project. Pick from 5 project types, work through 10 hands-on modules, and go from "what is this?" to "I can build anything with this." No prior experience with AI coding tools needed — the curriculum adapts to your level and walks you through one step at a time.

> **First time hearing of Antigravity IDE?** It's a powerful agentic AI coding assistant environment. You describe in plain English what you want to build, and the Antigravity Agent writes the code, creates rich artifacts, and runs commands. Think of it as a very skilled coding partner that lives natively in your workspace.

<details>
<summary>Under the hood: the research behind this curriculum</summary>

This repository is an architectural adaptation of the **cc-self-train** framework (originally for Claude Code) built to natively leverage Antigravity IDE capabilities. It preserves the five pedagogical research contributions: (1) a **persona progression model**, (2) an **adaptive learning system** powered by Python daemons observing your transcript, (3) a **cross-domain unified curriculum**, (4) a **step-pacing mechanism** utilizing conversational turn-taking, and (5) an **auto-updating curriculum design** powered by Antigravity Skills. See [MIGRATION_PLAN.md](MIGRATION_PLAN.md) for full architectural details.

</details>

## Prerequisites

You should be comfortable with:
- **Opening a terminal** and basic commands (`cd`, `ls`, `mkdir`)
- **Basic Git** (`git add`, `git commit`)
- **The Antigravity Chat UI** (how to talk to the agent)

## Quick Start

**Time to first working feature:** ~90 minutes (Module 2). **Full curriculum:** ~10-15 hours across 10 modules. 

1. **Clone this repo into your workspace:**
   ```bash
   git clone https://github.com/bmellinger11/ag-self-train.git
   cd ag-self-train
   ```
2. **Open the repository in Antigravity IDE.**
   The `.agents` configuration folder will load automatically, registering the curriculum orchestrator.
3. **Type `learn-ide`** (without a slash) or "start the learning modules" in the chat to begin.

That's it. The agent will walk you through picking a project and scaffolding everything. 

## Who This Is For

You've installed Antigravity IDE and want to know how to use it optimally. Pick one of 5 tutorial projects and work through 10 progressive modules that take you from "first session" to "multi-agent orchestration." By the end, you won't just know what these features do — you'll have used every one of them to build something you're proud of.

## The 5 Options

- **Canvas — Personal Portfolio Site** ⭐ Recommended for first-timers
- **Forge — Personal Dev Toolkit**
- **Nexus — Local API Gateway**
- **Sentinel — Code Analyzer & Test Generator**
- **Bring Your Own Project (BYOP)**

*All options teach the exact same 10 IDE capabilities. Pick based on interest.*

## The 10 Modules

| # | Module | Antigravity IDE Features Taught |
|---|--------|---------------------------------|
| 1 | **Setup & First Contact** | Workspace Customization Roots (`.agents/`), `learner_profile.json`, Agent Chat UI, basic Artifacts |
| 2 | **Blueprint & Build** | **Planning Mode**, `implementation_plan.md`, `task.md` checklists, `walkthrough.md` |
| 3 | **Rules & Context** | Global & Project-scoped rules in `AGENTS.md`, Knowledge Items (KIs) System |
| 4 | **Skills & Commands** | Custom Skills in `SKILL.md`, Native Slash Commands (`/goal`, `/schedule`, `/grill-me`, `/learn`) |
| 5 | **Hooks & Observation** | Python observation daemons (`observe_interaction.py`), Background Tasks via `/schedule` |
| 6 | **MCP Servers** | **Plugins** (`plugin.json`, grouping skills and agents) |
| 7 | **Guard Rails** | System-injected `<user_rules>` in `AGENTS.md` specifying mandatory constraints |
| 8 | **Subagents** | `invoke_subagent` and `browser_subagent` for multi-agent workflows |
| 9 | **Tasks & TDD** | Background Tasks (`manage_task`), automated testing with checklist artifacts |
| 10 | **Parallel Dev & Eval**| Concurrent subagent orchestration, advanced artifact generation (Carousels, Mermaid) |

## Companion Resources

- [Official Antigravity Docs](https://antigravity.google/docs/home) — The definitive reference for Antigravity IDE features.
- [MIGRATION_PLAN.md](MIGRATION_PLAN.md) — Detailed mapping between Claude Code capabilities and Antigravity features.

## Always Current

You don't need to worry about the curriculum going stale. The `auto-updater` Skill (triggered on startup if a version mismatch is detected) uses Antigravity's agentic tools to fetch the IDE changelog, research features, and safely append new steps to your curriculum. You can also run it as a background cron job using `/schedule`.

## Acknowledgements
This project is an adaptation of the `cc-self-train` architecture.
- **Original Author**: Zain Naboulsi
- **Paper**: [Agentic Education: Using Claude Code to Teach Claude Code](https://arxiv.org/pdf/2604.17460)
- **Original Repository**: [zainnab-sparq/cc-self-train](https://github.com/zainnab-sparq/cc-self-train)
