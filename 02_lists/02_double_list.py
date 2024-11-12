def double_elements(numbers):
    # Create a new list with doubled values using list comprehension
    doubled_numbers = [num * 2 for num in numbers]
    
    # Return the modified list
    return doubled_numbers

# Example usage
numbers = [1, 2, 3, 4]
doubled_numbers = double_elements(numbers)

# Output the result
print(f"Original list: {numbers}")
print(f"Doubled list: {doubled_numbers}")
