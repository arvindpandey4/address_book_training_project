class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        self.contacts.append(Contact(input("First: "), input("Last: ")))

    def delete_contact(self):
        name = input("First name to delete: ")
        for i in range(len(self.contacts)):
            if self.contacts[i].first == name:
                del self.contacts[i]
                print("Deleted")
                return
        print("Not found")


def main():
    print("Welcome to Address Book Program")
    book = AddressBook()
    book.add_contact()
    book.delete_contact()

if __name__ == "__main__":
    main()
