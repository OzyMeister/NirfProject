import requests
from bs4 import BeautifulSoup
import os
import urllib.request

url = "https://www.nirfindia.org/2022/EngineeringRanking.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract all links from the webpage
links = [a["href"] for a in soup.find_all("a", href=True)]

# Filter redirectable links by checking if the links start with "http"
redirectable_links = [link for link in links if link.startswith("http")]

# Filter links that end with ".png"
png_links = [link for link in redirectable_links if link.endswith(".png")]

# Create a folder to save the images
folder_name = "22images"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Download and save the images
counter = 1  # Initialize the counter
for link in png_links:
    filename = f"{counter}.png"  # Set the filename to the counter value plus the .png extension
    urllib.request.urlretrieve(link, f"{folder_name}/{filename}")  # Download the image and save it with the filename
    counter += 1  # Increment the counter for the next image
