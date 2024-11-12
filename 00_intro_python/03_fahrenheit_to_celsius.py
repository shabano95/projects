def main():
    # ask the user to enter a temperature in Fahrenheit
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert the temperature to Celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
    
    # Display the result
    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")

# main function to call
main()
