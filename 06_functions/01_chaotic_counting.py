import random

DONE_LIKELIHOOD = 0.3  # Example: 30% chance to stop at each step

def done() -> bool:
    """Randomly returns True with a likelihood of DONE_LIKELIHOOD"""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """Counts from 1 to 10, stopping early if done() returns True"""
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    
    for i in range(1, 11):  # Counting from 1 to 10
        if done():  # Check if we should stop
            return  # Stops the function if done() returns True
        print(i, end=" ")  # Print the current number without newline
    
    print()  # Print a newline after counting up to 10

def main():
    chaotic_counting()  # Call chaotic counting
    print("I'm done.")  # Print this when chaotic_counting finishes

if __name__ == '__main__':
    main()
