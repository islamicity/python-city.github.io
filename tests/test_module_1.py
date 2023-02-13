import requests
from bs4 import BeautifulSoup

# send a request to the website and retrieve the HTML content
url = "https://gic.islamicity.tv"
response = requests.get(url)
html_content = response.text

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# extract the information you want from the HTML content
# in this case, let's extract the title of the page
title = soup.find("title").text

# print the extracted information
print("Title:", title)
