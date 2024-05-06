# Create a variable and assign it the string "Just do it!"
my_string = "Just do it!"
# Access the "!" from the variable by index and print it
print(my_string[-1])
# Print the slice "do" from the variable
print(my_string[5:7])
# print the slice "it!" from the variable
print(my_string[8:])
# Print the slice "Just" from the variable
print(my_string[:4])
# Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".
resulting_string = "Don't " + my_string[5:]
print(resulting_string)


