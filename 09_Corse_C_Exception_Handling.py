# Problem 1: Handling TypeError
# Errors and Exceptions
# Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("TypeError occurred! Unsupported operand type(s) for ** or pow()")

# Problem 2: Handling ZeroDivisionError
# Handle the exception thrown by the code below by using try and except blocks. 
# Then use a finally block to print 'All Done

x = 5
y = 0

try:
    z = x / y
except ZeroDivisionError:
    print("ZeroDivisionError occurred! Division by zero is not allowed.")
finally:
    print("All Done.")

# Problem 3: Asking for an integer input and printing its square
#Write a function that asks for an integer and prints the square of it. 
# Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            num = int(input("Input an integer: "))
        except ValueError:
            print("An error occurred! Please try again!")
            continue
        else:
            print("Thank you, your number squared is:", num ** 2)
            break

ask()

