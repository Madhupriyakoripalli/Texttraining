# Read the number of rainy and cloudy days
X, Y = map(int, input().split())

# Calculate the number of clear days
clear_days = 7 - X - Y

# Output the number of clear days
print(clear_days)
