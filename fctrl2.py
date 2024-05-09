# Function to calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

t = int(input())


for _ in range(t):
    # Input the integer n
    n = int(input())
    
   
    result = factorial(n)
    
    # Output the result
    print(result)
