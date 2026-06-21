contacts = {}
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
        }
    print("Contact added successfully!\n") 
def view_contacts():
    if not contacts:
        print("No contacts found!\n")
        return
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
def search_contact():
    key = input("Enter name or phone: ")
    found = False
    for name, info in contacts.items():
        if key == name or key == info["phone"]:
            print("\nContact Found:")
            print("Name:", name)
            print("Phone:", info["phone"])
            print("Email:", info["email"])
            print("Address:", info["address"])
            found = True
    if not found:
        print("Contact not found!\n")
def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("New phone: ")
        email = input("New email: ")
        address = input("New address: ")
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact updated!\n")
    else:
        print("Contact not found!\n")
def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted!\n")
    else:
        print("Contact not found!\n")
while True:
    print("=== CONTACT BOOK ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!\n")
