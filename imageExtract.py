import requests # importing requests library to make a GET request to the webpage
from bs4 import BeautifulSoup # importing BeautifulSoup library to parse the HTML 
import os # importing os library to create the folder 
import urllib.request # importing urllib.request library to open the links and save the images

url = "https://www.nirfindia.org/2022/EngineeringRanking.html" # the url of the webpage
response = requests.get(url) # making a GET request to the webpage
soup = BeautifulSoup(response.content, "html.parser") # parsing the HTML

# Extract all links from the webpage
links = [a["href"] for a in soup.find_all("a", href=True)] 

# Filter redirectable links by checking if the links start with "http"l 
redirectable_links = [link for link in links if link.startswith("http")] 

# Filter links that end with ".png"
png_links = [link for link in redirectable_links if link.endswith(".png")]

# Create a folder to save the images
folder_name = "22images"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Download and save the images
for link in png_links:
    filename = link.split("/")[-1] # Extracting the file name from the link
    urllib.request.urlretrieve(link, f"{folder_name}/{filename}") # Downloading the image and saving it to the folder with the extracted file name