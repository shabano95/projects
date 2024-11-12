def print_divisors(num):
    # Print divisors of the number
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):  # Loop through numbers from 1 to num
        if num % i == 0:  # If num is divisible by i without a remainder
            print(i, end=" ")  # Print the divisor

def main():
    num = int(input("Enter a number: "))  # Ask the user for a number
    print_divisors(num)  # Call the print_divisors function

# Call the main function to start the program
if __name__ == "__main__":
    main()
