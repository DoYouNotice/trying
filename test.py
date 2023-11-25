import requests
from bs4 import BeautifulSoup
import os

# Function to scrape links from the specified HTML elements
def scrape_links(url, selector):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.select(selector)
    links = [element.get('href') for element in elements]
    return links

# Specify the URL and CSS selector
url = "https://geizhals.de/?cat=gra16_512"
selector = "tr.xf_tr:nth-child(4) > td:nth-child(3)"

# Scrape links
links = scrape_links(url, selector)

# Print the scraped links
print(f"Scraped links: {links}")

# Save the links to a file
file_path = "scraped_links.txt"  # You can adjust the file path as needed
with open(file_path, 'w') as file:
    for link in links:
        file.write(link + '\n')

# Print a message indicating the file path
print(f"Links saved to: {file_path}")
