# Define the ADULT_AGE constant
ADULT_AGE = 18

def is_adult(age):
    # Check if the age is greater than or equal to ADULT_AGE
    if age >= ADULT_AGE:
        return True  # Return True if the person is an adult
    else:
        return False  # Return False if the person is not an adult

def main():
    age = int(input("How old is this person?: "))  # Prompt the user to enter the age
    print(is_adult(age))  # Call the function and print the result

# Run the main function
if __name__ == "__main__":
    main()
