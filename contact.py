class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        if name in self.contacts:
            print("Contact with this name already exists. Use a different name.")
        else:
            self.contacts[name] = {"phone_number": phone_number, "email": email, "address": address}
            print("Contact added successfully.")

    def view_contact_list(self):
        print("\nContact List:")
        print("--------------")
        for name, contact_info in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone Number: {contact_info['phone_number']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            print("--------------")

    def search_contact(self, query):
        results = []
        for name, contact_info in self.contacts.items():
            if query.lower() in name.lower() or query in contact_info["phone_number"]:
                results.append((name, contact_info))
        return results

    def update_contact(self, name, phone_number=None, email=None, address=None):
        if name in self.contacts:
            if phone_number:
                self.contacts[name]["phone_number"] = phone_number
            if email:
                self.contacts[name]["email"] = email
            if address:
                self.contacts[name]["address"] = address
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter the address: ")
            contact_manager.add_contact(name, phone_number, email, address)

        elif choice == "2":
            contact_manager.view_contact_list()

        elif choice == "3":
            query = input("Enter the name or phone number to search: ")
            results = contact_manager.search_contact(query)
            if results:
                print("\nSearch Results:")
                for name, contact_info in results:
                    print(f"Name: {name}")
                    print(f"Phone Number: {contact_info['phone_number']}")
                    print(f"Email: {contact_info['email']}")
                    print(f"Address: {contact_info['address']}")
                    print("--------------")
            else:
                print("No contacts found.")

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            phone_number = input("Enter the new phone number (press Enter to keep the same): ")
            email = input("Enter the new email (press Enter to keep the same): ")
            address = input("Enter the new address (press Enter to keep the same): ")
            contact_manager.update_contact(name, phone_number, email, address)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == "6":
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
