# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).

---

## [Unreleased]

## [1.0.1] - 2026-03-16

### Added
- "Middle ground" TOC header structure in section 3.2 (3.2.x numbered, children unnumbered)
- Top-level files in `Vault/` created to match full TOC structure
- Added new category files and documentation

### Changed
- Relocated Library & Learning resources from `Vault/` root to `Vault/3. Forge/`

### Removed
- `sync_vault.py` — script deleted in favor of direct agentic structure management

## [1.0.0] - 2026-03-14

### Added
- `generate_podcast.py` — converts all Vault notes to MP3 via edge-tts
- `sync_vault.py` — syncs Vault folder structure with Table of Contents H1 sections
- `AGENTS.md` — central AI agent constitution for the repository
- `README.md` — project documentation with setup, scripts, and structure
- `requirements.txt` — pinned Python dependencies
- `.agents/skills/generate_obsidian_note` — skill for creating Zettelkasten-formatted notes
- `.agents/skills/sync_vault_structure` — mandatory skill for folder/TOC sync
- `.agents/skills/maintain_project_docs` — mandatory skill for requirements.txt and README updates
- `.agents/skills/conventional_commits` — mandatory skill for commit message format
- `.agents/workflows/create_new_note` — end-to-end note creation workflow
- Vault folder structure created for all 12 TOC sections
- `.gitkeep` normalisation across all empty Vault folders

### Changed
- Reorganised repo: moved all Obsidian content into `Vault/` subfolder
- `generate_podcast.py` resolves edge-tts from `.venv` automatically
- `.gitignore` updated to exclude `.venv/`, `Vault/Audio/`, and `podcast_history.json`
