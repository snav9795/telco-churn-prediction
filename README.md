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
| [`.cursor/`](.cursor/) | Editor skills and rules for this repo (safe to commit so collaborators share the same standards) |

## Quick start (modeling work)

```bash
cd churn-prediction
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Study guides

If `docs/study/` does not contain the daily `.md` files, see [`docs/study/RESTORE_STUDY_GUIDES.md`](docs/study/RESTORE_STUDY_GUIDES.md).

## Git: private workspace + public grading repo

- **Private (full workspace):** [`github.com/snav9795/CS5998---Capstone-Project`](https://github.com/snav9795/CS5998---Capstone-Project) — `git push origin main`
- **Public (grading, `churn-prediction/` only):** intended remote [`github.com/snav9795/telco-churn-prediction`](https://github.com/snav9795/telco-churn-prediction) — create the empty public repo if needed, then from the workspace root run [`scripts/Publish-PublicChurnRepo.ps1`](scripts/Publish-PublicChurnRepo.ps1) or `.\scripts\Publish-PublicChurnRepo.ps1 -CreatePublicRepo` (uses `gh`).

Full instructions: [`docs/setup/Two_Repos_Git.md`](docs/setup/Two_Repos_Git.md).
