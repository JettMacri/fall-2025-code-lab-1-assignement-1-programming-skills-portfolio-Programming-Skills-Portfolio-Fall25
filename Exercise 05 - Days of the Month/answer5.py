## Exercise 5: Days of the Month - 30 Marks
#Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.
### Instructions:
#1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
#2. Input Handling: Ask the user to input the month number.
#3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.
### Advanced Requirement:
#Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.
def get_days(month, year=None):
    if month < 1 or month > 12:
        return "The number added is wrong. Please enter a number between 1 and 12." #If the month number added is wrong, it is outputed the same
    if month == 2:  
        if year is not None: 
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
                return 29 
            else:
                return 28  
    return  [month]  

month_input = input("Enter the month number (1-12): ") #The user is asked to enter a number

try:
    month_number = int(month_input)  
    
    if month_number == 2:
        year_input = input("Please enter year: ") #If febuary/2 is inputed, the user is asked for year to make sure of the leap year
        year_number = int(year_input)  
        days = get_days(month_number, year_number)  
    else:
        days = get_days(month_number)  
    

    print(f"There are {days} days in month {month_number}")

except ValueError:
    print("Invalid")