import random

def guess_my_number():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)

    # Start the game
    print("I am thinking of a number between 0 and 99...")

    while True:
        # Prompt the user to enter their guess
        guess = int(input("Enter a guess: "))

        # Check if the guess is too high, too low, or correct
        if guess > secret_number:
            print("Your guess is too high")
        elif guess < secret_number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break  # Exit the loop when the guess is correct

# Run the game
guess_my_number()
