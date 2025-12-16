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
        print("Contact added")


def main():
    print("Welcome to Address Book Program")
    book = AddressBook()
    book.add_contact()
    for c in book.contacts:
        c.display()

if __name__ == "__main__":
    main()

