# Function to check if it's possible to change string S to R
def can_transform(S, R):
    # Count the number of 1s in S and R
    count_S_1 = S.count('1')
    count_R_1 = R.count('1')
    
    # If the number of 1s in S and R are not equal, it's impossible
    if count_S_1 != count_R_1:
        return "NO"
    
    # Otherwise, it's possible
    return "YES"

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the length of the strings
    N = int(input())
    
    # Read the strings S and R
    S = input().strip()
    R = input().strip()
    
    # Check if it's possible to transform S to R
    result = can_transform(S, R)
    
    # Output the result
    print(result)
