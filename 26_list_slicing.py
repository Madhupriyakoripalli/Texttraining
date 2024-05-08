# Step 1
list_of_lists = [[0, 2], [4, 6], [8, 10], [12, 14]]

# Access the first list from the list of lists in step 1 by index then print it
first_list = list_of_lists[0]
print(first_list)

# Access the 14 from the list in step 1 then print it
fourteen = list_of_lists[-1][-1]
print(fourteen)

# Step 2
second_list = ["chair", "table", "desk", "lamp", "bed"]

# Use a negative integer to access "chair" from the variable in step 4 by index then print it
chair = second_list[-5]
print(chair)

# Print "Most people own at least 2 chairs."
print("Most people own at least " + str(first_list[1]) + " " + chair + ".")

# Step 3
third_list = [0.98, 8.76, 6.54, 4.32]

# Print the slice [8.76, 6.54, 4.32] from the variable 
print(third_list[1:])

# Print the slice [8.76, 6.54] from the variable 
print(third_list[1:3])

# Print the slice [0.98, 8.76] from the variable
print(third_list[:2])

