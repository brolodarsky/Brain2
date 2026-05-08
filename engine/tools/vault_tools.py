import os
import sys
from pathlib import Path
from langchain_core.tools import tool

# Determine Vault root path dynamically
ENGINE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = ENGINE_DIR.parent
VAULT_ROOT = PROJECT_ROOT / "Vault"

@tool
def read_toc() -> str:
    """Reads the Table of Contents.md file to understand the folder structure of the Vault."""
    toc_path = VAULT_ROOT / "Table of Contents.md"
    try:
        with open(toc_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading Table of Contents: {str(e)}"

@tool
def read_note(note_path: str) -> str:
    """Reads the contents of a specific note or file in the Vault. Provide the relative path from the Vault root, or just the note name if it's unique."""
    if os.path.isabs(note_path):
        target_path = Path(note_path)
    else:
        target_path = VAULT_ROOT / note_path
        if not target_path.exists():
            if not target_path.name.endswith('.md'):
                target_path = target_path.with_suffix('.md')
            
    if target_path.exists() and target_path.is_file():
        try:
            with open(target_path, 'r', encoding='utf-8') as f:
                try:
                    rel_path = target_path.relative_to(VAULT_ROOT)
                except ValueError:
                    rel_path = target_path
                return f"--- File: {rel_path} ---\n\n" + f.read()
        except Exception as e:
            return f"Error reading file {note_path}: {str(e)}"
    
    # If not found directly, try to search for the file in the Vault by note name
    base_name = os.path.basename(note_path)
    if not base_name.endswith('.md'):
        base_name += '.md'
        
    found_paths = []
    for root, dirs, files in os.walk(VAULT_ROOT):
        if '.git' in dirs:
            dirs.remove('.git')
            
        for file in files:
            if file == base_name or file == os.path.basename(note_path):
                found_paths.append(Path(root) / file)
                
    if not found_paths:
        return f"File not found: {note_path}. Try using search_vault."
    elif len(found_paths) == 1:
        try:
            with open(found_paths[0], 'r', encoding='utf-8') as f:
                rel_path = found_paths[0].relative_to(VAULT_ROOT)
                return f"--- File: {rel_path} ---\n\n" + f.read()
        except Exception as e:
            return f"Error reading file {found_paths[0]}: {str(e)}"
    else:
        rel_paths = [str(p.relative_to(VAULT_ROOT)) for p in found_paths]
        return f"Multiple files found for {note_path}. Please be more specific. Matches:\n" + "\n".join(rel_paths)

@tool
def search_vault(keyword: str) -> str:
    """Searches across all notes in the vault for a specific string keyword. Returns the file paths and context of the matches."""
    results = []
    keyword_lower = keyword.lower()
    
    for root, dirs, files in os.walk(VAULT_ROOT):
        if '.git' in dirs:
            dirs.remove('.git')
        
        for file in files:
            if not file.endswith('.md'):
                continue
                
            path = Path(root) / file
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                if keyword_lower in content.lower():
                    idx = content.lower().find(keyword_lower)
                    start = max(0, idx - 40)
                    end = min(len(content), idx + len(keyword) + 40)
                    snippet = content[start:end].replace('\n', ' ')
                    
                    rel_path = path.relative_to(VAULT_ROOT)
                    results.append(f"- {rel_path}: \"...{snippet}...\"")
            except Exception:
                pass
                
    if not results:
        return f"No results found for keyword: {keyword}"
        
    output = f"Found '{keyword}' in {len(results)} files:\n"
    for r in results[:20]:
        output += f"{r}\n"
    if len(results) > 20:
        output += f"...and {len(results)-20} more files."
        
    return output
