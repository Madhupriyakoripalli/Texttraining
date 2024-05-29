# Problem 1: Convert 1024 to binary and hexadecimal representation
num = 1024
binary_representation = bin(num)
hexadecimal_representation = hex(num)
print("Binary representation:", binary_representation)
print("Hexadecimal representation:", hexadecimal_representation)

# Problem 2: Round 5.23222 to two decimal places
rounded_num = round(5.23222, 2)
print("Rounded number:", rounded_num)

# Problem 3: Check if every letter in the string s is lowercase
s = 'hello how are you Mary, are you feeling okay?'
is_lower = all(c.islower() for c in s if c.isalpha())
print("Are all letters lowercase?", is_lower)

# Problem 4: How many times does the letter 'w' show up in the string below?
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
count_w = s.count('w')
print("Number of times 'w' appears:", count_w)

# Problem 5: Find the elements in set1 that are not in set2
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
difference_set = set1 - set2
print("Elements in set1 not in set2:", difference_set)

# Problem 6: Find all elements that are in either set
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension
power_dict = {i: i**3 for i in range(5)}
print("Dictionary:", power_dict)

# Problem 8: Reverse the list below
list1 = [1,2,3,4]
reversed_list = list1[::-1]
print("Reversed list:", reversed_list)

# Problem 9: Sort the list below
list2 = [3,4,2,5,1]
sorted_list = sorted(list2)
print("Sorted list:", sorted_list)
