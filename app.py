import json
import os
inventory = {
    "lipstick": {"quantity": 10, "price": 15.99},
    "lip gloss": {"quantity": 15, "price": 12.49},
    "face moisturizer": {"quantity": 8, "price": 20.00},
    "face wash": {"quantity": 20, "price": 10.75},
    "face mask": {"quantity": 5, "price": 25.00}
}

ADMIN_PASSWORD = "admin123"  # authentication password for admin access

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item, details in inventory.items():
            print(f"{item.capitalize()}: {details['quantity']} units at ${details['price']} each")

class Admin:
    """Class for Admin with permissions to add, update, and delete inventory items."""
    
    @staticmethod
    def add_item(name, quantity, price):
        if name in inventory:
            inventory[name]['quantity'] += quantity
        else:
            inventory[name] = {'quantity': quantity, 'price': price}
        print(f"Added {quantity} of {name}.")
    
    @staticmethod
    def update_item(name, quantity=None, price=None):
        if name in inventory:
            if quantity is not None:
                inventory[name]['quantity'] = quantity
            if price is not None:
                inventory[name]['price'] = price
            print(f"Updated {name}.")
        else:
            print(f"{name} not found in inventory.")
    
    @staticmethod
    def delete_item(name):
        if name in inventory:
            del inventory[name]
            print(f"Deleted {name} from inventory.")
        else:
            print(f"{name} not found in inventory.")

class User:
    """Class for User with permission only to view inventory."""
    
    @staticmethod
    def view_inventory():
        view_inventory()

def main():
    print("Welcome to the Cosmetics Store Inventory System!")
    import os

role = os.getenv("ROLE", "user")  # Default to 'user' if ROLE is not provided
print("Role:", role)

    
if role == "admin":
        password = input("Enter admin password: ")
        if password == ADMIN_PASSWORD:
            admin = Admin()
            while True:
                print("\nAdmin Menu:")
                print("1. Add Item")
                print("2. View Inventory")
                print("3. Update Item")
                print("4. Delete Item")
                print("5. Exit")
                
                choice = input("Choose an option: ")
                
                if choice == '1':
                    name = input("Enter item name: ").lower()
                    quantity = int(input("Enter quantity: "))
                    price = float(input("Enter price: "))
                    admin.add_item(name, quantity, price)
                
                elif choice == '2':
                    view_inventory()
                
                elif choice == '3':
                    name = input("Enter item name to update: ").lower()
                    quantity = input("Enter new quantity (leave blank to skip): ")
                    price = input("Enter new price (leave blank to skip): ")
                    admin.update_item(name, int(quantity) if quantity else None, float(price) if price else None)
                
                elif choice == '4':
                    name = input("Enter item name to delete: ").lower()
                    admin.delete_item(name)
                
                elif choice == '5':
                    print("Exiting admin menu.")
                    break
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Incorrect password. Access denied.")
    
elif role == "user":
        user = User()
        while True:
            print("\nUser Menu:")
            print("1. View Inventory")
            print("2. Exit")
            
            choice = input("Choose an option: ")
            
            if choice == '1':
                user.view_inventory()
            
            elif choice == '2':
                print("Exiting user menu.")
                break
            else:
                print("Invalid option. Please try again.")
else:
        print("Invalid role. Please restart and enter 'admin' or 'user'.")

if __name__ == "__main__":
    main()