# Read input
x, y = map(int, input().split())

# Check if Chef has enough money to buy 2 ice creams
if y >= 2 * x:
    print("YES")
else:
    print("NO")
