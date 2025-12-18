# Address Book Training Project

A comprehensive training project demonstrating Object-Oriented Programming concepts in Python through the development of an Address Book system.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Use Cases (UC1-UC10)](#use-cases)
- [Review Sessions](#review-sessions)
- [Main Implementation](#main-implementation)
- [File Structure](#file-structure)

---

## Project Overview

This project implements a progressive learning path for building an Address Book application with incrementally increasing complexity. Each use case builds upon the previous knowledge and introduces new programming concepts.

---

## Use Cases

### UC1: Basic Contact Creation
**File:** `uc1.py`

**Description:** Creates a simple Contact and AddressBook class with basic input/output functionality.

**Key Concepts:**
- Basic class definition
- Object instantiation
- Simple methods
- User input handling

**Features:**
- Create a Contact with first and last name
- Create an AddressBook
- Add a single contact
- Display contact information

**Sample Code:**
```python
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
```

---

### UC2: Add Multiple Contacts with Validation
**File:** `uc2.py`

**Description:** Extends UC1 to handle adding multiple contacts and validate for duplicates.

**Key Concepts:**
- List operations
- Duplicate checking
- Conditional logic
- Loop structures

**Features:**
- Add multiple contacts in one session
- Check for duplicate entries before adding
- Prevent duplicate contacts in the address book

**Sample Code:**
```python
def add_contact(self):
    c = Contact(input("First: "), input("Last: "))
    for existing in self.contacts:
        if existing.same(c):
            print("Duplicate found")
            return
    self.contacts.append(c)
    print("Contact added")
```

---

### UC3: Edit Contact Information
**File:** `uc3.py`

**Description:** Adds functionality to edit existing contacts.

**Key Concepts:**
- Searching through collections
- Updating object attributes
- User menu systems

**Features:**
- Search for a contact by first name
- Edit contact details
- Handle case where contact is not found

**Sample Code:**
```python
def edit_contact(self):
    first = input("First name to edit: ")
    for c in self.contacts:
        if c.first == first:
            c.last = input("New last name: ")
            print("Contact updated")
            return
    print("Contact not found")
```

---

### UC4: Delete Contact
**File:** `uc4.py`

**Description:** Implements contact deletion functionality.

**Key Concepts:**
- List removal operations
- Index-based removal
- Error handling

**Features:**
- Search for a contact by name
- Delete the contact if found
- Display appropriate messages

**Sample Code:**
```python
def delete_contact(self):
    name = input("First name to delete: ")
    for i in range(len(self.contacts)):
        if self.contacts[i].first == name:
            del self.contacts[i]
            print("Deleted")
            return
    print("Not found")
```

---

### UC5: Add Multiple Contacts with Loop
**File:** `uc5.py`

**Description:** Enhances adding multiple contacts with a loop-based approach.

**Key Concepts:**
- While loops
- User-controlled iteration
- Batch operations

**Features:**
- Add multiple contacts in a continuous loop
- User decides when to stop adding
- Display all added contacts

**Sample Code:**
```python
def add_multiple(self):
    while True:
        self.contacts.append(Contact(input("First: "), input("Last: ")))
        if input("Add more? (y/n): ") != "y":
            break
```

---

### UC6: Create Multiple Address Books
**File:** `uc6.py`

**Description:** Introduces the concept of managing multiple address books.

**Key Concepts:**
- Dictionary usage
- System-level architecture
- Multiple object instances

**Features:**
- Create multiple named address books
- Store address books in a system-level container
- Support for multiple users or categories

**Sample Code:**
```python
class AddressBookSystem:
    def __init__(self):
        self.books = {}

    def create_book(self):
        name = input("Book name: ")
        self.books[name] = AddressBook()
        print("Book created")
```

---

### UC7: Duplicate Check by Full Name
**File:** `uc7.py`

**Description:** Implements proper duplicate detection using both first and last names.

**Key Concepts:**
- Composite key checking
- Case-insensitive comparison
- Better duplicate detection

**Features:**
- Check duplicates by both first and last name
- Case-insensitive duplicate detection
- More robust validation

**Sample Code:**
```python
def same(self, other):
    return self.first.lower() == other.first.lower()

def add_contact(self):
    c = Contact(input("First: "), input("Last: "))
    for existing in self.contacts:
        if existing.same(c):
            print("Duplicate found")
            return
    self.contacts.append(c)
    print("Contact added")
```

---

### UC8: Search by City
**File:** `uc8.py`

**Description:** Adds location-based search functionality.

**Key Concepts:**
- Attribute-based filtering
- Search operations
- Contact details expansion

**Features:**
- Search contacts by city
- Display contacts from a specific city
- Support for city and state attributes

**Sample Code:**
```python
class Contact:
    def __init__(self, name, city, state):
        self.name = name
        self.city = city
        self.state = state

def search(self):
    city = input("City to search: ")
    for c in self.contacts:
        if c.city == city:
            print(c.name)
```

---

### UC9: View Contacts by City
**File:** `uc9.py`

**Description:** Groups and displays all contacts organized by city.

**Key Concepts:**
- Dictionary-based grouping
- Data organization
- setdefault() method

**Features:**
- Group contacts by city
- Display city-wise contact lists
- Efficient city-to-contacts mapping

**Sample Code:**
```python
def main():
    contacts = []
    contacts.append(Contact("A", "Bangalore", "KA"))
    contacts.append(Contact("B", "Chennai", "TN"))

    city_map = {}
    for c in contacts:
        city_map.setdefault(c.city, []).append(c.name)

    for city in city_map:
        print(city, city_map[city])
```

---

### UC10: Advanced Fare Calculation System
**File:** `uc10.py`

**Description:** A ride-sharing fare calculation system with dynamic pricing based on time and distance.

**Key Concepts:**
- Complex business logic
- Conditional pricing
- Time-based calculations
- Real-world application

**Features:**
- Calculate base fare
- Apply time-based surge pricing (peak hours 8-10 AM, 6-9 PM)
- Apply night surcharge (after 11 PM or before 5 AM)
- Apply maximum fare cap (₹1000)
- Dynamic pricing based on distance and time

**Pricing Formula:**
- Base Fare: ₹50
- Per km charge: ₹12/km
- Peak hours (8-10 AM, 6-9 PM): 1.5x multiplier
- Night hours (11 PM - 5 AM): +₹100 surcharge
- Maximum cap: ₹1000

**Sample Code:**
```python
class Ride:
    def __init__(self, distance, start_time):
        self.distance = distance
        self.start_time = start_time
    
    def calculate_fare(self):
        base_fare = 50
        per_km_fare = 12
        final_fare = base_fare + (self.distance * per_km_fare)

        hr = int(self.start_time.split(":")[0])

        if (8 <= hr < 10) or (18 <= hr < 21):
            final_fare = final_fare * 1.5
        
        if (hr >= 23) or (hr < 5):
            final_fare = final_fare + 100
        
        if final_fare > 1000:
            final_fare = 1000
        
        return final_fare
```

---

## Review Sessions

### Review1: Loop Optimization - Enumerate
**File:** `review1.py`

**Description:** Demonstrates the difference between manual index tracking and Python's `enumerate()` function.

**Key Concepts:**
- Loop index management
- Python built-in functions
- Code optimization

**Comparison:**
```python
# Traditional approach
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
i = 0
for day in weekdays:
    print(i, day)
    i += 1

# Pythonic approach using enumerate
for i, day in enumerate(weekdays):
    print(i, day)
```

**Lesson:** `enumerate()` is cleaner and more Pythonic than manually managing index counters.

---

### Review2: Fuel System Implementation with Abstract Base Classes
**File:** `review2.py`

**Description:** Demonstrates Object-Oriented design principles using Abstract Base Classes and inheritance.

**Key Concepts:**
- Abstract Base Classes (ABC)
- Inheritance
- Polymorphism
- Complex business logic

**Features:**
- Base FuelSystem abstract class
- PetrolFuelSystem concrete implementation
- Dynamic fuel calculation based on:
  - Throttle position
  - Vehicle load
  - Ambient temperature
  - Injector efficiency
  - Combustion losses

**Sample Code:**
```python
from abc import ABC, abstractmethod

class FuelSystem(ABC):
    @abstractmethod
    def fuel(self, throttle, load, temperature):
        pass

class PetrolFuelSystem(FuelSystem):
    def fuel(self, throttle, load, temperature):
        base_flow = 0.8
        throttle_factor = throttle * 0.05
        load_factor = load * 0.1

        if temperature < 10:
            temp_factor = 1.2
        elif temperature > 40:
            temp_factor = 0.9
        else:
            temp_factor = 1.0

        injector_efficiency = 0.92
        combustion_loss = 0.08

        raw_fuel = base_flow + throttle_factor + load_factor
        adjusted_fuel = raw_fuel * temp_factor
        final_fuel = adjusted_fuel * injector_efficiency
        usable_fuel = final_fuel * (1 - combustion_loss)
        
        return usable_fuel
```

**Lesson:** Abstract classes define a contract for derived classes, promoting code reusability and maintainability.

---

### Review3: Code Style Improvements
**File:** `review3.py`

**Description:** Demonstrates code improvements and best practices.

**Key Concepts:**
- Code readability
- Python conventions
- Optimization techniques

**Example:** Cleaner enumeration approach and best practice patterns.

---

## Main Implementation
**File:** `main.py`

**Description:** The complete, production-ready implementation of the Address Book system incorporating all learned concepts.

**Features:**
- Complete Contact class with full details
- Full AddressBook with CRUD operations
- Duplicate detection with proper name matching
- Edit functionality with field selection
- Search capabilities
- Display formatting

**Class Structure:**
```python
class Contact:
    def __init__(self, first, last, address, city, state, zip_code, phone, email):
        # Full contact details

class AddressBook:
    def add_contact(contact)
    def edit_contact(first, last)
    def delete_contact(first, last)
    def display_all()
    def search_by_city(city)
    # ... more methods
```

---

## File Structure

```
Address Book/
├── main.py              # Complete implementation
├── uc1.py              # UC1: Basic Contact Creation
├── uc2.py              # UC2: Add Multiple Contacts
├── uc3.py              # UC3: Edit Contact
├── uc4.py              # UC4: Delete Contact
├── uc5.py              # UC5: Multiple Contacts Loop
├── uc6.py              # UC6: Multiple Address Books
├── uc7.py              # UC7: Duplicate Detection
├── uc8.py              # UC8: Search by City
├── uc9.py              # UC9: View by City
├── uc10.py             # UC10: Fare Calculation
├── review1.py          # Review: Enumerate
├── review2.py          # Review: Fuel System (Abstract Classes)
├── review3.py          # Review: Code Improvements
└── README.md           # This file
```

---

## Learning Path

1. **Basics (UC1-UC2)**: Class definition, instantiation, basic CRUD
2. **Intermediate (UC3-UC5)**: Searching, editing, deletion, loops
3. **Advanced (UC6-UC7)**: Multiple objects, proper duplicate detection
4. **Application (UC8-UC10)**: Real-world features, complex logic
5. **Reviews**: Best practices, design patterns, optimization

---

## Key Concepts Learned

- Object-Oriented Programming (OOP)
- Classes and Objects
- Methods and Attributes
- Lists and Dictionaries
- Loops and Conditionals
- Duplicate Detection Algorithms
- Search and Filter Operations
- Abstract Base Classes (ABC)
- Inheritance and Polymorphism
- Real-world business logic implementation

---

## Git Branches

This project is organized with feature branches:
- `feature/uc1` - UC1 implementation
- `feature/uc2` - UC2 implementation
- `feature/uc3` - UC3 implementation
- `feature/uc4` - UC4 implementation
- `feature/uc5` - UC5 implementation
- `feature/uc6` - UC6 implementation
- `feature/uc7` - UC7 implementation
- `feature/uc8` - UC8 implementation
- `feature/uc9` - UC9 implementation
- `feature/uc10` - UC10 implementation

---

## How to Run

### Run a specific use case:
```bash
python uc1.py
python uc2.py
# ... etc
```

### Run the complete implementation:
```bash
python main.py
```

### Run review sessions:
```bash
python review1.py
python review2.py
python review3.py
```

---

## Notes

- All files follow basic Python conventions
- Each use case is independent and can be run standalone
- The main.py combines all concepts into a single unified system
- Review files provide additional learning and best practices

---

**Author:** Arvind Pandey  
**Project Type:** Training Project  
**Language:** Python 3.x  
**Last Updated:** December 2025
