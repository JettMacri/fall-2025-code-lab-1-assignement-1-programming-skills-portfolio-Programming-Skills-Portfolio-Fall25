## Exercise 3: Biography - 25 Marks
#In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.
### Steps:
#1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
#2. Print the values on separate lines using a single `print()` statement.
#3. Use variables with appropriate data types for each piece of information.
### Advanced Requirements:
#Have the user input their name, hometown, and age instead of hardcoding the values.
#Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
#Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?
#Answer:
# Exercise - Personal Information Program
# This program asks the user for their first name, last name,
# hometown, and age. It then prints the information back to them.
# This demonstrates the use of variables, user input, and output.

# Collect user information using input()
first_name = input("Enter your first name: ")   # Ask for first name
last_name = input("Enter your last name: ")     # Ask for last name
hometown = input("Enter your hometown: ")       # Ask for hometown

# Age is converted to an integer because it is a number
age = int(input("Enter your age: "))

# Display the collected information back to the user

print("Your name is", first_name, last_name)
print("Your hometown is", hometown)
print("Your age is", age)

# Note: If the user enters a non-numeric value for age, the program will raise a ValueError.
