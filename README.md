# CS5998 — Capstone Project workspace

**Master of Data Science & Artificial Intelligence**

This folder is the top level for coursework, the telco churn deliverable, and Cursor project settings.

## Layout

| Path | Purpose |
|------|---------|
| [`churn-prediction/`](churn-prediction/) | Main **code project**: data, notebooks, `src/`, app, `requirements.txt`, milestone reports tied to the build |
| [`docs/course/`](docs/course/) | Official course-facing reference (e.g. student guide) |
| [`docs/study/`](docs/study/) | Optional 7-day study guides and concept sheets (see restore note inside if files are missing) |
| [`docs/submissions/`](docs/submissions/) | Portal-style submissions (e.g. milestone 1 text exports) |
| [`AGENTS.md`](AGENTS.md) | Instructions for AI assistants: Python indent/syntax checks before wrap-up, structured commit messages |
| [`.cursor/`](.cursor/) | Editor skills and rules for this repo (safe to commit so collaborators share the same standards) |

## Quick start (modeling work)

From the workspace root, work inside `churn-prediction/` and install dependencies.

**Option A — reuse an existing venv (Windows)**  
If you already have a shared environment at `%USERPROFILE%\envs\py_3_12` (Python 3.12.10, created with `python -m venv` from pyenv’s interpreter):

```powershell
cd churn-prediction
& "$env:USERPROFILE\envs\py_3_12\Scripts\Activate.ps1"
pip install -r requirements.txt
```

**Option B — new venv inside the repo**

```powershell
cd churn-prediction
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Check indentation & structured commits

**AI assistants:** the same expectations are in [`AGENTS.md`](AGENTS.md) and the always-on Cursor rule [`.cursor/rules/agent-indent-and-commits.mdc`](.cursor/rules/agent-indent-and-commits.mdc).

From the **workspace root** (any shell with `python` on `PATH`; use your venv if you prefer):

**Python indentation and block structure** — stdlib only:

```powershell
python -m tabnanny churn-prediction
python -m compileall -q churn-prediction
```

- `tabnanny` reports ambiguous or mixed tab/space indentation in `.py` files.
- `compileall` fails on syntax errors (including `IndentationError`). Drop `-q` to see filenames as they compile.

**Commit message** — use a clear, structured line (and optional body). Pattern:

```text
<type>(<scope>): <short imperative summary>

- Bullet details if useful (what / why)
```

Common `<type>` values: `feat`, `fix`, `docs`, `refactor`, `chore`, `test`. Use a small `<scope>` when it helps (e.g. `churn-prediction`, `readme`).

**One-shot commit from PowerShell** (message from a here-string; adjust `git add` as needed):

```powershell
git add -A
@"
feat(churn-prediction): train baseline model and save metrics

- Add notebook run notes; no API change
"@ | git commit -F -
```

## Study guides

If `docs/study/` does not contain the daily `.md` files, see [`docs/study/RESTORE_STUDY_GUIDES.md`](docs/study/RESTORE_STUDY_GUIDES.md).

## Git: private workspace + public grading repo

- **Private (full workspace):** [`github.com/snav9795/CS5998---Capstone-Project`](https://github.com/snav9795/CS5998---Capstone-Project) — `git push origin main`
- **Public (grading, `churn-prediction/` only):** intended remote [`github.com/snav9795/telco-churn-prediction`](https://github.com/snav9795/telco-churn-prediction) — create the empty public repo if needed, then from the workspace root run [`scripts/Publish-PublicChurnRepo.ps1`](scripts/Publish-PublicChurnRepo.ps1) or `.\scripts\Publish-PublicChurnRepo.ps1 -CreatePublicRepo` (uses `gh`).

Full instructions: [`docs/setup/Two_Repos_Git.md`](docs/setup/Two_Repos_Git.md).
