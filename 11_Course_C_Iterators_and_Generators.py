# Iterators and Generators
# Problem 1: Generator for Squares
# Create a generator that generates the squares of numbers up to some number N.

def gensquares(N):
    for num in range(N):
        yield num ** 2

for x in gensquares(10):
    print(x)

# Problem 2: Generator for Random Numbers
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
import random

def rand_num(low, high, n):
    for _ in range(n):
        yield random.randint(low, high)

for num in rand_num(1, 10, 12):
    print(num)

# Problem 3: Converting a String to an Iterator
# Use the iter() function to convert the string below into an iterator:
s = 'hello'
iter_s = iter(s)

# Problem 4
#Explain a use case for a generator using a yield statement 
#where you would not want to use a normal function with a return statement.

#ANS: If the output has the potential of taking up a large amount of memory and 
#you only intend to iterate through it, you would want to use a generator. 

# Extra Credit!

#Can you explain what gencomp is in the code below?
#(Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
