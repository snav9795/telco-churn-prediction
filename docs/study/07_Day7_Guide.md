# Day 7 — Final report, video, submission

**CS5998 Capstone Project | ~2 hours (spread over writing days)**

**Output:** Final report document, ~6 min demo video, reproducibility checklist, LMS submission with links.

---

## 1. Concepts

- **Technical report:** Problem → data → methods → results → interpretation → limitations → ethics → conclusion.
- **Reproducibility:** Exact steps, versions, random seeds, and file layout so others can rerun.
- **Demo video:** Screen capture + voice; show live deployed app, not only slides.

---

## 2. Why it matters

Milestone 3 is **50%** of the capstone; clarity and completeness matter as much as model accuracy.

---

## 3. Report structure (suggested)

Save as `churn-prediction/reports/Final_Report.md` or Word/PDF per course rules.

1. **Title, author, abstract** (150–250 words).
2. **Introduction** — business problem, churn cost, project goal.
3. **Data** — source, size, features, target, missing values, EDA highlights (embed figures).
4. **Methods** — preprocessing, models, metrics, SHAP, system architecture figure.
5. **Results** — tables, ROC, confusion matrices, comparison LR vs XGBoost.
6. **Discussion** — what drives churn, limitations, bias/fairness note if relevant.
7. **Deployment** — Streamlit overview, URL, how to run locally.
8. **Conclusion** — deliverables summary, future work.
9. **References** — Kaggle dataset, papers, libraries.
10. **Appendix** — hyperparameters, hardware, full metric tables (optional).

Page count: follow course spec (often 25–30 pages with figures).

---

## 4. Demo video checklist (~6 minutes)

| Time | Content |
|------|---------|
| 0:00–0:45 | Introduce yourself, problem, dataset |
| 0:45–1:30 | Quick GitHub tour (README, folders) |
| 1:30–4:30 | **Live deployed app**: all 3 pages |
| 4:30–5:30 | One SHAP or metric insight |
| 5:30–6:00 | How to reproduce (`requirements.txt`, run command) |

Tools: OBS Studio, Zoom local record, or PowerPoint screen record.

---

## 5. Reproducibility checklist

- [ ] `requirements.txt` installs without errors on a clean venv
- [ ] Random seeds set where relevant (`random_state`)
- [ ] Raw data path documented (or script to download)
- [ ] Notebooks run top-to-bottom after preprocess
- [ ] Streamlit command documented in README
- [ ] Public app URL in README and report

---

## 6. Submission pack

Per LMS instructions, typically:

- Final report PDF
- Demo video file or link (unlisted YouTube if allowed)
- GitHub repository URL
- Live Streamlit URL
- Any signed coversheets

---

## 7. Viva prep

1. **Biggest weakness of your model?** Imbalance, linearity assumptions, or data age.
2. **How would you deploy in a real company?** Batch scoring, API, monitoring drift.
3. **Ethical concern?** Using predictions for discriminatory pricing or denial of service without oversight.

---

**Previous:** [`06_Day6_Guide.md`](06_Day6_Guide.md) · **Glossary:** [`Concepts_Reference.md`](Concepts_Reference.md)
