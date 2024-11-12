# Create an empty dictionary for the phonebook
phonebook = {}

# Function to add a contact
def add_contact(name, number):
    phonebook[name] = number
    print(f"Added {name} to the phonebook.")

# Function to search for a contact
def search_contact(name):
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}.")
    else:
        print(f"{name} not found in the phonebook.")

# Function to display all contacts
def display_contacts():
    if phonebook:
        print("Phonebook Contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("The phonebook is empty.")

# Menu-driven interface
while True:
    print("\nPhonebook Menu:")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Display all contacts")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        add_contact(name, number)
    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == "3":
        display_contacts()
    elif choice == "4":
        print("Exiting the phonebook program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
