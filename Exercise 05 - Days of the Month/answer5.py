# Exercise 5: Days of the Month - 30 Marks
#Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.
# Instructions:
#1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
#2. Input Handling: Ask the user to input the month number.
#3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.
# Advanced Requirement:
#Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.
# Exercise 5: Days of the Month - 30 Marks
# This program tells the user how many days are in a specific month.
# It uses a dictionary to map month numbers (1–12) to the number of days.
# It also adjusts February depending on whether the year is a leap year.

#Answer:
# Function: get_days(month, year=None)
# Purpose: Returns the number of days in a given month.
# If the month is February, a year may be provided
# to determine leap year status.
def get_days(month, year=None):

    # Dictionary mapping each month number to days (default February = 28)
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }

    # Validate month number
    if month < 1 or month > 12:
        return "The number added is wrong. Please enter a number between 1 and 12." 

    # Special case: February (month 2)
    if month == 2 and year is not None:
        # Check leap year rules properly
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29  # Leap year February
        else:
            return 28  # Normal February

    # Return the number of days for all other months
    return month_days[month]

# Main Program
month_input = input("Enter the month number (1-12): ")

try:
    month_number = int(month_input)

    # If month is February, ask for the year
    if month_number == 2:
        year_input = input("Please enter the year: ")
        year_number = int(year_input)
        days = get_days(month_number, year_number)
    else:
        days = get_days(month_number)

    print(f"There are {days} days in month {month_number}.")

except ValueError:
    print("Invalid input. Please enter whole numbers only.") 