def print_ones_digit(num):
    # Calculate the ones digit using the modulo operator
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))  # Prompt the user for input
    print_ones_digit(num)  # Call the function to print the ones digit

# Call the main function to start the program
if __name__ == "__main__":
    main()
