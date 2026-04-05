# Cursor AI context: rules, skills, agents, and related files

This guide explains **how Cursor (and similar “AI pair programmer” setups) load instructions**, what each file type is for, and **how to combine them** without duplicating or fighting yourself. It uses this capstone repo as a concrete example where helpful.

---

## Mental model: three layers

Think of context in three layers:

| Layer | Typical question it answers | Load behavior (conceptually) |
|-------|------------------------------|------------------------------|
| **Always-on project policy** | “What must the agent obey in *this* repo every time?” | Injected or strongly prioritized for the workspace |
| **Scoped rules** | “What applies when I touch *these* files?” | Activated when matching paths are in play |
| **On-demand playbooks** | “How do we run *this* workflow well?” | Loaded when the task matches (discovery via description) |

**Rules** and **AGENTS.md** usually sit in the first two layers. **Skills** sit in the third.

**Two more levers (covered later):** **custom slash commands** (you explicitly run `/…`) and **subagents** (delegated or background agent work with its own context). They are not replacements for rules—they change *how* and *when* a workflow starts.

---

## 1. `AGENTS.md` (workspace root)

**What it is:** A project-level file (often at the **repository root**) that holds **standing instructions for the agent** for that workspace. Cursor treats it as persistent guidance for the whole project.

**Best for:**

- Commands that should run **before** declaring work done (e.g. `tabnanny`, `compileall`).
- Repo-wide conventions: commit message format, branch naming, “never commit secrets,” etc.
- Pointers to where deeper detail lives (rules, skills, README sections).

**Not ideal for:**

- Huge style guides (use a **skill** or **scoped rule** + link).
- Content that only applies to one file type (use a **globbed rule**).

**Example from this repo:** Root `AGENTS.md` tells the agent to run Python indentation checks under `churn-prediction/` and to use a structured commit message format, and it links to `.cursor/rules/` and the capstone skill.

**When to use:** When you want **“always remember this for this repo”** without tying it to a specific glob.

---

## 2. `.cursor/rules/*.mdc` (Cursor rules)

**What it is:** Markdown files with **YAML frontmatter** in `.cursor/rules/`. Each file is one **rule**: a focused policy or pattern.

**Frontmatter (typical):**

| Field | Role |
|--------|------|
| `description` | Human/agent-readable summary; helps in rule pickers and discovery |
| `globs` | Optional. If set, the rule is associated with matching files (e.g. `**/*.py`) |
| `alwaysApply` | If `true`, the rule applies to **every** chat/edit session in the project |

**Best for:**

- **Short, sharp** constraints: “use this error-handling shape,” “don’t edit these paths unless asked.”
- **File-type standards:** TypeScript only, notebooks only, etc.
- **One concern per file** so you can enable/disable mentally and avoid mega-prompts.

**Best practices (from Cursor’s own guidance):**

- Keep each rule **small** (on the order of tens of lines for the core idea; avoid multi-hundred-line blobs in every rule).
- Prefer **concrete examples** (good vs bad snippets).
- Split topics instead of one “god rule.”

**Pattern used in this repo:** `capstone-code-standards-py.mdc` applies to `**/*.py`, summarizes standards in a few bullets, and **links to** `.cursor/skills/capstone-code-standards/SKILL.md` for the full checklist. That avoids stuffing the rule with long prose.

**When to use:**

- **`alwaysApply: true`** — Truly universal project laws (use sparingly; noise adds up).
- **`globs: ...`** — Standards that apply when working in specific parts of the tree.

---

## 3. `.cursor/skills/<skill-name>/SKILL.md` (Agent skills)

**What it is:** A **skill** is a folder (e.g. `.cursor/skills/capstone-code-standards/`) whose main file is **`SKILL.md`**. The file has YAML frontmatter (`name`, `description`) and a body with procedures, checklists, templates, and optional links to `reference.md`, `examples.md`, or `scripts/`.

**How it differs from rules:**

- Skills are designed for **discovery**: the **`description`** tells the agent *what the skill does* and **when to use it** (trigger phrases, scenarios).
- They support **progressive disclosure**: keep `SKILL.md` lean; put encyclopedic detail in linked files the agent reads only when needed.
- Personal skills can live in `~/.cursor/skills/`; **project skills** in `.cursor/skills/` (shared with the team via git).

**Best for:**

- Multi-step **workflows** (“before push: A, B, C”).
- **Templates** (PR description, incident report, commit style with examples).
- Domain knowledge that is **not** needed on every message.

**Best practices:**

- Write `description` in **third person**, with both **WHAT** and **WHEN**, plus **trigger terms** (see Cursor’s create-skill guidance).
- Stay **concise**; assume the model is already strong—only add non-obvious value.
- Avoid storing skills in `~/.cursor/skills-cursor/` (reserved for Cursor’s built-ins).

**When to use:** When the right question is **“Should the agent read a playbook for this task?”** rather than **“Should every session carry this text?”**

---

## 4. “Instructions” and `instruction.md`

**There is no single standard filename `instruction.md` that all Cursor versions treat specially** the way `AGENTS.md` and `.cursor/rules/*.mdc` are treated. People often mean one of these instead:

| What people mean | Where it lives | Notes |
|------------------|----------------|--------|
| **User Rules** | Cursor Settings → Rules (user/global) | Applies across projects unless overridden; good for *your* tone, accessibility, date format, etc. |
| **Project rules** | `.cursor/rules/*.mdc` + optional `AGENTS.md` | Prefer these for *team-shared*, repo-specific behavior |
| **Legacy project file** | `.cursorrules` at repo root (older pattern) | Some projects still use one big file; splitting into `.mdc` rules is usually easier to maintain |
| **Random `instructions.md`** | Any path you choose | **Not magical** unless your team agrees to @-mention it or the agent is told to read it in `AGENTS.md` |

**Recommendation:** Treat **`AGENTS.md` + `.cursor/rules/`** as the canonical project instruction surface. If you maintain a custom `docs/.../instructions.md`, **link it from `AGENTS.md`** or a rule so the agent knows it exists.

---

## 5. `rules.md` (generic)

**Not a special Cursor filename by default.** If you create `rules.md`, it is just documentation unless:

- You reference it from `AGENTS.md`, or
- You duplicate its content into `.cursor/rules/*.mdc` (better for machine consumption).

**Use `rules.md`** for **humans** (onboarding, rationale). **Use `.mdc` rules** for **the agent**.

---

## 6. Custom slash commands (`/…`)

**What they are:** Reusable prompts you trigger from the chat/agent input by typing **`/`** and picking a command. Cursor loads the command’s text (usually from a markdown file) and runs it like a structured request.

**Where they live (typical layouts):**

| Scope | Path | Who gets it |
|-------|------|-------------|
| **Project** | `.cursor/commands/<name>.md` | Anyone who clones the repo |
| **Personal** | `~/.cursor/commands/<name>.md` | You, across workspaces |

Exact UI labels and discovery can change between Cursor versions; if a command does not appear, confirm the folder name (`.cursor/commands`), file extension (`.md`), and that the workspace root is the folder Cursor has open.

**How they differ from rules and skills:**

| Mechanism | Who turns it on? | Role |
|-----------|------------------|------|
| **Rules / `AGENTS.md`** | Automatic (by workspace / globs) | Persistent policy |
| **Skills** | Agent + task match on `description` | On-demand playbooks |
| **Slash commands** | **You** (explicit `/command`) | Repeatable **user-initiated** workflows |

**Best for:**

- Checklists you run on demand (“`/review` this PR”, “`/tests` for this module”).
- Long prompt templates you do **not** want injected into every session.
- Team-shared workflows versioned next to the code.

**Best practices:**

- One command = one job; split giant prompts into multiple commands.
- Start the file with a short **goal** line so future-you knows when to use it.
- Point to a **skill** or doc for depth instead of duplicating paragraphs inside the command file.

---

## 7. Subagents and delegated work

**What people mean by “subagents”:** Work is handed off to **another agent context** (specialized prompt, often different tools or model), so the main chat stays focused and large exploration does not eat the whole thread.

**Why use delegation:**

- **Context isolation** — Research across many files or long tool output stays out of your primary conversation.
- **Parallelism** — Multiple delegated tasks can run in parallel when the product supports it.
- **Specialization** — A narrow system prompt or tool set for “only search the repo” vs “only run shell.”

**Built-in patterns (conceptual):** Cursor’s agent stack may include specialized helpers (for example, **explore**-style codebase search, **shell**-focused command runners, or **browser** automation via MCP). You do not author these as repo files; they are part of the product. Treat them as **automatic delegation** for heavy or noisy subtasks.

**Custom subagents (when available):** Some Cursor versions let you define **custom agents** under paths such as `.cursor/agents/` (project) or `~/.cursor/agents/` (personal), often as markdown with frontmatter (name, instructions, tool/model hints). **Verify paths and schema in your Cursor version’s docs**—this area evolves quickly.

**How subagents relate to rules, skills, and commands:**

| Piece | Relationship to subagents |
|-------|---------------------------|
| **Rules / `AGENTS.md`** | Still apply to the **main** agent; clarify whether subagents inherit them (product-dependent—check current docs). |
| **Skills** | Good **source material** for what a custom subagent should do (“run the checklist in SKILL X”). |
| **Slash commands** | Often the **user-facing trigger** (“`/deep-dive`”) that starts a delegated or long-running workflow. |

**When to prefer which:**

- **Single thread + rules/skills** — Small edits, one file, short answers.
- **Slash command** — Same workflow many times; you want a button-like prompt.
- **Subagent / background work** — Large repo survey, long CI fix loop, or parallel tracks where isolation matters.

---

## 8. Other pieces people confuse with the above

| Mechanism | Role |
|-----------|------|
| **`.cursorignore`** | Like `.gitignore` for the AI: reduces noise; does not “teach” style |
| **`.cursor/plans/*.plan.md`** | Planning artifacts; not a substitute for rules/skills |
| **Chat system reminders / tool rules** | Ephemeral; you cannot rely on them for repo policy |
| **MCP servers** | Tools and data sources; some servers ship their own instructions—separate from repo rules |
| **Notepads / docs you @-mention** | Ad hoc context for one thread |

---

## 9. How to combine them without duplication

**Anti-pattern:** The same long bullet list copied into `AGENTS.md`, three `.mdc` files, and a skill. You will eventually update one place and forget the others.

**Recommended pattern:**

1. **`AGENTS.md`** — Non-negotiables for the whole repo + **links** (“see skill X for full checklist”).
2. **`.cursor/rules/*.mdc`** — Short, scoped guardrails + **one level of linking** into a skill or doc.
3. **`.cursor/skills/.../SKILL.md`** — The **deep** procedure, examples, pre-push steps.

This repo’s split is a good template:

- **Rule:** tiny summary for `*.py` / `*.ipynb`.
- **Skill:** full standards and workflow.
- **AGENTS.md:** commands that must run and commit format.

**Decision cheat sheet:**

- **Every session, whole repo** → `AGENTS.md` or `alwaysApply: true` rule (keep tiny).
- **When editing certain paths** → `globs` rule.
- **Heavy or occasional workflows** → skill with a strong `description`.
- **Personal preferences across all projects** → Cursor user Rules in settings.

---

## 10. Power-up checklist for your dev setup

1. **Write `AGENTS.md`** with 5–15 lines of “must do” items and links.
2. **Add one `alwaysApply` rule** only if something truly applies everywhere; otherwise prefer globs.
3. **Create skills** for: code review, release checklist, domain APIs, “how we run tests,” etc.
4. **Keep rules under one concern** and **under ~50 lines** of core content when possible.
5. **Link, don’t duplicate** long prose between rule and skill.
6. **Version-control** project rules and skills so teammates get the same agent behavior.
7. **Use personal skills** in `~/.cursor/skills/` for *your* cross-repo habits (commit style, shell preferences) if they are not project-specific.
8. **Add `.cursor/commands/`** for repeated workflows (review, test pass, release notes) and keep each command file short, linking to skills for detail.
9. **Use subagents / background agents** for large exploration or parallel tracks; keep policy in `AGENTS.md` + rules so behavior stays consistent where the product applies them.

---

## 11. Quick reference table

| File / location | Primary purpose | Typical activation |
|-----------------|-----------------|--------------------|
| `AGENTS.md` | Repo-wide agent instructions | Workspace / always in effect for project |
| `.cursor/rules/*.mdc` | Scoped or global machine-readable rules | `alwaysApply` or `globs` |
| `.cursor/skills/*/SKILL.md` | On-demand workflows and deep guidance | Matched via `description` / user task |
| `.cursorrules` | Legacy all-in-one project instructions | If present, still honored in some flows |
| Cursor **User Rules** | Personal global preferences | All projects (you) |
| Custom `instructions.md` | Documentation *you* define | Only if linked or @-mentioned |
| `rules.md` | Human doc | Not automatic for the agent |
| `.cursor/commands/*.md` | Custom **slash** prompts (`/name`) | You pick `/` in agent/chat input |
| `.cursor/agents/*` (if supported) | Custom **subagent** definitions | Delegation / background flows (see Cursor docs) |
| Built-in subagent helpers | Explore / shell / browser-style delegation | Product-managed; not repo files |

---

## 12. Where to learn more in this repo

- Root [`AGENTS.md`](../../AGENTS.md) — always-on repo instructions.
- [`.cursor/rules/`](../../.cursor/rules/) — scoped rules (`.mdc`).
- [`.cursor/skills/capstone-code-standards/SKILL.md`](../../.cursor/skills/capstone-code-standards/SKILL.md) — example skill with frontmatter and workflow.

Cursor’s own authoring guides are embedded in the **create-rule** and **create-skill** skills (if installed in your Cursor skills library).

**Cursor product docs (URLs change with releases):** [Slash commands](https://cursor.com/docs/cli/reference/slash-commands), [Subagents](https://cursor.com/docs/subagents), and the [Background agent](https://docs.cursor.com/background-agent) pages describe command files and delegation; confirm folder names and frontmatter in the version you run.
