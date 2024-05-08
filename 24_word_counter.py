def count_words(sentence):
    # Filter out characters besides numbers, letters, spaces, apostrophes, and hyphens
    filtered_sentence = ''.join(char if char.isalnum() or char in [' ', "'", "-"] else '' for char in sentence)
   

