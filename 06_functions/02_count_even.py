def count_even(lst):
    """Populates the list with user input and counts the even numbers."""
    
    # Step 1: Populating the list
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        
        if user_input == "":  # If the input is empty, stop taking inputs
            break
        
        try:
            num = int(user_input)  # Convert the input into an integer
            lst.append(num)  # Append the integer to the list
        except ValueError:
            print("Please enter a valid integer.")  # Handle non-integer input
    
    # Step 2: Count even numbers
    even_count = 0
    for num in lst:
        if num % 2 == 0:  # Check if the number is even
            even_count += 1
    
    print(f"The number of even numbers in the list is: {even_count}")

def main():
    lst = []
    count_even(lst)  # Call the function to populate the list and count evens

if __name__ == '__main__':
    main()
