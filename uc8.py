class Contact:
    def __init__(self, name, city, state):
        self.name = name
        self.city = city
        self.state = state


class AddressBookSystem:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        self.contacts.append(Contact(
            input("Name: "), input("City: "), input("State: ")
        ))

    def search(self):
        city = input("City to search: ")
        for c in self.contacts:
            if c.city == city:
                print(c.name)


def main():
    print("Welcome to Address Book Program")
    system = AddressBookSystem()
    system.add_contact()
    system.search()

if __name__ == "__main__":
    main()
