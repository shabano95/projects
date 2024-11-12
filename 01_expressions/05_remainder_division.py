def main():
    # Ask the user for the first integer (dividend)
    dividend = int(input("Please enter an integer to be divided: "))
    
    # Ask the user for the second integer (divisor)
    divisor = int(input("Please enter an integer to divide by: "))
    
    # Calculate the quotient and remainder
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # Print the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# Run the main function
main()
