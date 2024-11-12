def main():
    # Ask the user to type a number, then convert it to a float so it can handle decimal numbers
    number = float(input("Type a number to see its square: "))
    
    # Calculate the square of the number by multiplying it by itself
    square = number * number
    
    # Print the result in a format that includes both the original number and its square
    print(f"{number} squared is {square}")

# Run the main function
main()
