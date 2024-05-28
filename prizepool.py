# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
   
    x, y = map(int, input().split())
    
    # Calculate the total prize money
    total_prize = 10 * x + 90 * y
    
    # Print the total prize money
    print(total_prize)

