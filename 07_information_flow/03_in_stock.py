# Function to return the number of fruit in stock
def num_in_stock(fruit):
    # A dictionary simulating the inventory of fruits
    inventory = {
        "apple": 50,
        "pear": 1000,
        "banana": 200,
        "orange": 30,
        "grape": 150
    }
    
    # Return the number of fruit in stock, or 0 if the fruit is not found
    return inventory.get(fruit.lower(), 0)

def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ")
    
    # Get the number of that fruit in stock
    stock = num_in_stock(fruit)
    
    # Check if the fruit is in stock and print the appropriate message
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

# Run the program
if __name__ == "__main__":
    main()
