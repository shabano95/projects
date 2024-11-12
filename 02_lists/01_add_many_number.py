def sum_of_numbers(numbers):
    # Initialize the sum to 0
    total = 0
    
    # Loop through each number in the list and add it to the total
    for num in numbers:
        total += num
    
    # Return the total sum
    return total

# Example usage
numbers_list = [1, 2, 3, 4, 5]
result = sum_of_numbers(numbers_list)
print(f"The sum of the numbers is: {result}")
