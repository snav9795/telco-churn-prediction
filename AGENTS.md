# Agent instructions (CS5998 capstone workspace)

Use this file together with [`.cursor/rules/`](.cursor/rules/) and [`.cursor/skills/capstone-code-standards/SKILL.md`](.cursor/skills/capstone-code-standards/SKILL.md) when editing this repository.

## Python indentation and syntax

Before finishing a change that touches Python under `churn-prediction/`, run from the **workspace root** (stdlib only; use the project venv if `python` is not on `PATH`):

```powershell
python -m tabnanny churn-prediction
python -m compileall -q churn-prediction
```

- `tabnanny`: flags ambiguous or mixed tab/space indentation in `.py` files.
- `compileall`: catches syntax errors including `IndentationError`. Omit `-q` to list files as they compile.

If either command reports problems, fix them before suggesting the work is complete.

## Git commit messages

Use a **structured** subject line and an optional body:

```text
<type>(<scope>): <short imperative summary>

- Optional bullets (what changed / why)
```

- **Types:** `feat`, `fix`, `docs`, `refactor`, `chore`, `test` (others only if clearly needed).
- **Scope:** short and useful, e.g. `churn-prediction`, `readme`, `scripts`.
- **Subject:** imperative mood, roughly within 72 characters, no trailing period.

When the user asks for a commit message or you propose one after edits, follow this format. For a multi-line message in PowerShell you can use a here-string piped to `git commit -F -` (see root [README.md](README.md) § *Check indentation & structured commits*).

## Scope and style

For Python/notebook style (comments, naming, what not to “clean up” unsolicited), follow the capstone standards rule and skill linked above.
