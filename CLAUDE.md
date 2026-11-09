# CLAUDE.md — working rules for Claude Code

Project: **AnswerCheck**, a short-answer self-check study aid for students
(github.com/hassnain45/answercheck). The full plan is in the project brief; this
file holds the rules from section 6 of that brief.

## Working rules

- Work on one phase at a time. At the end, show outputs and wait for
  confirmation. Do not start the next phase.
- Never invent numbers, citations, links or licences. Every reported metric must
  come from a logged run file. If unsure, say so.
- Never tune on a test set. Use grouped validation as defined in Phase 2.
- Do not commit data, checkpoints, model files, tokens or keys. Use environment
  variables and Colab Secrets.
- Free tools only. No paid APIs, no paid GPUs, no LLM calls.
- Keep logic in `src/`, notebooks thin. Pin versions. Fix and log random seeds.
  Write tests for splits, metrics and inference.
- Explain each technical decision in one or two plain sentences. Use
  beginner-friendly comments.
- Before using any hosting or tool, re-check its current free-tier limits and
  flag any doubt.
- Prefer simple solutions. Do not add complex architectures only to look
  advanced.

## Practical notes

- Local setup: `python -m venv .venv`, then
  `.venv/bin/pip install -r requirements.txt -e .`, then `.venv/bin/pytest`.
- Training runs on Google Colab. Colab does not push to GitHub: code is edited
  and pushed locally, and Colab only clones / pulls.
- Run logs go to `experiments/` as one JSON per run (config, seed, split,
  metrics, git commit).
