def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high

# Test the function
print(in_range(5, 1, 10))  # True, because 5 is between 1 and 10
print(in_range(0, 1, 10))  # False, because 0 is not between 1 and 10
print(in_range(10, 1, 10)) # True, because 10 is equal to high and it's inclusive
