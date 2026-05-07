import sys
import os
import argparse

# Add the engine directory to sys.path
engine_dir = os.path.dirname(os.path.abspath(__file__))
if engine_dir not in sys.path:
    sys.path.append(engine_dir)

def main():
    """
    Universal dispatcher for the Brain 2 Engine.
    """
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--voice', action='store_true')
    parser.add_argument('--telegram', action='store_true')
    parser.add_argument('--ingest', action='store_true')
    
    # Peek at args to see if we should dispatch to a specific interface or tool
    args, remaining = parser.parse_known_args()
    
    if args.voice:
        from interfaces.voice import main as voice_main
        voice_main()
    elif args.telegram:
        from interfaces.telegram import main as telegram_main
        telegram_main()
    elif args.ingest:
        # Import the ingest logic
        # Note: ingest_vault.py uses its own argparse, so we'll need to call its main.
        from agents.rag.ingest_vault import main as ingest_main
        # We need to strip the --ingest flag from sys.argv so it doesn't confuse ingest_vault's parser
        sys.argv = [sys.argv[0]] + remaining
        ingest_main()
    else:
        # Default to CLI
        from interfaces.cli import main as cli_main
        cli_main()

if __name__ == "__main__":
    main()
