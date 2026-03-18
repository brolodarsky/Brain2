---
description: Identify and report broken wiki-links and empty folders in the Vault.
---

# Cleanup Orphans — Maintenance Skill

Use this skill when asked to "clean the vault", "find orphans", or perform periodic Zettelkasten maintenance.

## Trigger
- Explicit user request to find broken links, missing files, or empty folders.

## Objectives

1. **Find Broken Wiki-Links:**
   - Scan all `.md` files in `Vault/` for `[[wiki-links]]` syntax.
   - Identify any link that points to a non-existent file. Note: Obsidian wiki-links usually point to file basenames without the `.md` extension.
   - Compile a list of exactly which files contain the broken links, and what the broken target is.

2. **Find Empty Folders:**
   - Scan `Vault/` for directories that contain no `.md` or media files (ignoring `.gitkeep`).
   - Flag these for potential removal.

## Action Protocol

1. **Scan and Analyze:** Use tools (e.g. `grep_search`, `list_dir`, or Python scripts) to discover the broken links and empty directories.
2. **Report:** Do NOT delete or modify files automatically. Present a concise report to the user listing:
   - Every file containing a broken link, alongside the broken link text.
   - Every empty folder found.
3. **Resolution:** Wait for the user to instruct you on how to resolve each item (e.g. "delete the links", "create the missing notes", or "remove the empty folders").
