# Get a positive integer from the user
user_integer = int(input("Enter a positive integer: "))

# Initialize variables
sum_of_integers = 0
current_number = user_integer

# Calculate the sum using a while loop
while current_number > 0:
    sum_of_integers += current_number
    current_number -= 1

# Print the user entered integer and the sum found by the while loop
print("User entered integer:", user_integer)
print("Sum found by the while loop:", sum_of_integers)

