# Read Chef's initial rating and the change in rating
x, y = map(int, input().split())

# Calculate Chef's new rating
new_rating = x + y

# Check if Chef becomes 5 star rated
if new_rating >= 2000:
    print("YES")
else:
    print("NO")
