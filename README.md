# AnswerCheck

**A short-answer self-check for students.** Paste a question, a reference answer
(from your textbook or notes) and your own answer. A fine-tuned transformer model
says whether your answer looks **correct, partly correct or incorrect**, with a
confidence score, and says **"not sure"** when its confidence is low.

> **Status:** early development (Phase 0: project setup). Nothing works yet.

## Honest limits

- It is a **study aid, not an official grader**. It can be wrong.
- It is trained on science-domain data (SciEntsBank, Beetle). Results on your
  own university course are **not guaranteed**.
- You must supply a reference answer.
- No LLMs and no paid APIs are used anywhere.

## Quick start (local)

```bash
git clone https://github.com/hassnain45/answercheck.git
cd answercheck
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt -e .
pytest
```

## Quick start (Google Colab)

Open `notebooks/01_colab_setup.ipynb` in Colab
(File > Open notebook > GitHub > `hassnain45/answercheck`) and run all cells.

## Repository layout

| Folder | What goes there |
| --- | --- |
| `src/answercheck/` | All project code (data, models, training, evaluation, inference) |
| `notebooks/` | Thin Colab notebooks that call the code in `src/` |
| `configs/` | YAML settings for each model / experiment |
| `experiments/` | One JSON result file per run |
| `tests/` | Automated tests (`pytest`) |
| `app/` | The Gradio web app |
| `docs/` | Data report, model card, paper |

## Licence

Code: MIT (see `LICENSE`). Datasets have their own licences (to be recorded in
`DATA_LICENSES.md`).
