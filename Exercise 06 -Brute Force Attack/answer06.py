# Exercise 6: Brute Force Attack - 30 Marks
# This program simulates a password entry system. The user must enter
# the correct password to gain access. The program also includes an
# optional feature that limits users to a maximum of 5 attempts.

#Answer:
# Set the correct password and maximum number of allowed attempts.

correct_password = "12345"   # The required password 
max_attempts = 5             # User can try up to 5 times
attempts = 0                 # Counter to track the number of attempts made

# While loop continues until the user enters the correct password
# or until they run out of attempts
while attempts < max_attempts:

    # Ask the user to type the password
    password = input("Enter the password: ")

    # Check if the entered password is correct
    if password == correct_password:
        print("Access granted. You have successfully signed in.")
        break  # Exit the loop because the correct password was entered

    else:
        # Increase the attempt counter because the password was wrong
        attempts += 1
        remaining_attempts = max_attempts - attempts

        # If the user still has attempts left
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts remaining.")
        else:
            # All attempts used = security alert
            print("All attempts used. The authorities have been notified.")