string = "North Dakota"
# Right justify the string with 17 spaces
print(string.rjust(17))
# Left justify the string with 17 spaces, padding with "*"
print(string.ljust(17, "*"))
# Center the string with 16 characters, padding with "+"
center_plus =string.center(16, "+")
print(center_plus)
# Remove "North" from the left of the string
print(string.lstrip("North"))
# Remove "+" from the right of center_plus
print(center_plus.rstrip("+"))
# Remove "+" from both sides of center_plus
print(center_plus.strip("+"))
# Replace "North" with "South" in the string
print(string.replace("North", "South"))