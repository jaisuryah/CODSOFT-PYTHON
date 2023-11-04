class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for index, contact in enumerate(self.contacts):
                print(f"{index + 1}. {contact.name} - {contact.phone_number}")
        else:
            print("Contact list is empty.")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if
                          search_term.lower() in contact.name.lower() or search_term in contact.phone_number]
        if found_contacts:
            print("Matching Contacts:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("No matching contacts found.")

    def update_contact(self, index, new_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = new_contact
            print(f"Contact {index + 1} updated.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print(f"Contact {index + 1} deleted.")
        else:
            print("Invalid contact index.")

def main():
    contact_book = ContactBook()

    # Adding sample contacts to the contact book
    contact_book.add_contact(Contact("RAMESH", "1234567890", "ramesh@example.com", "123 Main St"))
    contact_book.add_contact(Contact("RAM", "9876543210", "ram@example.com", "456 Elm St"))

    while True:
        print("\nContact Management System")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            contact_book.view_contacts()
        elif choice == '2':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(Contact(name, phone, email, address))
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            index = int(input("Enter the index of contact to update: ")) - 1
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.update_contact(index, Contact(name, phone, email, address))
        elif choice == '5':
            index = int(input("Enter the index of contact to delete: ")) - 1
            contact_book.delete_contact(index)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
