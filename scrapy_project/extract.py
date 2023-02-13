import requests
from bs4 import BeautifulSoup

# send a request to the website and retrieve the HTML content
url = "https://gic.islamicity.tv/tamankuliner"
response = requests.get(url)
html_content = response.text

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# extract all the links from the HTML content
links = []
for link in soup.find_all("a"):
    href = link.get("href")
    links.append(href)

# print the extracted links
print("Links:", links)
