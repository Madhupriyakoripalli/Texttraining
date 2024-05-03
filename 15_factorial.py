#create a factorial number
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
# Testing the function with inputs 
input_values = [3, 4, 5]
for value in input_values:
    print(f"Factorial of {value}:", factorial(value))
