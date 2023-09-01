address_book = {}  # Store contacts as a dictionary with names as keys

def add_contact(name, phone, email, group):

    # Check for duplicate contacts
    if name in address_book:
        print(f"{name} already exists in the address book.")
    else:
        address_book[name] = {'Phone': phone, 'Email': email, 'Group': group}
        print(f"Contact {name} added successfully.")

def search_contact(name):
    if name in address_book:
        contact_info = address_book[name]
        print('-' * 20)
        print(f"Name: {name}")
        print(f"Phone: {contact_info['Phone']}")
        print(f"Email: {contact_info['Email']}")
        print(f"Group: {contact_info['Group']}")
        print('-' * 20)
    else:
        print('-' * 20)
        print(f"{name} not found in the address book.")
        print('-' * 20)

def display_contacts():
    if not address_book:
        print("Address book is empty.")
    else:
        print("Contacts:")
        print('-' * 20)
        for name, info in address_book.items():
            print(f"Name: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Group: {info['Group']}")
            print('-' * 20)

def display_group(group):
    group_contacts = [name for name, info in address_book.items() if info['Group'] == group]
    if group_contacts:
        print('-' * 20)
        print(f"Contacts in group '{group}':")
        for name in group_contacts:
            print(name)
        print('-' * 20)
    else:
        print('-' * 20)
        print(f"No contacts found in group '{group}'.")
        print('-' * 20)

while True:
    print('-' * 20)
    print("\nOptions:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display Contacts")
    print("4. Display Contacts in a Group")
    print("5. Quit\n")
    print('-' * 20)

    choice = input("\nEnter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        group = input("Enter group: ")
        add_contact(name, phone, email, group)
    elif choice == '2':
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == '3':
        display_contacts()
    elif choice == '4':
        group = input("Enter group to display contacts: ")
        display_group(group)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
