import random

def main():
    # Simulate rolling two dice
    die1 = random.randint(1, 6)  # Roll for the first die (random number between 1 and 6)
    die2 = random.randint(1, 6)  # Roll for the second die (random number between 1 and 6)
    
    # Calculate the total of the two dice rolls
    total = die1 + die2
    
    # Print the results of the rolls and the total
    print(f"Die 1 rolled: {die1}")
    print(f"Die 2 rolled: {die2}")
    print(f"Total: {total}")

# Run the main function
main()
