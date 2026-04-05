---
description: Breaks down a dense external source (article, paper, PDF, URL) into multiple atomic, interlinked notes filed into the Library & Learning section of the Zettelkasten. Use this when you want to deeply integrate knowledge — not just save it. For lightweight saving of raw content, use /capture_content instead.
---

# Workflow: Distill Learning (`/distill_learning`)

This workflow mitigates the friction of adding dense, complex information (like research papers or deep technical tutorials) into the knowledge base by breaking them down into atomic, linked notes.

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

7. **(Optional) Update Current Learning:**
   - If the distilled material represents an active area of study, add or update an entry in `Vault/1. The Core/1.1. Philosophy & Personal North Star/Current Learning.md` linking to the new notes.
