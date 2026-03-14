---
description: End-to-end workflow for creating a new Obsidian note in the Knowledge Base
---

# Create New Note

Use this workflow whenever you need to add a new note to the Knowledge Base.

## Steps

1. Identify the topic and which H1 section in `Vault/Table of Contents.md` it belongs to.

2. Apply the `sync_vault_structure` skill to confirm the target folder exists. Create it if missing.

3. Apply the `generate_obsidian_note` skill to create the note file with correct YAML frontmatter, structure, and intra-links.

4. Add a `[[Wiki-link]]` to the new note from the appropriate section of `Vault/Table of Contents.md`.

5. Confirm with the user that the note content and placement look correct.
