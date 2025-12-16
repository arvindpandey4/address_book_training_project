class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def same(self, other):
        return self.first.lower() == other.first.lower()


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        c = Contact(input("First: "), input("Last: "))
        for existing in self.contacts:
            if existing.same(c):
                print("Duplicate found")
                return
        self.contacts.append(c)
        print("Contact added")


def main():
    print("Welcome to Address Book Program")
    book = AddressBook()
    book.add_contact()
    book.add_contact()

if __name__ == "__main__":
    main()
