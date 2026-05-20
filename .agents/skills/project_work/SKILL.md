---
name: project_work
description: Keep active project documents inside the Vault up to date whenever changes are planned, implemented, completed, or conceptually modified. Make sure to use this skill whenever you complete a task related to a project, plan modifications, create a new sub-project, or add/remove tasks conceptually from any Project - *.md file, even if the user does not explicitly request it.
---

# Mandatory Behavior

Apply this protocol whenever any project-related change occurs during execution. This includes completing tasks, modifying plans, adding or removing features, or altering the conceptual direction of any project.

## 1. Locate the Project Note

Identify the relevant project note inside the Vault. Project notes always have the prefix Project - and end with .md.
- Search for the project note using vault search or file list tools.
- If no matching project note exists, check if this is a sub-task of an existing active project, or create a new project note if appropriate.

## 2. Update Tasks and Checklist Items

When tasks are completed, started, or modified:
- Locate the relevant checkbox or task status indicator within the project note.
- Update the checkbox from uncompleted (e.g., ⬜ Not Started, - [ ]) to completed (e.g., 🟩 Completed (YYYY-MM-DD), - [x]) or in-progress (e.g., ⏳ Workshopping).
- Maintain the existing format of the task list within that specific file.
- If a task is completed, append the completion date in YYYY-MM-DD format (e.g. (2026-05-19) or [2026-05-19]) to improve temporal traceability.

## 3. Update Project Planning and Scope

When conceptual items are added, removed, or changed:
- Update the relevant sections of the project note (such as Objectives, Build Sections, Roadmap Goals, or Proposed Changes).
- Document any shifts in implementation strategy, target dates, or architectural decisions.
- Add new tasks to the task list as they are discovered or planned. Remove or mark obsolete tasks if they are no longer relevant.

## 4. Keep Global Tracking Documents in Sync

Ensure other files that reference this project are also kept up to date:
- If a new project note is created, register it under the Active Projects section of Vault/1. The Core/1.1. Philosophy & Personal North Star/To Do List.md.
- If a project is completed, archived, or no longer needed, run the archive_project protocol to update To Do List.md, Table of Contents.md, and move the project file to its section-specific archive directory.
- Update any MOCs (Map of Content) or higher-level project notes that link to or track the current project.
