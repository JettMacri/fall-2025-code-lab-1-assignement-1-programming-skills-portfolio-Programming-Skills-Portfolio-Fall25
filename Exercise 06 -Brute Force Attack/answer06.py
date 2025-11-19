## Exercise 6: Brute Force Attack - 30 Marks
#Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.
### Basic Requirements:
#1. Define the correct password.
#2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
#3. Output an appropriate message when the correct password is entered.
### Optional Requirements:
#Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.
#Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

correct_password = "125656"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    password = input("Enter your password") 
    if password == correct_password:
        print("You have been signed in") 
        break
    else: 
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"The password is incorrect. You have {remaining_attempts} attempts remaining") 
        else: 
            print (f"The authorities have been alerted") 