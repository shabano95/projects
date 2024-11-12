# Constant to store the maximum value for the Fibonacci sequence
MAX_VALUE = 10000

def print_fibonacci():
    # Starting values for Fibonacci sequence
    a, b = 0, 1
    
    # Print the first two terms
    print(a, end=" ")
    
    # Print Fibonacci sequence terms until they exceed the maximum value
    while b < MAX_VALUE:
        print(b, end=" ")
        a, b = b, a + b  # Update a and b to the next two terms in the sequence

# Call the function to print the Fibonacci sequence
print_fibonacci()
