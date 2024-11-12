# Minimum height requirement
MIN_HEIGHT = 50

# Ask the user for their height
height = int(input("How tall are you? "))

# Check if the user meets the height requirement
if height >= MIN_HEIGHT:
    print("You're tall enough to ride!")
else:
    print("You're not tall enough to ride, but maybe next year!")
