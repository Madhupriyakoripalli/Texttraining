def count_words(sentence):
    # Filter out characters besides numbers, letters, spaces, apostrophes, and hyphens
    filtered_sentence = ''.join(char if char.isalnum() or char in [' ', "'", "-"] else '' for char in sentence)
   # Count the number of spaces in the filtered string and add 1
    return filtered_sentence.count(' ') + 1
# Test the function with the provided strings
str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."
print(count_words(str_1))
print(count_words(str_2))
print(count_words(str_3))
