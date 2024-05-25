# Built-in Functions Test
# Problem 1: Finding the length of each word in the phrase using map():

def word_lengths(phrase):
    return list(map(len, phrase.split()))

word_lengths('How long are the words in this phrase')

# Problem 2: Converting a list of digits to a number using reduce():
# Use reduce() to take a list of digits and return the number that they correspond to

from functools import reduce

def digits_to_num(digits):
    return reduce(lambda x, y: x * 10 + y, digits)

digits_to_num([3, 4, 3, 2, 1])

#Problem 3: Filtering words from a list that start with a target letter using filter():
# Use filter to return the words from a list of words which start with a target letter.

def filter_words(word_list, letter):
    return list(filter(lambda word: word.startswith(letter), word_list))

l = ['hello', 'are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'heart']
filter_words(l, 'h')

# Problem 4: Concatenating strings from two lists with a connector using zip() and list comprehension:
# Use zip() and a list comprehension to return a list of the same length where each value is the two strings from L1 and L2 concatenated together with connector between them

def concatenate(L1, L2, connector):
    return [x + connector + y for x, y in zip(L1, L2)]

concatenate(['A', 'B'], ['a', 'b'], '-')

# Problem 5: Creating a dictionary with values of a list as keys and their indices as values using enumerate():
def d_list(L):
    return {value: index for index, value in enumerate(L)}

d_list(['a', 'b', 'c'])

# Problem 6: Counting the number of items in the list whose value equals its index using enumerate():

def count_match_index(L):
    return sum(1 for index, value in enumerate(L) if index == value)

count_match_index([0, 2, 2, 1, 5, 5, 6, 10])

