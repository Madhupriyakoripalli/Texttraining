# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the amount of water Chef drank today
    x = int(input())
    
    # Check if Chef drank at least 2000ml of water
    if x >= 2000:
        print("YES")
    else:
        print("NO")
