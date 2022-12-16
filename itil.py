import requests
import json
import pyperclip

# Dictionary of books and their ISBNs
books = {'ITIL V3 Foundation Exam: The Study Guide': '9781119942757', 'ITIL Foundation, ITIL 4 edition': ' 9780113313082', 'ITIL Foundation Exam Study Guide': '9781119942757', 'ITIL Service Transition: 2011 (Best Management Practices)': '9780113313068', 'ITIL Service Strategy (ITIL v3 Service Lifecycle)': '9780113313044', 'Operational Support And Analysis ITIL Intermediate Capability Handbook':'9780113313075', 'ITIL Service Design: 2011':'9780113313051','ITIL Continual Service Improvement: 2011 (Best Management Practices)':'9780113313082'}

# Print the list of books
print("Choose one of the following books:")
for i, book in enumerate(books):
    print(f"{i+1}: {book}")

# Get the user's choice of book
choice = int(input())

# Get the ISBN of the chosen book
isbn = list(books.values())[choice-1]

# Use the ISBN to get the publisher and year of publication using the Amazon Books API
url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
response = requests.get(url)
data = response.json()
publisher = data[f"ISBN:{isbn}"]['publishers'][0]['name']
year = data[f"ISBN:{isbn}"]['publish_date']


# Get the page number from the user
page = input("Enter page number: ")

# Generate the line in the specified format
line = f"AXELOS Limited, {list(books.keys())[choice-1]}, {publisher} {year}, p.{page} ISBN {isbn}"

# Print the line and copy it to the clipboard
print(line)
pyperclip.copy(line)
print("\nCopied to clipboard!")
