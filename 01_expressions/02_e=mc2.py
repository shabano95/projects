def main():
    # Define the constant speed of light in meters per second
    C = 299792458  # m/s

    # Continually prompt the user for mass input
    while True:
        try:
            # Ask the user to enter mass in kilograms
            mass = float(input("Enter kilos of mass: "))
            
            # Calculate energy using the formula E = m * C^2
            energy = mass * C ** 2
            
            # Display the results
            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s")
            print(f"{energy} joules of energy!\n")
        
        except ValueError:
            print("Please enter a valid number for mass.")
        except KeyboardInterrupt:
            print("\nExiting the program.")
            break

# Run the main function
main()
