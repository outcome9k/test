def run_menu():
    print("== Tool Menu ==")
    print("1. Black2")
    print("2. Exit")

    while True:
        choice = input("Choose option: ")
        if choice == '1':
            print("Running Black2...")
        elif choice == '2':
            print("Bye!")
            break
        else:
            print("Invalid")
