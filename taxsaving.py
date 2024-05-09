# Function to calculate the minimum amount needed to invest
def calculate_investment(X, Y):
    return max(0, X - Y)

T = int(input())

for _ in range(T):
    # Input earnings (X) and tax threshold (Y)
    X, Y = map(int, input().split())
    
    investment_needed = calculate_investment(X, Y)
    
    # Output the result
    print(investment_needed)