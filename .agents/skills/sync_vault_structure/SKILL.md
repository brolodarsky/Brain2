---
description: Automatically sync Vault folder structure whenever Table of Contents changes
---

# Vault Structure Sync — Mandatory Trigger

**ALWAYS run this skill whenever `Vault/Table of Contents.md` is modified in any way**, including:
- A new H1 section (`#`) is added
- An existing H1 section is renamed
- An H1 section is removed

> This skill manages **folders only**. It does NOT create, move, or delete note files.
> When creating a new note inside a folder, use the `generate_obsidian_note` skill.

---

## What You Must Do (Every Time)

1. **Parse H1s from the TOC.** Read `Vault/Table of Contents.md` and extract every line starting with a single `# `. Strip the `# ` prefix — the remainder is the exact required folder name. Ignore YAML frontmatter and H2+ headers.

2. **List existing Vault folders.** Call `list_dir` on `Vault/`. Ignore `Audio/` and `zImages/`.

3. **Create any missing folders.** For every expected folder name not yet present in `Vault/`, create it immediately. Place a `.gitkeep` file inside so Git tracks it.

4. **Normalise `.gitkeep` across all empty folders.** Scan every Vault folder. If a folder is empty and has no `.gitkeep`, create one. Git ignores empty folders entirely, so this ensures they are always pushed to GitHub regardless of how they were originally created.

5. **Remove stale `.gitkeep` files.** If a folder now contains real content (i.e., any file other than `.gitkeep`), delete its `.gitkeep` — it is no longer needed and just adds noise.

6. **Report orphaned folders — never delete them.** If a folder exists in `Vault/` but has no matching H1, notify the user:
   > ⚠️ `X. Old Name/` has no matching H1 in the TOC. Was it renamed? Confirm and I can rename it for you.

7. **Confirm sync.** After completing, tell the user how many folders were created and list any discrepancies found.

---

## Shortcut

Instead of doing this manually, you can run the companion script, after asking for user permission:
```bash
python sync_vault.py
```
