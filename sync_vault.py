"""
sync_vault.py
─────────────
Reads the H1 sections from Vault/Table of Contents.md and ensures
every top-level section has a matching folder in the Vault.

It will:
  • Create any folders that are missing.
  • Normalise .gitkeep — add to any empty folder that lacks one.
  • Remove stale .gitkeep files from folders that now contain real notes.
  • Report any folders that exist but have no matching H1 (possible renames).
  • Never delete or rename anything automatically.

Usage:
    python sync_vault.py
"""

import re
import sys
from pathlib import Path

# ─── Paths ───────────────────────────────────────────────────────────────────
REPO_DIR = Path(__file__).parent
VAULT_DIR = REPO_DIR / "Vault"
TOC_FILE  = VAULT_DIR / "Table of Contents.md"

# Folders inside Vault that are never "content" folders — always ignored
IGNORED_FOLDERS = {"Audio", "zImages"}

# ─── Helpers ─────────────────────────────────────────────────────────────────

def parse_h1_sections(toc_text: str) -> list[str]:
    """Extract top-level (H1) section names from the TOC, stripping the
    leading '# ' prefix.  YAML front-matter is automatically skipped."""

    # Strip YAML front-matter
    toc_text = re.sub(r"^---\n.*?\n---\n", "", toc_text, flags=re.DOTALL)

    folders = []
    for line in toc_text.splitlines():
        # Match ONLY H1 lines: one '#' followed by a space
        if re.match(r"^# .+", line):
            folder_name = line[2:].strip()
            folders.append(folder_name)
    return folders


def current_vault_folders() -> set[str]:
    """Return names of all immediate subdirectories of the Vault,
    minus the ignored system folders."""
    return {
        item.name
        for item in VAULT_DIR.iterdir()
        if item.is_dir() and item.name not in IGNORED_FOLDERS
    }


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    # Ensure emoji/unicode prints correctly on Windows terminals
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print("🔍  Reading Table of Contents...")

    if not TOC_FILE.exists():
        print(f"[!] Cannot find Table of Contents at: {TOC_FILE}")
        return

    toc_text = TOC_FILE.read_text(encoding="utf-8")
    expected = parse_h1_sections(toc_text)

    if not expected:
        print("[!] No H1 sections found in Table of Contents. Nothing to do.")
        return

    print(f"    Found {len(expected)} top-level section(s) in the TOC.\n")

    existing = current_vault_folders()
    expected_set = set(expected)

    created     = []
    discrepancies = []

    # ── Create missing folders ────────────────────────────────────────────────
    for folder_name in expected:
        folder_path = VAULT_DIR / folder_name
        if not folder_path.exists():
            folder_path.mkdir(parents=True)
            # Create a .gitkeep so Git tracks the empty folder
            (folder_path / ".gitkeep").touch()
            created.append(folder_name)
            print(f"  ✅  Created: {folder_name}/")

    # ── Normalise .gitkeep across ALL existing empty folders ────────────────
    normalised = []
    for folder in VAULT_DIR.iterdir():
        if not folder.is_dir() or folder.name in IGNORED_FOLDERS:
            continue
        contents = [f for f in folder.iterdir() if f.name != ".gitkeep"]
        gitkeep  = folder / ".gitkeep"
        if not contents and not gitkeep.exists():
            # Empty with no .gitkeep — add one
            gitkeep.touch()
            normalised.append(("added", folder.name))
            print(f"  📌  Added .gitkeep to existing empty folder: {folder.name}/")
        elif contents and gitkeep.exists():
            # Has real content — .gitkeep is now stale, remove it
            gitkeep.unlink()
            normalised.append(("removed", folder.name))
            print(f"  🧹  Removed stale .gitkeep from: {folder.name}/")

    # ── Detect extras (possible renames / obsolete folders) ───────────────────
    for existing_folder in sorted(existing):
        if existing_folder not in expected_set:
            discrepancies.append(existing_folder)

    # ── Summary ───────────────────────────────────────────────────────────────
    print()
    if not created and not discrepancies and not normalised:
        print("✨  Vault structure is already in sync with the Table of Contents.")
        return

    if created:
        print(f"✅  Created {len(created)} new folder(s).")

    if normalised:
        added   = sum(1 for t, _ in normalised if t == "added")
        removed = sum(1 for t, _ in normalised if t == "removed")
        if added:   print(f"📌  Added .gitkeep to {added} previously untracked empty folder(s).")
        if removed: print(f"🧹  Removed stale .gitkeep from {removed} folder(s) that now have content.")

    if discrepancies:
        print("\n⚠️   The following folders exist in Vault but have NO matching H1 in the TOC:")
        for name in discrepancies:
            print(f"      • {name}")
        print("\n    These may be renamed sections or obsolete folders.")
        print("    Please review and let your AI agent know if any should be renamed or removed.")


if __name__ == "__main__":
    main()
