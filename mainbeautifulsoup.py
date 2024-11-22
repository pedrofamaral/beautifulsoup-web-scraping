import requests
from bs4 import BeautifulSoup
import csv
from pymongo import MongoClient
import sys

# Send a GET request to the URL
response = requests.get('https://www.twitch.tv/gaules')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first <h1> tag
first_header = soup.find('h1')

print('First <h1> tag text:', first_header.text)

# Find all <a> tags (links)
all_links = soup.find_all('a')

print('All <a> tag hrefs:')
for link in all_links:
    print(link.get('href'))

# Access attributes of an element
first_link = all_links[0]

print('First link text:', first_link.text)
print('First link href:', first_link.get('href'))

# Navigate the DOM tree
# Example: Find a div with a specific class, then find a child element
specific_div = soup.find('div', class_='d-flex')

if specific_div:
    child_element = specific_div.find('span')

    if child_element:
        print('Text of child <span> in specific div:', child_element.text)
    else:
        print('No <span> tag found within the specific div with class "d-flex"')
else:
    print('Div with class "d-flex" not found')

# Navigate using parent and siblings
if first_header:
    parent_element = first_header.parent
    print('Parent of first <h1> tag:', parent_element.name)

    next_sibling = first_header.find_next_sibling()
    print('Next sibling of first <h1> tag:', next_sibling.name if next_sibling else 'No next sibling')
    

# Extracting data for storing
data_to_store = {
    'First_h1_tag': first_header.text,
    'First_link_text': first_link.text,
    'First_link_href': first_link.get('href')
}

# Storing data to a CSV file
csv_file = 'scraped_data.csv'

with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=data_to_store.keys())
    writer.writeheader()
    writer.writerow(data_to_store)

print('Data saved to CSV file:', csv_file)

# Storing data to MongoDB
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['scraping_db']
    collection = db['scraped_data']
    collection.insert_one(data_to_store)
    print('Data saved to MongoDB collection: scraped_data')
except Exception as e:
    print('Error:', e)
    print('Failed to connect to MongoDB. Exiting...')
    sys.exit(1)
