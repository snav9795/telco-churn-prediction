# Two repositories: private workspace + public `churn-prediction`

Use **one** Git working copy at the capstone workspace root. Push the full tree to a **private** GitHub repo and publish only `churn-prediction/` to a **public** repo for grading.

---

## Step 1 — Create both repositories on GitHub

1. Sign in at [https://github.com/new](https://github.com/new).
2. **Repo A (private)**  
   - Name: e.g. `cs5998-capstone-workspace`  
   - Visibility: **Private**  
   - Do **not** add README, .gitignore, or license (empty repo).
3. **Repo B (public)**  
   - Name: e.g. `telco-churn-prediction`  
   - Visibility: **Public**  
   - Do **not** add README, .gitignore, or license (empty repo).

Copy the HTTPS (or SSH) URLs for both. Example:

- Private: `https://github.com/YOUR_USERNAME/cs5998-capstone-workspace.git`
- Public: `https://github.com/YOUR_USERNAME/telco-churn-prediction.git`

---

## Step 2 — First-time Git setup (workspace root)

Open a terminal in the **capstone workspace root** (the folder that contains `churn-prediction/`, `docs/`, `.cursor/`, etc.).

If this folder is **not** yet a Git repository:

```powershell
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
git add .
git commit -m "Initial commit: full capstone workspace"
```

*(This repo may already have an initial commit. If `git init` says the folder is already a repository, skip `git init` and only set `user.name` / `user.email` if Git reports “Author identity unknown”.)*

Rename branch to `main` if needed:

```powershell
git branch -M main
```

Add **private** remote and push:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/cs5998-capstone-workspace.git
git push -u origin main
```

If `origin` already exists with a wrong URL:

```powershell
git remote set-url origin https://github.com/YOUR_USERNAME/cs5998-capstone-workspace.git
git push -u origin main
```

---

## Step 3 — Add public remote

```powershell
git remote add public https://github.com/YOUR_USERNAME/telco-churn-prediction.git
```

Verify:

```powershell
git remote -v
```

---

## Step 4 — First publish of the grading repo (subtree)

From the **same workspace root**:

```powershell
git subtree split --prefix=churn-prediction -b churn-public
git push public churn-public:main --force
```

After this, the **public** repository’s root matches the contents of your `churn-prediction/` folder (no extra `churn-prediction/` directory layer).

You can delete the local branch if you want (optional):

```powershell
git branch -d churn-public
```

---

## Ongoing workflow

| Action | Commands (from workspace root) |
|--------|--------------------------------|
| Save **everything** to private | `git add .` → `git commit -m "..."` → `git push origin main` |
| Update **public** grading repo | `git subtree push --prefix=churn-prediction public main` |

If `git subtree push` is slow or fails, use the **split + push** fallback again:

```powershell
git subtree split --prefix=churn-prediction -b churn-public
git push public churn-public:main --force
git branch -d churn-public
```

---

## Checklist

- [ ] Repo A private, Repo B public, both created empty on GitHub  
- [ ] `git push origin main` succeeds (full workspace)  
- [ ] `git push public …` succeeds (only `churn-prediction/` at public root)  
- [ ] No `.env` or API keys committed (see `.gitignore` files)  
- [ ] Course allows committing the Kaggle CSV; if not, remove from tracking and document download in public `README.md`

---

## What not to do

- Do **not** run `git init` inside `churn-prediction/` if you use this subtree workflow (nested repos conflict with tracking the same files at the parent).

For the submodule alternative, see the capstone plan document you used to set this up.
