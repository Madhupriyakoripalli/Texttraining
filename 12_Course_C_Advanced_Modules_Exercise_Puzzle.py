import shutil
import re
import os

# Step 1: Unzipping the File
shutil.unpack_archive('unzip_me_for_instructions.zip', '', 'zip')

# Step 2: Read the instructions file
with open('extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)

# Step 3: Regular Expression to Find the Link
pattern = r'\d{3}-\d{3}-\d{4}'

# Step 4: Create a function for regex
def search(file, pattern=r'\d{3}-\d{3}-\d{4}'):
    with open(file, 'r') as f:
        text = f.read()
        if re.search(pattern, text):
            return re.search(pattern, text)
        else:
            return ''

# Step 5: OS Walk through the Files to Get the Link
results = []
for folder, sub_folders, files in os.walk(os.path.join(os.getcwd(), 'extracted_content')):
    for f in files:
        full_path = os.path.join(folder, f)
        results.append(search(full_path))

# Step 6: Print the found telephone numbers
for r in results:
    if r != '':
        print(r.group())
