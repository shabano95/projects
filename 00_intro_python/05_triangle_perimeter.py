def main():
    #22ask the user to enter the lengths of each side of the triangle
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))
    
    # Calculate the perimeter of the triangle
    perimeter = side1 + side2 + side3
    
    # Print the perimeter
    print("The perimeter of the triangle is", perimeter)

# Run the main function
main()
