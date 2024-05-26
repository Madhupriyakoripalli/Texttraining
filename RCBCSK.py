# Read input
x, y = map(int, input().split())

# Calculate the difference between RCB's score and CSK's score
difference = x - y

# Check if RCB qualifies to the playoffs
if difference >= 18:
    print("RCB")
else:
    print("CSK")

