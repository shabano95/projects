def print_multiple(message, repeats):
    # Loop to print the message 'repeats' number of times
    for _ in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")  # Get message from user
    repeats = int(input("Enter a number of times to repeat your message: "))  # Get the number of repeats
    print_multiple(message, repeats)  # Call the function to print the message

# Call the main function to start the program
if __name__ == "__main__":
    main()
