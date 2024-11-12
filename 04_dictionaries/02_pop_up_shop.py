# Dictionary of fruits and their prices
fruit_prices = {
    "apple": 2.5,
    "durian": 5.0,
    "jackfruit": 10.0,
    "kiwi": 3.0,
    "rambutan": 4.0,
    "mango": 3.5
}

# Function to calculate the total cost
def calculate_total(fruit_prices):
    total_cost = 0
    # Loop through each fruit in the dictionary
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * price
    
    # Print the total cost
    print(f"Your total is ${total_cost:.2f}")

# Call the function to run the program
calculate_total(fruit_prices)
