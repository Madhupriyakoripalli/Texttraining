# Task One: Use Python to extract the Google Drive link from the .csv file
import csv

# Read the CSV file
with open('Exercise_Files/find_the_link.csv', 'r') as file:
    reader = csv.reader(file)
    # Extract the link from the diagonal elements
    link = ''.join(row[i] for i, row in enumerate(reader))

print("Google Drive Link:", link)

# Task Two: Download the PDF from the Google Drive link and find the phone number
import PyPDF2
import requests
import re

# Download the PDF from the Google Drive link
url = 'https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q'
response = requests.get(url)
with open('Exercise_Files/Find_the_Phone_Number.pdf', 'wb') as pdf_file:
    pdf_file.write(response.content)

# Open the PDF and search for the phone number
with open('Exercise_Files/Find_the_Phone_Number.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfFileReader(pdf_file)
    phone_pattern = r'\d{3}[-\.\s]?\d{3}[-\.\s]?\d{4}'
    for page_num in range(reader.numPages):
        page = reader.getPage(page_num)
        text = page.extractText()
        phone_numbers = re.findall(phone_pattern, text)
        if phone_numbers:
            print("Phone Number:", phone_numbers[0])
            break
