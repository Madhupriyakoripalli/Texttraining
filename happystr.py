def is_vowel(char):
    return char in 'aeiou'

def chef_happy_string(s):
    for i in range(len(s) - 2):
        if is_vowel(s[i]) and is_vowel(s[i+1]) and is_vowel(s[i+2]):
            return "HAPPY"
    return "SAD"

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the string
    S = input()
    # Check if Chef is happy or not
    result = chef_happy_string(S)
    # Print the result
    print(result)
