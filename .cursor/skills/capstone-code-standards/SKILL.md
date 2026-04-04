---
name: capstone-code-standards
description: >-
  Applies MDSAI capstone code style for Python and Jupyter in this repo: self-explanatory
  naming, minimal comments (brief only for non-obvious logic), sparse notebook code cells.
  Use when writing or editing .py/.ipynb under churn-prediction, refactoring before push, or
  when the user asks for style cleanup or comment reduction.
---

# Capstone code standards

## Comments

- Remove comments that only restate the next line or a clear name (e.g. `# load data` above `load_data()`).
- Keep **at most one short line** where the *why*, a subtle invariant, or a non-obvious algorithm step cannot be expressed via naming alone.
- Do not strip license headers, required attribution, or course-mandated markers if present.

## Naming

- Prefer descriptive `class`, `def`, and variable names over explanatory comments.
- Accept conventional ML shorthand (`X_train`, `y_val`, `df`, etc.) where standard in notebooks and sklearn-style code.

## Docstrings

- If the course rubric requires them: use a **single line** on public entry points (modules, main public functions); omit verbose Google/NumPy-style blocks on trivial helpers and private internals unless the rubric demands it.
- If the rubric is silent: default to clear naming plus minimal comments as above.

## Jupyter notebooks

- Put narrative and methodology in **markdown cells**; keep code cells lean.
- Avoid long `#` comment blocks in code that duplicate markdown.

## Scope (do not “clean” unless asked)

- Leave pedagogical content in `docs/study/` and `docs/course/`, formal writeups in `churn-prediction/reports/`, and `docs/submissions/` unchanged unless the user explicitly requests edits there.

## Before `git push` (code pass)

1. Limit changes to intended code paths (e.g. `churn-prediction/src/**/*.py`, `churn-prediction/notebooks/**/*.ipynb` once they exist).
2. Apply this skill in one pass: drop redundant comments, rename where it improves clarity, preserve behavior and outputs.
3. Review diffs (especially notebooks) before committing.
