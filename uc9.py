class Contact:
    def __init__(self, name, city, state):
        self.name = name
        self.city = city
        self.state = state


def main():
    contacts = []
    contacts.append(Contact("A", "Bangalore", "KA"))
    contacts.append(Contact("B", "Chennai", "TN"))

    city_map = {}
    for c in contacts:
        city_map.setdefault(c.city, []).append(c.name)

    for city in city_map:
        print(city, city_map[city])

if __name__ == "__main__":
    main()
