def get_last_element(lst):
    # Print the last element of the list
    print(lst[-1])

# Main program to prompt the user for input
lst = []
n = int(input("How many elements do you want to input? "))

# Get the elements from the user
for _ in range(n):
    element = input("Enter an element: ")
    lst.append(element)

# Call the function to print the last element
get_last_element(lst)
