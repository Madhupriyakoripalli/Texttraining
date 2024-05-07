mixed_case = "A Song of Ice and Fire"
# Check if mixed_case is all upper case
print(mixed_case.isupper())
# Check if mixed_case is all lower case
print(mixed_case.islower())
# Change all letters to upper case
print(mixed_case.upper())
# Change all letters to lower case
print(mixed_case.lower())
# Check if mixed_case is in title case
print(mixed_case.istitle())
# Check if mixed_case starts with the letter it starts with
print(mixed_case.startswith(mixed_case[0]))
# Check if mixed_case ends with the letter it ends with
print(mixed_case.endswith(mixed_case[-1]))
# Split mixed_case into words
words = mixed_case.split()
print(words)
# Join words into a single string
joined_string = ' '.join(words)
# Check if the joined string is entirely alphabetic
print(joined_string.isalpha())
print(joined_string)