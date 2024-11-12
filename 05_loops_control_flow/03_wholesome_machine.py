# The affirmation we want the user to type
affirmation = "I am capable of doing anything I put my mind to."

# Loop until the user types the affirmation correctly
while True:
    user_input = input("Please type the following affirmation: ")
    
    # Check if the input is correct
    if user_input == affirmation:
        print("That's right! :)")
        break  # Exit the loop if the affirmation is correct
    else:
        print("Hmmm That was not the affirmation.")