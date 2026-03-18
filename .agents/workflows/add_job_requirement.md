---
description: Automates the extraction of skills from job descriptions, adds them to the Employer Skill Requirements note, and updates the AI summary.
---

# Workflow: Add Job Requirement (`/add_job_requirement`)

This workflow automates the process of extracting job requirements from a source (URL, PDF, or raw text) and adding them to the centralized tracking note.

## Trigger
When asked to "parse this job", "add this job requirement", or when explicitly invoking `/add_job_requirement [source]`.

## Steps

1. **Extract Information:**
   - Read the provided source (PDF using `view_file` or `read_url_content`, etc.).
   - Extract the following fields: Role Name, Company, Core Requirements, Preferred Background, and any compensation/bonus information.

2. **Format the Entry:**
   - Format the extracted information into a markdown section:
     ```markdown
     ## [Role Name] - [Company]
     - **Source:** [Link or File Reference]
     - **Date Added:** [Current Date]
     - **Desired Background and Skills:**
         - [Skill 1]
         - [Skill 2]
         ...
     ```

3. **Update the Note (`Vault/4. Operations & Wealth/4.3. Career Strategy & Revenue/Employer Skill Requirements.md`):**
   - Append or insert the newly formatted entry into the `# 📋 Roles & Requirements` section.

4. **Regenerate the AI Summary:**
   - Read the entirety of the `# 📋 Roles & Requirements` section.
   - Synthesize the common themes, required degrees, prominent languages/frameworks, and domain knowledge.
   - Replace the contents of the `# 🤖 AI Summary` section with the newly generated synthesis.

5. **Commit Changes:**
   - Group the changes into a single conventional commit (e.g., `feat(career): add [Company] requirements and refresh summary`).
