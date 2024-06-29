from bs4 import BeautifulSoup
import requests
from pprint import pprint

#File_Path
file_path=r"DAY_45_Billboard Hot 100\top_100MoviesList.txt"

# Step 2: Construct the URL for the Billboard Hot 100 chart for the given date
url = f"https://www.empireonline.com/movies/features/best-movies-2/"

# Step 3: Fetch the webpage content
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve data. Please check the date format or try a different date.")
    exit(0)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser",)



# Find all elements that contain the movie titles
# Inspect the page to find the correct class or id for the song titles
# In this case, we assume the titles are within <h3> tags with a specific class

movies = soup.select("div h3", id='listicleItem_listicle-item__title__BfenH')
 
movies_list = [movie.get_text(strip=True) for movie in movies]

# Open the file in write mode
with open(file_path, "w", encoding='utf-8') as file:
    # Iterate through the movies_list in reverse order if needed
    for movie in movies_list[::-1]:
        # Write each movie to the file
        file.write(movie + "\n")