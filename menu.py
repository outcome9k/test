def run_menu():
    print("Welcome to the TOOL MENU!")
    print("1. Black2")
    print("2. Kramer")
    print("3. Exit")

    while True:
        choice = input("Choose: ")
        if choice == '1':
            print("Running Black2...")
        elif choice == '2':
            print("Running Kramer...")
        elif choice == '3':
            print("Bye!")
            break
        else:
            print("Invalid!")