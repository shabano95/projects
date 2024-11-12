def add_three_copies(my_list, data):
    # Add three copies of the data to the list
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

# Main program starts here
message = input("Enter a message to copy: ")

# Create an empty list
my_list = []

# Show the list before modification
print("List before:", my_list)

# Call the function to add three copies of the message to the list
add_three_copies(my_list, message)

# Show the list after modification
print("List after:", my_list)
