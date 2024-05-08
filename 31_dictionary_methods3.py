# Paste the provided dictionaries into the .py file
internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
# Use .update() to add the contents of another_one to internet_celebrities
internet_celebrities.update(another_one)
# Create a variable and assign it a copy of internet_celebrities
internet_celebrities_copy = internet_celebrities.copy()
# Use the .clear() method to get rid of the contents of internet_celebrities
internet_celebrities.clear()