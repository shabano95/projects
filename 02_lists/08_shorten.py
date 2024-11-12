MAX_LENGTH = 3  # The maximum allowed length for the list

def shorten(lst):
    # Check if the list is longer than MAX_LENGTH
    while len(lst) > MAX_LENGTH:
        # Pop the last element from the list and print it
        removed_item = lst.pop()
        print(removed_item)

# The main function to test the shorten function
def main():
    # Sample list for testing
    user_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

    # Call the shorten function with the list
    shorten(user_list)

# Call main to run the program
main()
