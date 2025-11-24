## Exercise 8: Simple Search - 30 Marks
#Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".
### Optional Requirements:
#1. Allow the user to input the search term instead of using a predefined value.
#2. Implement the search functionality based on user input.
#Answer:
# This program searches for a name inside a list.

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask the user which name they want to search for
search_term = input("Enter the name to search for: ")

# Check if the name is in the list
if search_term in names:
    print(f"{search_term} was found in the list.")
else:
    print(f"{search_term} was not found in the list.")
