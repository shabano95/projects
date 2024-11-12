def average(a: float, b: float) -> float:
    """
    Returns the number which is halfway between a and b
    """
    return (a + b) / 2

def main():
    # Getting input from the user for two sets of numbers
    a1 = float(input("Enter the first number for avg_1: "))
    b1 = float(input("Enter the second number for avg_1: "))
    a2 = float(input("Enter the first number for avg_2: "))
    b2 = float(input("Enter the second number for avg_2: "))

    # Calculating the averages
    avg_1 = average(a1, b1)
    avg_2 = average(a2, b2)

    # Calculating the final average
    final = average(avg_1, avg_2)

    # Printing results
    print(f"avg_1 = ({a1} + {b1}) / 2 = {avg_1}")
    print(f"avg_2 = ({a2} + {b2}) / 2 = {avg_2}")
    print(f"final average between avg_1 and avg_2: ({avg_1} + {avg_2}) / 2 = {final}")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
