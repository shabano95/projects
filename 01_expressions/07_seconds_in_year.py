def main():
    # Constants
    DAYS_IN_A_YEAR = 365
    HOURS_IN_A_DAY = 24
    MINUTES_IN_AN_HOUR = 60
    SECONDS_IN_A_MINUTE = 60
    
    # Calculate the number of seconds in a year
    seconds_in_a_year = DAYS_IN_A_YEAR * HOURS_IN_A_DAY * MINUTES_IN_AN_HOUR * SECONDS_IN_A_MINUTE
    
    # Print the result in a nice statement
    print(f"There are {seconds_in_a_year} seconds in a year!")

# Run the main function
main()
