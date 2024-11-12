import random

def roll_dice():
    # This function generates a random roll for each die and returns the results
    die1 = random.randint(1, 6)  # local variable die1
    die2 = random.randint(1, 6)  # local variable die2
    return die1, die2

def main():
    # Loop to simulate rolling the dice three times
    for roll_number in range(1, 4):  # local variable roll_number
        die1, die2 = roll_dice()  # die1 and die2 are used here but are local to this function
        print(f"Roll {roll_number}: Die 1 = {die1}, Die 2 = {die2}")

# Run the main function
main()
