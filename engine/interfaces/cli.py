import sys
import argparse
from agents.rag.agent import run_ask_brain

def main():
    """
    CLI Interface for Brain 2.
    """
    # Force UTF-8 output
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(
        description="Brain 2 Engine",
        usage='python engine/main.py "your question" [--domain DOMAIN] [--tag TAG] [--type TYPE]',
    )
    parser.add_argument("query", nargs="+", help="Your question for the brain")
    parser.add_argument("--domain", type=str, default=None,
                        help="Filter by domain (health, career, tech, personal, meta, projects, learning)")
    parser.add_argument("--tag", type=str, default=None,
                        help="Filter by tag substring (e.g. 'medical', 'ai', 'finance')")
    parser.add_argument("--type", type=str, default=None,
                        help="Filter by note type (e.g. 'journal', 'overview', 'workshop')")

    args = parser.parse_args()
    query = " ".join(args.query)

    filters = {}
    if args.domain:
        filters["domain"] = args.domain
    if args.tag:
        filters["tag"] = args.tag
    if args.type:
        filters["type"] = args.type

    run_ask_brain(query, filters=filters if filters else None)

if __name__ == "__main__":
    main()
