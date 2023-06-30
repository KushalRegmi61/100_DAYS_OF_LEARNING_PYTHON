from bs4 import BeautifulSoup
import requests
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()

import spotipy
from spotipy.oauth2 import SpotifyOAuth

#getting hold of spotify id and password
SPOTIFY_ID = os.getenv('SPOTIFY_ID')
SPOTIFY_SECRET = os.getenv('SPOTIFY_SECRET')
PLAYLIST_ENDPOINT=f"https://api.spotify.com/v1/users/Mr KuSH/playlists"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_ID,
    client_secret=SPOTIFY_SECRET,
    redirect_uri='http://example.com',
    scope='user-library-read'
))

token_info = sp.get_access_token()
access_token = token_info['access_token']
print(access_token)





# #TODO_1: Prompt the user for a date
# date = input("Enter the date you would like to travel to (YYYY-MM-DD): ")

# #TODO_2: Construct the URL for the Billboard Hot 100 chart for the given date
# url = f"https://www.billboard.com/charts/hot-100/{date}/"

# #TODO_3: Fetch the webpage content
# response = requests.get(url)
# if response.status_code != 200:
#     print("Failed to retrieve data. Please check the date format or try a different date.")
#     exit(0)

# # Create a BeautifulSoup object
# soup = BeautifulSoup(response.text, "html.parser")

# #TODO_4 CREATE A LIST OF TOP 100 SONG OF THAT WEEK
# songs = soup.select("li h3", id='title-of-a-story') 
# songs_list = [song.get_text(strip=True) for song in songs]
# pprint(songs_list)

