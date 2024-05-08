# Take a input
original_string = input("Enter a string: ")
# Initialize an empty string to hold the reversed string
reversed_string = ""

# Use a for loop to reverse the string
for i in range(len(original_string) - 1, -1, -1):
    reversed_string += original_string[i]
    
# Print the reversed string
print("Reversed string:", reversed_string)

