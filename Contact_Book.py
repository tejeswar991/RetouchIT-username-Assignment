import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    # Load contacts from JSON file. returns a dictionary
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME, "r") as f:
            data = f.read().strip()
            if not data:
                return {}
            return json.loads(data)
    except (json.JSONDecodeError, OSError):
        print("contacts.json is invalid...")
        return {}

def save_contacts(contacts):
    # Save contacts dictionary to JSON file.
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(contacts, file, indent=4)
    except OSError:
        print("Error: Could not save contacts to file.")

# Load contacts at start
contacts = load_contacts()

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. View All")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ADD CONTACT
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print("Contact added successfully!")

    # UPDATE CONTACT
    elif choice == "2":
        name = input("Enter name to update: ")

        if name in contacts:
            n_phone = input("Enter new phone: ")
            n_email = input("Enter new email: ")

            contacts[name]["phone"] = n_phone
            contacts[name]["email"] = n_email

            save_contacts(contacts)
            print("Contact updated!")
        else:
            print("Contact not found!")

    # SEARCH CONTACT
    elif choice == "3":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
        else:
            print("Contact not found!")

    # VIEW ALL CONTACTS
    elif choice == "4":
        if not contacts:
            print("No contacts found.")
        else:
            for name, info in contacts.items():
                print(name, "->", info)

    # DELETE CONTACT
    elif choice == "5":
        name = input("Enter name to delete: ")

        if name in contacts:
            contacts.pop(name)
            save_contacts(contacts)
            print("Contact deleted!")
        else:
            print("Contact not found!")

    # EXIT
    elif choice == "6":
        print("Thank you for using the contact manager")
        break

    else:
        print("Invalid choice!")