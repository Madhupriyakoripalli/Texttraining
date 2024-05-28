# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the speeds of Jerry and Tom
    X, Y = map(int, input().split())
    
    # Check if Tom will be able to catch Jerry
    if X < Y:
        print("YES")
    else:
        print("NO")
