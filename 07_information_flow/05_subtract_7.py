
# Helper function to subtract 7 from the input number
def subtract_seven(num):
    return num - 7

def main():
    # Prompt the user for a number
    num = int(input("Enter a number: "))
    
    # Call the subtract_seven function and print the result
    result = subtract_seven(num)
    print("Result after subtracting 7:", result)

# Run the program
if __name__ == "__main__":
    main()
