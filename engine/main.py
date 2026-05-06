import sys
import urllib.parse
from langchain_core.messages import HumanMessage
from core.constants import CHROMA_PATH
from agents.rag.graph import build_rag_graph

# Force UTF-8 output
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def execute_rag_query(query: str, thread_id: str = None) -> dict:
    """
    Core function to execute the RAG LangGraph agent and return the final state.
    """
    app = build_rag_graph()
    
    config = {}
    if thread_id:
        config["configurable"] = {"thread_id": thread_id}
        
    initial_state = {
        "messages": [HumanMessage(content=query)],
        "context": [],
        "sources": [],
    }
    
    return app.invoke(initial_state, config=config)

def run_ask_brain(query: str):
    """
    CLI Wrapper: Executes the RAG agent and prints the output to stdout.
    """
    print(f"\n[Brain 2] Query: {query}\n")
    
    final_state = execute_rag_query(query)
    answer = final_state["messages"][-1].content
    
    print("=" * 60)
    print(answer)
    print("=" * 60)
    
    if final_state["sources"]:
        vault_name = urllib.parse.quote(CHROMA_PATH.parent.name)
        print("\n[Sources]")
        for src in dict.fromkeys(final_state["sources"]):
            encoded = urllib.parse.quote(src.replace("\\", "/"))
            obsidian_link = f"obsidian://open?vault={vault_name}&file={encoded}"
            print(f"  - {src}")
            print(f"    {obsidian_link}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python engine/main.py \"<your question>\"")
        sys.exit(1)
        
    query = " ".join(sys.argv[1:])
    
    # In the future, we can add a dispatcher here to choose different agents
    # based on query classification or flags.
    run_ask_brain(query)

if __name__ == "__main__":
    main()
