
class Contact:
    def __init__(self, first, last, address, city, state, zip_code, phone, email):
        self.first = first
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code
        self.phone = phone
        self.email = email

    def full_name(self):
        return self.first.lower(), self.last.lower()

    def display(self):
        return f"{self.first} {self.last} | {self.address} | {self.city} | {self.state} | {self.zip} | {self.phone} | {self.email}"

    # UC7
    def is_same_person(self, other):
        return self.first.lower() == other.first.lower() and self.last.lower() == other.last.lower()


class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    # UC7
    def has_contact(self, contact):
        for c in self.contacts:
            if c.is_same_person(contact):
                return True
        return False

    # UC2
    def add_contact(self, contact):
        if self.has_contact(contact):
            print("Duplicate entry found. Contact not added.")
            return
        self.contacts.append(contact)
        print("Contact added successfully.")

    # UC3
    def edit_contact(self, first, last):
        for c in self.contacts:
            if c.first.lower() == first.lower() and c.last.lower() == last.lower():
                while True:
                    print("1.First 2.Last 3.Address 4.City 5.State 6.Zip 7.Phone 8.Email 9.Done")
                    ch = input("Choose field: ")
                    if ch == "1":
                        c.first = input("New first name: ")
                    elif ch == "2":
                        c.last = input("New last name: ")
                    elif ch == "3":
                        c.address = input("New address: ")
                    elif ch == "4":
                        c.city = input("New city: ")
                    elif ch == "5":
                        c.state = input("New state: ")
                    elif ch == "6":
                        c.zip = input("New zip: ")
                    elif ch == "7":
                        c.phone = input("New phone: ")
                    elif ch == "8":
                        c.email = input("New email: ")
                    elif ch == "9":
                        break
                    else:
                        print("Invalid option")
                print("Contact updated.")
                return
        print("Contact not found.")

    # UC4
    def delete_contact(self, first, last):
        for i in range(len(self.contacts)):
            c = self.contacts[i]
            if c.first.lower() == first.lower() and c.last.lower() == last.lower():
                del self.contacts[i]
                print("Contact deleted.")
                return
        print("Contact not found.")

    # UC5
    def add_multiple(self):
        while True:
            contact = read_contact_from_console()
            self.add_contact(contact)
            more = input("Add another? (y/n): ").lower()
            if more != "y":
                break

    def show_contacts(self):
        if not self.contacts:
            print("No contacts.")
            return
        for c in self.contacts:
            print(c.display())


class AddressBookSystem:
    def __init__(self):
        self.books = {}
        self.books["master"] = AddressBook("master")  # UC6

    # UC8
    def search_by_city_state(self):
        choice = input("Search by city or state: ").lower()
        value = input("Enter value: ").lower()
        found = False

        for book in self.books.values():
            for c in book.contacts:
                if choice == "city" and c.city.lower() == value:
                    print(book.name, "->", c.display())
                    found = True
                if choice == "state" and c.state.lower() == value:
                    print(book.name, "->", c.display())
                    found = True

        if not found:
            print("No contacts found.")

    # UC9
    def view_by_city_state(self):
        city_map = {}
        state_map = {}

        for book in self.books.values():
            for c in book.contacts:
                city_map.setdefault(c.city, []).append(c)
                state_map.setdefault(c.state, []).append(c)

        print("\nPersons by City")
        for city in city_map:
            print(city)
            for c in city_map[city]:
                print(" ", c.display())

        print("\nPersons by State")
        for state in state_map:
            print(state)
            for c in state_map[state]:
                print(" ", c.display())

    # UC10
    def count_by_city_state(self):
        city_count = {}
        state_count = {}

        for book in self.books.values():
            for c in book.contacts:
                city_count[c.city] = city_count.get(c.city, 0) + 1
                state_count[c.state] = state_count.get(c.state, 0) + 1

        print("\nCount by City")
        for city in city_count:
            print(city, ":", city_count[city])

        print("\nCount by State")
        for state in state_count:
            print(state, ":", state_count[state])


def read_contact_from_console():
    first = input("First name: ")
    last = input("Last name: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("Zip: ")
    phone = input("Phone: ")
    email = input("Email: ")
    return Contact(first, last, address, city, state, zip_code, phone, email)


def open_address_book(book):
    while True:
        print("\nAddress Book:", book.name)
        print("1.Show 2.Add 3.Edit 4.Delete 5.Add Multiple 6.Back")
        ch = input("Choice: ")

        if ch == "1":
            book.show_contacts()
        elif ch == "2":
            contact = read_contact_from_console()
            book.add_contact(contact)
        elif ch == "3":
            first = input("First name: ")
            last = input("Last name: ")
            book.edit_contact(first, last)
        elif ch == "4":
            first = input("First name: ")
            last = input("Last name: ")
            book.delete_contact(first, last)
        elif ch == "5":
            book.add_multiple()
        elif ch == "6":
            break
        else:
            print("Invalid option")


def main():
    print("Welcome to Address Book Program")  # UC1
    system = AddressBookSystem()

    while True:
        print("\nMain Menu")
        print("1.Open Book 2.Create Book 3.List Books 4.Search 5.View City/State 6.Count 7.Exit")
        ch = input("Choice: ")

        if ch == "1":
            name = input("Book name: ")
            if name in system.books:
                open_address_book(system.books[name])
            else:
                print("Address book not found.")
        elif ch == "2":
            name = input("New book name: ")
            if name in system.books:
                print("Already exists.")
            else:
                system.books[name] = AddressBook(name)
                print("Address book created.")
        elif ch == "3":
            for b in system.books:
                print("-", b)
        elif ch == "4":
            system.search_by_city_state()  # UC8
        elif ch == "5":
            system.view_by_city_state()  # UC9
        elif ch == "6":
            system.count_by_city_state()  # UC10
        elif ch == "7":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
