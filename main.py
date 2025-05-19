import functions

def show_menu():
    print("\n=== Veterinary Clinic - Main Menu ===")
    print("1. Register pet")
    print("2. Register consultation")
    print("3. List pets")
    print("4. View consultation history of a pet")
    print("5. Exit")

def main():
    while True:
        show_menu()
        option = input("Select an option: ")
        if option == "1":
            functions.register_pet()
        elif option == "2":
            functions.register_consultation()
        elif option == "3":
            functions.list_pets()
        elif option == "4":
            functions.view_pet_history()
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()