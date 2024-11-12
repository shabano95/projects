# Create an empty dictionary to store the counts
counts = {}

# Continuously ask the user for numbers until an empty input is entered
while True:
    num = input("Enter a number: ")
    
    # Break the loop if the input is empty
    if num == "":
        break
    
    # Convert the input to an integer
    num = int(num)
    
    # Update the count in the dictionary
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

# Print the results
for num, count in counts.items():
    print(f"{num} appears {count} times.")
