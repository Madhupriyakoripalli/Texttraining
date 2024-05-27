# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    
    x = int(input())
    
    # Calculate the total distance Chef travels through office trips in a week
    total_distance = 2 * x * 5
    
    # Print the result
    print(total_distance)
