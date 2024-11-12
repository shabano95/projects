import math

def main():
    # Prompt the user for the lengths of the two sides
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))
    
    # Calculate the length of the hypotenuse using the Pythagorean theorem
    bc = math.sqrt(ab ** 2 + ac ** 2)
    
    # Display the result
    print(f"The length of BC (the hypotenuse) is: {bc}")

# Run the main function
main()
