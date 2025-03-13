# Contact manager application

def add_contact(contacts, name, phone, email):
    for contact in contacts:
        if contact[0] == name:
            print("Contact with this name already exists!")
            return
    contacts.append((name, phone, email))
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\nList of Contacts:")
    print(f"{'Name':<20} {'Phone Number':<15} {'Email':<30}")
    print("-" * 65)
    for contact in contacts:
        print(f"{contact[0]:<20} {contact[1]:<15} {contact[2]:<30}")

def search_contact(contacts, name):
    for contact in contacts:
        if contact[0] == name:
            print(f"Contact Found:\n{'Name':<20} {contact[0]}\n{'Phone Number':<20} {contact[1]}\n{'Email':<20} {contact[2]}")
            return
    print("Contact not found!")

def update_contact(contacts, name, new_phone):
    for i, contact in enumerate(contacts):
        if contact[0] == name:
            contacts[i] = (name, new_phone, contact[2])
            print("Contact updated successfully!")
            return
    print("Contact not found!")

def delete_contact(contacts, name):
    for i, contact in enumerate(contacts):
        if contact[0] == name:
            del contacts[i]
            print("Contact deleted successfully!")
            return
    print("Contact not found!")

def main():
    contacts = []
    while True:
        print("\nWelcome to Contact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            add_contact(contacts, name, phone, email)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(contacts, name)
        elif choice == "4":
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone number: ")
            update_contact(contacts, name, new_phone)
        elif choice == "5":
            name = input("Enter name to delete: ")
            delete_contact(contacts, name)
        elif choice == "6":
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

---------------------------------------------------------------------------------------------------------------
Output-


Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 1 
Enter Name: Sakshi Wagh
Enter Phone Number: 8477890345
Enter Email: sakshivwagh@gmail.com
Contact added successfully!

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 2

List of Contacts:
Name                 Phone Number    Email
-----------------------------------------------------------------
Mayra Zagade         3456789012      mayra@gmail.com
Sakshi Wagh          8477890345      sakshivwagh@gmail.com

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 3
Enter name to search: Sakshi Wagh
Contact Found:
Name                 Sakshi Wagh
Phone Number         8477890345
Email                sakshivwagh@gmail.com

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 4
Enter name to update: Sakshi Wagh
Enter new phone number: 2345678901
Contact updated successfully!

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 5
Enter name to delete: Sakshi Wagh
Contact deleted successfully!

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 6
Exiting Contact Manager. Goodbye!
