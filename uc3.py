class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def display(self):
        print(self.first, self.last)


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        first = input("First name: ")
        last = input("Last name: ")
        self.contacts.append(Contact(first, last))

    def edit_contact(self):
        first = input("First name to edit: ")
        for c in self.contacts:
            if c.first == first:
                c.last = input("New last name: ")
                print("Contact updated")
                return
        print("Contact not found")


def main():
    print("Welcome to Address Book Program")
    book = AddressBook()
    book.add_contact()
    book.edit_contact()

if __name__ == "__main__":
    main()
