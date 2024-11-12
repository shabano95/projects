def get_user_data():
    # Prompt the user for their first name, last name, and email address
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    
    # Return the data as a tuple
    return first_name, last_name, email

def main():
    # Call get_user_data to retrieve the user data
    user_data = get_user_data()
    
    # Print the received user data
    print("Received the following user data:", user_data)

# Run the program
if __name__ == "__main__":
    main()
