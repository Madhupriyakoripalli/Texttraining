# Advanced Numbers
# Problem 1
num = 1024
binary_representation = bin(num)
hexadecimal_representation = hex(num)
print("Binary representation:", binary_representation)
print("Hexadecimal representation:", hexadecimal_representation)

# Problem 2
num = 5.23222
rounded_num = round(num, 2)
print("Rounded number:", rounded_num)

# Advanced Strings
# Problem 3
s = 'hello how are you Mary, are you feeling okay?'
print("Is every letter in s lowercase?", s.islower())

# Problem 4
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
count_w = s.count('w')
print("Number of times 'w' appears in s:", count_w)

# Advanced Sets
# Problem 5
set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
elements_not_in_set2 = set1 - set2
print("Elements in set1 but not in set2:", elements_not_in_set2)

# Problem 6
elements_in_either_set = set1.union(set2)
print("Elements that are in either set:", elements_in_either_set)

# Advanced Dictionaries
# Problem 7
dictionary = {x: x**3 for x in range(5)}
print("Dictionary:", dictionary)

# Advanced Lists
# Problem 8
list1 = [1, 2, 3, 4]
reversed_list1 = list1[::-1]
print("Reversed list:", reversed_list1)

# Problem 9
list2 = [3, 4, 2, 5, 1]
sorted_list2 = sorted(list2)
print("Sorted list:", sorted_list2)
