# Initialize an empty list
user_list = []

# Start a loop to ask for input until the user presses Enter without typing anything
while True:
    # Prompt the user to enter a value
    value = input("Enter a value: ")

    # If the user presses Enter without typing anything, break out of the loop
    if value == "":
        break

    # Add the entered value to the list
    user_list.append(value)

# Print the list once the loop is finished
print("Here's the list:", user_list)
