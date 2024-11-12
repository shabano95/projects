def main():
    # Ask the user to enter the measurement in feet
    feet = float(input("Enter measurement in feet: "))
    
    # Convert feet to inches (1 foot = 12 inches)
    inches = feet * 12
    
    # Display the result
    print(f"{feet} feet is equal to {inches} inches.")

# Run the main function
main()
