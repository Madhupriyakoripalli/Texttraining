def count_words(sentence):
    # Filter out characters besides numbers, letters, spaces, apostrophes, and hyphens
    filtered_sentence = ''.join(char if char.isalnum() or char in [' ', "'", "-"] else '' for char in sentence)
   # Count the number of spaces in the filtered string and add 1
    return filtered_sentence.count(' ') + 1

