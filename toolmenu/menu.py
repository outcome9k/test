def run_menu():
    import os

    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    RESET = '\033[0m'

    while True:
        os.system("clear")  # Clear screen every time

        print(f"{CYAN}╔════════════════════════╗")
        print(f"║      Tool  Menu        ║")
        print(f"╚════════════════════════╝{RESET}\n")

        print(f"{GREEN}1.{RESET} Black2")
        print(f"{GREEN}2.{RESET} Exit")

        choice = input(f"\n{YELLOW}Choose option: {RESET}")
        
        if choice == '1':
            print(f"\n{CYAN}>> Running Black2...{RESET}")
        elif choice == '2':
            print(f"\n{RED}>> Bye!{RESET}")
            break
        else:
            print(f"\n{RED}Invalid option! Try again.{RESET}")

        input(f"\n{YELLOW}Press Enter to continue...{RESET}")
