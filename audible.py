# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
  
    x = int(input())
    
    # Check if the frequency is within the audible range
    if 67 <= x <= 45000:
        print("YES")
    else:
        print("NO")