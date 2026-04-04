# Day 6 — GitHub & Streamlit Cloud

**CS5998 Capstone Project | ~2 hours**

**Output:** Public GitHub repository, deployed app URL, polished README with demo link.

---

## 1. Concepts

- **Git:** `init`, `add`, `commit`, `push`; `.gitignore` excludes `venv/`, `__pycache__/`, large secrets.
- **GitHub:** Remote host; `main` branch; optional `README` badges.
- **Deployment:** Streamlit Community Cloud runs your repo; reads `requirements.txt` (often at repo root or path you configure).
- **Secrets:** Never commit API keys; use Streamlit secrets UI if you add keys later.

---

## 2. Why it matters

Assessors and markers need a **URL** and a **cloneable repo** for reproducibility.

---

## 3. Step-by-step tasks

### 3.1 `.gitignore` (repo root or `churn-prediction/`)

Ensure at least:

```
venv/
.venv/
__pycache__/
.ipynb_checkpoints/
.env
```

If the Git repo root is **only** `churn-prediction/`, initialize Git there. If the repo root is the **whole capstone workspace**, commit from parent folder—be consistent with where `README` lives.

**Recommended for class repos:** Make `churn-prediction/` the Git root so Streamlit Cloud points at a single app path.

### 3.2 GitHub repository

1. Create empty repo on GitHub (no README if you already have one locally).
2. In project folder:

```bash
git init
git add .
git commit -m "Initial commit: telco churn ML pipeline and Streamlit app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 3.3 Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io), sign in with GitHub.
2. **New app** → select repo, branch, **main file path** e.g. `app/Home.py` (relative to repo root).
3. Python version: match your local (3.10–3.12 typical).
4. If dependencies live in `churn-prediction/requirements.txt`, set working directory or duplicate a root `requirements.txt`—Cloud expects to find deps from the configured root.

### 3.4 Polish

- App title, short description, footer with course name.
- `st.spinner` for slow SHAP or predictions.
- Test **deployed** URL on phone/incognito.

### 3.5 README

Add at top:

```markdown
## Live demo

[Open the app](https://YOUR_APP.streamlit.app)
```

---

## 4. Common failures

- **Module not found:** Missing package in `requirements.txt` used by Cloud.
- **File not found:** Wrong working directory; model paths must work from Cloud’s cwd.
- **App sleeps:** Free tier spins down; cold start is normal—mention in video.

---

## 5. Viva prep

1. **What is reproducibility?** Clone → venv → pip install → run notebook/app → similar results.
2. **Why GitHub?** Version history, sharing, marker access.
3. **Difference between Git and GitHub?** Git is local; GitHub is hosting.

---

**Previous:** [`05_Day5_Guide.md`](05_Day5_Guide.md) · **Next:** [`07_Day7_Guide.md`](07_Day7_Guide.md)
