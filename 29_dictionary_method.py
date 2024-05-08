# Create a dictionary spanning multiple lines
music_dictionary = {
    "Queen": "Bohemian Rhapsody",
    "Bee Gees": "Stayin' Alive",
    "U2": "One",
    "Michael Jackson": "Billie Jean",
    "The Beatles": "Hey Jude",
    "Bob Dylan": "Like A Rolling Stone"
}
# Print the length of the dictionary
print("Length of the dictionary:", len(music_dictionary))
# Print all keys from the dictionary on separate lines
print("Keys in the dictionary:")
for key in music_dictionary.keys():
    print(key)
# Print all values from the dictionary
print("\nValues in the dictionary:")
for value in music_dictionary.values():
    print(value)
