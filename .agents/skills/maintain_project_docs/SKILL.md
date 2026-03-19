---
description: Keep requirements.txt and README.md and CHANGELOG.md in sync whenever changes warrent it.
---

# Maintain Project Docs — Mandatory Trigger

## Trigger 1: After any `pip install` or `pip uninstall`

**ALWAYS regenerate `requirements.txt` immediately after installing or removing a Python package.**

Run this from the repo root:
```powershell
.venv\Scripts\pip.exe freeze > requirements.txt
```

Then commit `requirements.txt` along with whatever other changes prompted the install.

---

## Trigger 2: After adding, removing, or significantly changing project

**ALWAYS check whether `README.md` needs updating** when:
- A new `.py` script is added to the repo root
- An existing script's purpose, usage, or flags change
- A script is deleted
- An agentic skill or workflow is added, removed, or significantly changed.
- `/Vault` folder structure is changed.

Update the relevant section in `README.md` under `## Scripts`. Each script entry should include:
- **What it does** (one sentence)
- **Usage** — exact command to run
- **Any flags or config options** the user might need to know

Do not rewrite sections unrelated to the changed script.

---

## What Does NOT Need a README Update
- Internal refactors with no change to user-facing behaviour
- Bug fixes that don't change how the script is invoked
- Changes to agent skills or workflows (those are self-documenting)
