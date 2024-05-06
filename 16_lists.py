#Create a variable and assign it a list 
mixed_list = [10, 3.14, True, "Hello", [1, 2, 3]]
#Create another variable and assign it a call of the list() function with a string
string_list = list("Python")
#check if the letter "e" is in the list assigned to the variable
if "e" in string_list:
    print("The letter 'e' is in the list.")
else:
    print("The letter 'e' is not in the list.")
#Use the keyword "not in" to check if the letter "a" is not in the list 
if "a" not in string_list:
    print("The letter 'a' is not in the list.")
else:
    print("The letter 'a' is in the list.")
