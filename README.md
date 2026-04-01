# Brain 2

This is a personal "second brain"/knowledge management system that stores/uses markdown notes, images, pdfs and other files in a Vault as thoughts & memories.

It's read and tinkered with in Obsidian, tinkered with in agentic IDEs, version-controlled with Git, and synced to mobile via Syncthing.

Notes follow the Zettelkasten methodology. Vault folder structure is defined in `Table of Contents.md`. Several "brain engine" tools are available to help with automation.

---

## Repository Structure

```
Brain 2/
├── .agents/                    # AI agent instructions
│   ├── skills/                 # Mandatory behaviors
│   │   ├── analyze_health/           # Health diagnostics & context check
│   │   ├── analyze_psych/            # Psych support & cognitive architecture
│   │   ├── cleanup_orphans/          # Zettelkasten maintenance (links/folders)
│   │   ├── conventional_commits/     # Commit message format rules
│   │   ├── generate_obsidian_note/   # How to create new notes
│   │   ├── maintain_project_docs/    # Keep README & requirements.
│   └── workflows/              # Structured procedures (slash commands)
│       ├── add_job_requirement.md    # Job criteria extraction
│       ├── audit_inbox.md            # Zettelkasten inbox sorting
│       ├── create_new_note.md        # Obsidian note creation
│       ├── create_project.md         # Project planning/tasks
│       ├── distill_learning.md       # Atomic note synthesis
│       ├── plan_activity.md          # Itinerary generation
│       └── render_resume.md          # PDF resume rendering
├── .venv/                      # Python virtual environment (not committed)
├── Vault/                      # All Brain content lives here
│   ├── .obsidian/              # Obsidian settings
│   ├── .stfolder/              # Syncthing folder
│   ├── 1. The Core/                # Identity, governance, and foundations
│   │   ├── 1.1. Philosophy & Personal North Star/    # Values, principles, and long-term vision
│   │   ├── 1.2. Personal Knowledge Management (PKM)/ # Brain 2.0 meta and maintenance protocols
│   │   ├── 1.3. Security & Digital Sovereignty/      # Encryption, password strategy, and inheritance
│   │   └── 1.4. Emergency & Survival/                # Crisis protocols and emergency contacts
│   ├── 2. Health/                  # Physical and mental well-being
│   │   ├── 2.1. Fitness/                             # Training logs and performance tracking
│   │   ├── 2.2. Medical/                             # Health history, lab work, and sleep hygiene
│   │   │   ├── Health Logs/                          # Doctor visit notes (PCP, ENT, Pulmonology, etc.)
│   │   │   └── Lab Work/                             # Bloodwork results (BMP, CBC, Thyroid, etc.)
│   │   ├── 2.3. Psych/                               # Cognitive load and mindfulness rituals
│   │   └── 2.4. Nutrition/                           # Recipe vault and nutrition science
│   ├── 3. Operations & Wealth/     # Financial and logistical systems
│   │   ├── 3.1. Wealth & Asset Management/           # Investment strategy and recurring payments
│   │   ├── 3.2. Infrastructure & Logistics/          # Home lab, family estate, and auto maintenance
│   │   │   ├── 3.2.1. Home Improvement & Maintenance/
│   │   │   ├── 3.2.2. Family & Care/
│   │   │   └── 3.2.3. Auto/
│   │   └── 3.3. Career Strategy & Revenue/           # Job hunt, professional profile, and portfolio
│   │       ├── 3.3.1. Market Research & Future of Work/
│   │       ├── 3.3.2. Interview Prep & Technical Depth/
│   │       ├── 3.3.3. Professional Portfolio & Evidence/
│   │       ├── 3.3.4. Networking & Professional CRM/
│   │       ├── 3.3.5. Income Streams & Side Revenue/
│   │       └── 3.3.6. Compensation & Negotiation/
│   ├── 4. Playground/              # Social, culture, and creativity
│   │   ├── 4.1. Social Life & Community/             # People data, social club, and adventures
│   │   ├── 4.2. Romance & Partnership/               # Relationship maintenance and date ideas
│   │   ├── 4.3. Culture & Inspiration/               # Media archive, reading list, and education
│   │   └── 4.4. Creativity/                          # Writing, jokes, and creative exploration
│   ├── 5. Capture & Archive/       # Inbox and memory bank
│   │   ├── 5.1. Brain Dump & Inbox/                  # Quick capture and significant milestones
│   │   ├── 5.2. The Content Log (General)/           # Web archive and YouTube history
│   │   └── 5.3. Digital Inventory/                    # Hardware/software audits and backups
│   ├── 6. Forge/                   # Technical projects and learning
│   │   ├── 6.1. Projects/                            # Active development "The Lab"
│   │   │   ├── 6.1.1. Flagship Applications/         # Primary high-importance projects (Feeder, etc.)
│   │   │   ├── 6.1.2. Agentic R&D/                   # Agentic skills, workshops, and tinkering
│   │   │   ├── 6.1.3. Maintenance & Assets/          # Stable portfolios and meta-checklists
│   │   │   └── 6.1.4. Script Attic/                  # Inactive tools and experiments
│   │   └── 6.2. Library & Learning/                  # Technical archive and deep-dives
│   ├── Audio/                  # Gitignored
│   └── Table of Contents.md   # Master index — source of truth for structure
├── AGENTS.md                   # AI agent constitution
├── CHANGELOG.md                # Running log of notable changes
├── tools/                      # Automation tools
│   └── resume_engine/          # Premium PDF rendering system
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

## The Engine (Skills, Workflows & Tools)

This repository distinguishes between three types of "cognitive" capabilities that define how the Brain automation works:

1. **Skills (`.agents/skills/`)**: **Mandatory Behaviors**. These are instructions the AI Agent *must* follow whenever a specific trigger occurs (e.g., formatting a note or updating the changelog).
2. **Workflows (`.agents/workflows/`)**: **Active Procedures**. These are multi-step "recipes" (Slash Commands) for the agent to follow to achieve complex outcomes (like sorting an inbox or planning a project).
3. **Tools (`tools/`)**: **Deterministic Capabilities**. These are Python scripts for repetitive, heavy-lifting tasks (like MP3 generation or folder maintenance) that are triggered manually via terminal.

### Agent Skills (Mandatory Behaviors)

| Skill | Trigger |
|---|---|
| `analyze_health` | When asked about symptoms, medical conditions, or health advice |
| `analyze_psych` | When asked about emotional processing |
| `generate_obsidian_note` | When asked to create a new note or integrate new notes/thoughts into the vault |
| `maintain_project_docs` | Keep README.md, AGENTS.md, CHANGELOG.md and requirements.txt up to date |
| `conventional_commits` | On every `git commit` |
| `cleanup_orphans` | When asked to "clean the vault" or perform maintenance |

### Agentic Workflows (Slash Commands)

- `/add_job_requirement`: Automates extracting skills from a job description (PDF/URL).
- `/audit_inbox`: Sorts raw notes and bullet points from the Brain Dump & Inbox into the main Zettelkasten structure.
- `/create_project`: Consolidates rough notes or ideas into a structured project note, complete with extracted tasks and materials.
- `/distill_learning`: Synthesizes complex technical articles or PDFs into atomic, interlinked notes.
- `/plan_activity`: Cross-references Activities List, Date Ideas, and People Data notes to generate a structured markdown itinerary.
- `/render_resume`: Renders the Master Markdown Resume into a premium, professionally-styled PDF.

### Deterministic Tools (Scripts)

| Tool | Purpose | Usage |
|---|---|---|
| `generate_podcast.py` | Converts Vault notes to MP3 via edge-tts. | `python tools/generate_podcast.py` |
| `create_folders.py` | Idempotently creates the folder structure from TOC. | `python tools/create_folders.py` |
| `check_folders.py` | Validates Vault structure against TOC (dry-run). | `python tools/check_folders.py` |
| `add_gitkeeps.py` | Adds `.gitkeep` to all empty folders for Git tracking. | `python tools/add_gitkeeps.py` |
| `backup_vault.py` | Creates a timestamped local backup of the `Vault/`. | `python tools/backup_vault.py` |
| `resume_engine/` | PDF rendering system for the Master Resume. | (See `tools/resume_engine/`) |

---

## Security & Encryption

This repository uses **`git-crypt`** to transparently encrypt all personal content before it is pushed to GitHub. 

- **What is encrypted:** Everything inside the `Vault/` directory (except structural `.gitkeep` files).
- **What is visible:** Folder names and file names remain visible on GitHub, but the actual file contents are scrambled.
- **Master Key:** The symmetric key (`brain-key.key`) is required to unlock the repository on a new machine. It is strictly ignored by `.gitignore` and must be backed up securely off-site (e.g., in a password manager).

To unlock the repository on a new machine after cloning:
```bash
git-crypt unlock /path/to/your/brain-key.key
```

---

## Vault Maintenance
Whenever the `Table of Contents.md` is modified, run `tools/create_folders.py` to ensure the folder structure matches the plan.

- Handle `.gitkeep` files: add to empty folders, remove from populated ones.
- Orphaned folders (no matching TOC entry) should be reported, never deleted automatically.

---

## Obsidian Setup

Point Obsidian at the **`Vault/`** subfolder, not the repo root.

> Settings → About → Vault path → `…/Brain 2/Vault`
