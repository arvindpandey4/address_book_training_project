class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_multiple(self):
        while True:
            self.contacts.append(Contact(input("First: "), input("Last: ")))
            if input("Add more? (y/n): ") != "y":
                break


def main():
    print("Welcome to Address Book Program")
    book = AddressBook()
    book.add_multiple()
    for c in book.contacts:
        print(c.first, c.last)

if __name__ == "__main__":
    main()
