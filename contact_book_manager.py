contacts = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")
    contacts[name] = number
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, number in contacts.items():
            print(f"{name}: {number}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
