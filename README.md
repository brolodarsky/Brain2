# Knowledge Base

A personal AI/ML knowledge base built in [Obsidian](https://obsidian.md/), version-controlled with Git, and synced across devices via [Syncthing](https://syncthing.net/).

Notes follow the [Zettelkasten](https://zettelkasten.de/introduction/) methodology — atomic, interlinked, and tagged.

---

## Repository Structure

```
Knowledge Base/
├── .agents/                    # AI agent skills & workflows
│   ├── skills/
│   │   ├── conventional_commits/     # Commit message format rules
│   │   ├── generate_obsidian_note/   # How to create new notes
│   │   ├── maintain_project_docs/    # Keep README & requirements.txt in sync
│   └── workflows/
│       └── create_new_note.md        # End-to-end note creation flow
├── .venv/                      # Python virtual environment (not committed)
├── Vault/                      # All Obsidian content lives here
│   ├── 1. Foundational Mathematics & Statistics/
│   ├── 2. Programming & Software Engineering/
│   ├── 3. Machine Learning Fundamentals/
│   ├── 4. Deep Learning (DL)/
│   ├── 5. Natural Language Processing (NLP) & Vector Search/
│   ├── 6. Intelligent Agents & Autonomy/
│   ├── 7. Data Processing, Engineering & MLOps/
│   ├── 8. Computer Vision (CV)/
│   ├── 9. Reinforcement Learning (RL)/
│   ├── 10. Robotics (Hardware & Control Systems)/
│   ├── 11. AI Ethics, Safety & Governance/
│   ├── 12. Career Development & Strategy/
│   ├── Audio/                  # Generated MP3s — synced via Syncthing, not Git
│   ├── zImages/                # Embedded images
│   └── Table of Contents.md   # Master index — source of truth for structure
├── AGENTS.md                   # AI agent constitution for the repo
├── CHANGELOG.md                # Running log of notable changes
├── generate_podcast.py         # Converts notes to MP3 audiobooks
├── requirements.txt            # Pinned Python dependencies
└── .gitignore
```

---

## Setup

First time on a new machine:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> The `.venv/` folder is excluded from Git. `requirements.txt` is the source of truth for dependencies.

---

## Scripts

### `generate_podcast.py`
Converts every Markdown note in the Vault into an MP3 using Microsoft's neural TTS voices via [`edge-tts`](https://github.com/rany2/edge-tts).

- Only regenerates notes that are **new or modified** since the last run.
- Output goes to `Vault/Audio/` — excluded from Git, synced via Syncthing.
- Voice can be changed by editing `VOICE` at the top of the script.

**Usage** (from repo root, with `.venv` active or not):
```bash
python generate_podcast.py
```

**Setup** (first time only):
```bash
.venv\Scripts\Activate.ps1      # Windows PowerShell
pip install edge-tts
```

---

### Vault Maintenance
Any time `Vault/Table of Contents.md` is modified, the directory structure must be affirmed to match.

- Ensure every top-level H1 section has a matching folder in `Vault/`.
- Handle `.gitkeep` files: add to empty folders, remove from populated ones.
- Orphaned folders (no matching H1) should be reported, never deleted automatically.

---

## Obsidian Setup

Point Obsidian at the **`Vault/`** subfolder, not the repo root.

> Settings → About → Vault path → `…/Knowledge Base/Vault`

---

## Agent Skills

AI agent skills live in `.agents/skills/`. Each skill is a `SKILL.md` file that instructs the agent how to behave for a specific task:

| Skill | Trigger |
|---|---|
| `generate_obsidian_note` | When asked to create a new note |
| `maintain_project_docs` | After `pip install`/`uninstall`, or after adding/changing scripts |
| `conventional_commits` | On every `git commit` |
