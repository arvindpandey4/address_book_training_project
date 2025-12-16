class AddressBook:
    def __init__(self):
        self.contacts = []


class AddressBookSystem:
    def __init__(self):
        self.books = {}

    def create_book(self):
        name = input("Book name: ")
        self.books[name] = AddressBook()
        print("Book created")


def main():
    print("Welcome to Address Book Program")
    system = AddressBookSystem()
    system.create_book()

if __name__ == "__main__":
    main()
