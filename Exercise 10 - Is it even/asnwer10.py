## Exercise 10: Is it even? - 35 Marks
#Write a program that tests if a value is even or odd. Follow the instructions outlined below:
### Instructions:
#* The program should ask the user for a number from within the main function.
#* The entered number should be passed to a function that determines if the value is even or odd.
#* The function should return a message indicating whether the number is even or odd.
#* The message returned by the function should be printed from within the main function.
def even_odd(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

def main():
    print("Even or Odd Number Checker")
    entered_value = input("Enter a number: ")

    try:
        number = int(entered_value)
    except ValueError:
        print("Error: You must enter a valid whole number.")
        return

    result = even_odd(number)
    print(result)

if __name__ == "__main__":
    main()
