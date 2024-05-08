# Create a dictionary using .fromkeys() with consonants as keys
consonants_dict = dict.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")
# Print each key-value pair on a separate line using a for loop and .items() method
for key, value in consonants_dict.items():
    print(key, value)
# Pop and print "Big Mac" from the dictionary
fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's"))
# Remove the last key-value pair using .popitem() and print the updated dictionary
fast_food_items.popitem()
print(fast_food_items)