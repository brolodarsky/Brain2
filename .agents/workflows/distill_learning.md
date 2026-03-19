---
description: Synthesizes complex technical articles or PDFs into atomic, interlinked notes within the Zettelkasten.
---

# Workflow: Distill Learning (`/distill_learning`)

This workflow mitigates the friction of adding dense, complex information (like research papers or deep technical tutorials) into the knowledge base by breaking them down into atomic, linked notes.

## Trigger
When asked to "distill this article", "summarize this paper into the vault", or when invoking `/distill_learning [URL or PDF path]`.

## Steps

1. **Read & Absorb:**
   - Read the provided source material (using `read_url_content` for web pages or `view_file` for local PDFs).

2. **Extract Core Concepts:**
   - Identify the 1-3 most critical, distinct concepts, algorithms, or theories presented in the material.
   
3. **Draft Atomic Notes:**
   - For each extracted concept, draft a new atomic note.
   - Follow the `generate_obsidian_note` skill: use proper YAML frontmatter, ensure the title is specific but concise, and write the body in your own instructional format.

4. **Map to Knowledge Base:**
   - Analyze `Vault/Table of Contents.md` (specifically focusing on sections like `6.2. Library & Learning` or `3.1. Wealth & Asset Management`).
   - Determine exactly where each new atomic note belongs structurally.
   
5. **Establish Connections (Intra-linking):**
   - Ensure the new atomic notes link back to the **source material** (URL or PDF).
   - Ensure they link to **each other** if part of the same paper.
   - Crucially, search the Vault for related existing concepts and add `[[wiki-links]]` tying the new knowledge into the existing web.

6. **Review and Execute:**
   - Present a concise summary to the user: "I will create `Concept A.md` in `6.2.1` and `Concept B.md` in `6.2.3`. Is this correct?"
   - Await execution approval. Upon approval, create the physical files and update the `Table of Contents.md`.
