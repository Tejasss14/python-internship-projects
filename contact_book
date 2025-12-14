contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\nSaved Contacts:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")

def search_contact():
    search_name = input("Enter name to search: ")

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print("Contact found:")
            print(contact["name"], "-", contact["phone"])
            return

    print("Contact not found.")

def delete_contact():
    delete_name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == delete_name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return

    print("Contact not found.")

while True:
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please try again.")
