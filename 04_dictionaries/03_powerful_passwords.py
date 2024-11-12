import hashlib

# Simulating the hash_password function (this function will generate a hash for the password)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# This is where the email and its hashed password will be stored
stored_logins = {
    "user1@example.com": hash_password("password123"),
    "user2@example.com": hash_password("securepassword"),
    "user3@example.com": hash_password("mysecretpass")
}

# Function to check the login
def login(email, password_to_check):
    # Hash the password the user entered
    hashed_password = hash_password(password_to_check)
    
    # Check if the email exists in the stored logins
    if email in stored_logins:
        # Compare the hashed password with the stored hashed password
        if stored_logins[email] == hashed_password:
            return True
    return False

# Testing the login function
email = input("Enter your email: ")
password = input("Enter your password: ")

if login(email, password):
    print("Login successful!")
else:
    print("Login failed. Invalid email or password.")
