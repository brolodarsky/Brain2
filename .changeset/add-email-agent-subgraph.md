---
type: minor
---
### Added
- Created the **Email Agent** compiled LangGraph subgraph under `engine/agents/email/` to fetch and search IMAP emails.
- Added `search_emails` tool to `engine/agents/email/tools.py`.
- Established the Email Agent Golden Dataset evaluation suite in `engine/agents/email/evals/`.
- Added 5 new evaluation cases to the Career Agent dataset in `engine/agents/career/evals/dataset.json`.

### Changed
- Migrated `engine/tools/email_tool.py` to `engine/agents/email/tools.py`.
- Refactored **Content Router** (`engine/agents/router/agent.py`) into a ReAct agent to support `fetch_emails` tool calling prior to classification.
- Updated `tools/read_email.py` to import from the new agent tools module.
