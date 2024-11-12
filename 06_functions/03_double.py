def double(num):
    """Returns the result of multiplying num by 2."""
    return num * 2

def main():
    # Asking the user for input
    num = int(input("Enter a number: "))
    
    # Calling the double function and printing the result
    result = double(num)
    print(f"Double that is {result}")

if __name__ == "__main__":
    main()
