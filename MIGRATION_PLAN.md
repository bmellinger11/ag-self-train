# Antigravity IDE: Curriculum Migration Plan

This document details the architectural and pedagogical migration of the `cc-self-train` curriculum (originally built for Claude Code by Zain Naboulsi) to `ag-self-train`, an equivalent training tool fitted natively to the Antigravity IDE capabilities.

## 1. Pedagogical Architecture Migration
Zain's paper outlines five core pedagogical design patterns. We have mapped each pattern to an Antigravity-native implementation:

| Pedagogical Feature | Claude Code Implementation | Antigravity IDE Implementation |
|---------------------|----------------------------|--------------------------------|
| **Persona Progression** | Static prompts in `CLAUDE.md` and module-specific frontmatter. | The master Orchestrator Skill (`.agents/skills/ag-self-train/SKILL.md`) dynamically injects the Persona (Guide -> Collaborator -> Peer -> Launcher) based on the state in `learner_profile.json`. |
| **Adaptive Learning** | `SessionStart` / `Stop` hooks parsing the terminal interaction. | A Python daemon (`scripts/observe_interaction.py`) that parses the Antigravity `transcript.jsonl` log, tracks engagement quality, and updates the learner's effective level. |
| **Unified Curriculum** | 5 project types (Canvas, Forge, Nexus, Sentinel, BYOP) sharing 10 module sequences. | **Preserved:** We retain the 5 cross-domain project structures, ensuring that learning is focused on the IDE capabilities rather than the project logic. |
| **Step-Pacing** | `**STOP**` blocks enforced by LLM prompt adherence. | The native `ask_question` tool forces a hard UI pause (e.g. "Have you completed Step 1?") to enforce information load management. |
| **Auto-Updating** | A `/sync` skill triggered at `/start` that fetches the changelog and injects updates. | An `auto-updater` Skill utilizing Antigravity's agentic tools to fetch the IDE changelog, research features, and use `replace_file_content` to append new steps. Can be automated via the `/schedule` slash command. |

## 2. Feature Coverage Parity
The core of the curriculum involves 10 modules that progressively teach advanced IDE capabilities. This matrix outlines how Claude Code features are mapped to equivalent Antigravity capabilities:

| Module | Claude Code Feature | Antigravity IDE Equivalent Capability |
|--------|---------------------|---------------------------------------|
| 1. **Setup & First Contact** | `CLAUDE.md`, `/init`, `/memory`, terminal UI | **Workspace Customization Roots** (`.agents/`), `learner_profile.json`, Agent Chat UI, and generating basic Artifacts. |
| 2. **Blueprint & Build** | Plan mode, git integration | **Planning Mode**, `implementation_plan.md`, `task.md` checklists, and `walkthrough.md` summaries. |
| 3. **Rules & Context** | `.claude/rules/`, `CLAUDE.local.md`, `@imports` | Global & Project-scoped rules in `AGENTS.md`, and the **Knowledge Items (KIs)** System. |
| 4. **Skills & Commands** | `SKILL.md`, slash commands | Custom Skills in `skills/<skill_name>/SKILL.md`, and Native Slash Commands (`/goal`, `/schedule`, `/grill-me`, `/learn`). |
| 5. **Hooks & Observation** | `SessionStart`, `PostToolUse`, `Stop` hooks | Python observation daemons (e.g., `observe_interaction.py`), Background Tasks via `/schedule`. |
| 6. **MCP Servers** | MCP integration, `.mcp.json` | **Plugins** (`plugin.json`), grouping skills and agents together. |
| 7. **Guard Rails** | `PreToolUse` decision control | System-injected `<user_rules>` in `AGENTS.md` specifying mandatory constraints. |
| 8. **Subagents** | `.claude/agents/`, chaining, background | `invoke_subagent` and `browser_subagent` for multi-agent workflows. |
| 9. **Tasks & TDD** | Tasks system, cross-session persistence | Background Tasks (`manage_task`), `task.md` checklists. |
| 10. **Parallel Dev & Eval**| Worktrees, Agent Teams, plugins, eval | Concurrent subagent orchestration, advanced artifact generation (Carousels, Mermaid, Markdown tables). |

## 3. README Coverage Parity
To ensure that the `ag-self-train` repository provides equivalent guidance to the original, the `README.md` will maintain the exact structural outline of the `cc-self-train` README, adapted for Antigravity:

- **TL;DR:** Introduce the Antigravity IDE training environment.
- **Prerequisites:** Basic knowledge of the IDE layout and terminal basics.
- **Quick Start:** Clone the repo, let the `.agents` load, and type `learn-ide` to start.
- **Who This Is For:** Explain that this teaches Antigravity capabilities through hands-on project creation.
- **The 5 Options:** Detail the Canvas, Forge, Nexus, Sentinel, and BYOP options.
- **The 10 Modules:** Present the modified Feature Coverage Matrix (from Section 2 above).
- **Reference Docs:** Link to the official Antigravity docs (`https://antigravity.google/docs/home`).
- **Design Principles & Always Current:** Explain the Antigravity-native auto-updater skill and pacing primitives.
- **Acknowledgements:** Preserve the original attributions to Zain Naboulsi and the research paper.
