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

    # Extract the links
    links = [link['href'] for link in link_elements]

    # Save the links to a file
    with open('scraped_links.txt', 'w') as file:
        for link in links:
            file.write(link + '\n')
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
