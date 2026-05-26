"""
vault.py — Vault exploration routes.
Exposes the Vault's structure and note contents over HTTP for the Control Panel.
"""
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

router = APIRouter()


# ── Response Models ───────────────────────────────────────────

class VaultStructureResponse(BaseModel):
    tree: str
    path: str | None


class NoteContentResponse(BaseModel):
    path: str
    content: str


class SearchResult(BaseModel):
    results: str
    keyword: str
    path: str | None


# ── Routes ────────────────────────────────────────────────────

@router.get("/structure", response_model=VaultStructureResponse)
async def get_vault_structure(path: str | None = Query(default=None)):
    """
    Returns an indented tree of the vault directory structure.
    Without a path, returns top-level folders only.
    With a path, returns folders AND files in that subtree.
    """
    try:
        from tools.vault_tools import get_vault_structure as _get_structure

        tree = _get_structure.invoke({"path": path} if path else {})
        return VaultStructureResponse(tree=tree, path=path)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to read vault structure: {str(e)}",
        )


@router.get("/note", response_model=NoteContentResponse)
async def get_note(path: str = Query(..., description="Relative path from Vault root")):
    """
    Reads a specific note's contents from the Vault.
    """
    if not path.strip():
        raise HTTPException(status_code=400, detail="Path cannot be empty.")

    try:
        from tools.vault_tools import read_note as _read_note

        content = _read_note.invoke({"note_path": path})

        if content.startswith("File not found:"):
            raise HTTPException(status_code=404, detail=content)

        return NoteContentResponse(path=path, content=content)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to read note: {str(e)}",
        )


@router.get("/search", response_model=SearchResult)
async def search_vault(
    keyword: str = Query(..., description="Search term"),
    path: str | None = Query(default=None, description="Optional folder scope"),
):
    """
    Searches notes in the vault for a keyword. Optionally scoped to a folder.
    """
    if not keyword.strip():
        raise HTTPException(status_code=400, detail="Keyword cannot be empty.")

    try:
        from tools.vault_tools import search_vault as _search_vault

        args = {"keyword": keyword}
        if path:
            args["path"] = path

        results = _search_vault.invoke(args)
        return SearchResult(results=results, keyword=keyword, path=path)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Search failed: {str(e)}",
        )
