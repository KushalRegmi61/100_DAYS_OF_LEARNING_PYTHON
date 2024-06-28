from bs4 import BeautifulSoup
import requests
from pprint import pprint

# Step 1: Prompt the user for a date
date = input("Enter the date you would like to travel to (YYYY-MM-DD): ")

# Step 2: Construct the URL for the Billboard Hot 100 chart for the given date
url = f"https://www.billboard.com/charts/hot-100/{date}/"

# Step 3: Fetch the webpage content
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve data. Please check the date format or try a different date.")
    exit(0)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Find all elements that contain the song titles
# Inspect the page to find the correct class or id for the song titles
# In this case, we assume the titles are within <h3> tags with a specific class

songs = soup.select("li h3", id='title-of-a-story')
 
songs_list = [song.get_text(strip=True) for song in songs]
print(f"\n\t\tThe Top 100 Songs of {date} are:\n")
pprint(songs_list)