arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]

# Remove "tiger" from the list
del arctic_animals[arctic_animals.index("tiger")]
# Remove "elephant" from the list
arctic_animals.remove("elephant")
# Add "arctic fox" to the list
arctic_animals.append("arctic fox")
# Insert "snowy owl" between "polar bear" and "walrus"
arctic_animals.insert(arctic_animals.index("walrus"), "snowy owl")
# Sort the list alphabetically
arctic_animals.sort()
# Display the modified list
print(arctic_animals)
# Get the index number of "reindeer" and print it
reindeer_index = arctic_animals.index("reindeer")
print("Index of 'reindeer':", reindeer_index)
