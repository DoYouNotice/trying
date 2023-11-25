import os
import requests
from bs4 import BeautifulSoup

url = "https://geizhals.de/?cat=gra16_512"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Select the desired elements using the specified CSS selector
    link_elements = soup.select('tr.xf_tr:nth-child(4) > td:nth-child(3) a')

    # Extract and print the links
    links = [link['href'] for link in link_elements]

    # Use a relative path for the output file
    output_path = os.path.join(os.getcwd(), "scraped_links.txt")

    # Save the links to a file
    with open(output_path, "w") as file:
        for link in links:
            file.write(link + "\n")

    print(f"Scraped links saved to '{output_path}'")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
