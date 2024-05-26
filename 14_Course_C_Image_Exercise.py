from PIL import Image

# Open the word matrix and mask images
words = Image.open('word_matrix.png')
mask = Image.open("mask.png")

# Resize the mask to match the dimensions of the word matrix
mask = mask.resize(words.size)

# Add an alpha channel to the mask image
mask.putalpha(200)

# Paste the mask onto the word matrix image
words.paste(mask, (0, 0), mask)

# Display the result
words.show()
