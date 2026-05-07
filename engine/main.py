import sys
import os
import argparse
import threading
import logging
import time

# Add the engine directory to sys.path
engine_dir = os.path.dirname(os.path.abspath(__file__))
if engine_dir not in sys.path:
    sys.path.append(engine_dir)

from agents.rag.agent import run_ask_brain

# Disable noisy logs
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger('telegram').setLevel(logging.WARNING)

BOT_ONLINE = False

def start_telegram_interface():
    """Starts the telegram bot listener."""
    global BOT_ONLINE
    try:
        from interfaces.telegram import main as telegram_main
        BOT_ONLINE = True
        telegram_main()
    except Exception as e:
        BOT_ONLINE = False
        # Silent failure for background thread, we'll see it in status

def print_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("  " + "═" * 45)
    print("  ║" + " " * 12 + "🧠 BRAIN 2.0 ENGINE" + " " * 13 + "║")
    print("  " + "═" * 45)
    status = "🟢 ONLINE" if BOT_ONLINE else "⏳ STARTING"
    print(f"  [ Telegram Bot: {status} ]\n")

def show_menu():
    print("  1. 💬  Ask Brain (Text)")
    print("  2. 🎙️   Voice Query (Mic)")
    print("  3. 📥  Ingest Vault (Update Index)")
    print("  4. 🧹  Cleanup Orphans")
    print("  5. ❌  Exit")
    print("\n  " + "─" * 45)

def main():
    """
    Enduring terminal menu coordinator for the Brain 2 Engine.
    """
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--no-bot', action='store_true')
    args, remaining = parser.parse_known_args()

    # 1. Start Telegram Bot in background
    if not args.no_bot:
        threading.Thread(target=start_telegram_interface, daemon=True).start()

    # 2. If a query was passed directly via CLI, run it and exit
    if remaining:
        query = " ".join(remaining)
        run_ask_brain(query)
        return

    # 3. Otherwise, enter the persistent menu
    while True:
        print_header()
        show_menu()
        
        choice = input("  Select option [1-5] » ").strip()

        if choice == '1':
            query = input("\n  💬 Query: ")
            if query.strip():
                print("\n" + "─" * 45)
                run_ask_brain(query)
                input("\n  Press Enter to return to menu...")
        
        elif choice == '2':
            print("\n  🎙️ Starting local voice capture...")
            from interfaces.voice import main as voice_main
            voice_main()
            input("\n  Press Enter to return to menu...")
            
        elif choice == '3':
            print("\n  📥 Running ingestion...")
            from agents.rag.ingest_vault import main as ingest_main
            # Clear sys.argv to avoid confusing ingest_vault's parser
            old_argv = sys.argv
            sys.argv = [sys.argv[0]]
            try:
                ingest_main()
            finally:
                sys.argv = old_argv
            input("\n  Press Enter to return to menu...")

        elif choice == '4':
            print("\n  🧹 Cleaning orphans from vector store...")
            from agents.rag.ingest_vault import main as ingest_main
            old_argv = sys.argv
            sys.argv = [sys.argv[0], "--cleanup"]
            try:
                ingest_main()
            finally:
                sys.argv = old_argv
            input("\n  Press Enter to return to menu...")

        elif choice == '5' or choice.lower() in ['exit', 'q', 'quit']:
            print("\n  👋 Shutting down Brain 2.0. See you in the vault.")
            time.sleep(1)
            break
        
        else:
            print("  ⚠️ Invalid choice.")
            time.sleep(1)

if __name__ == "__main__":
    main()
