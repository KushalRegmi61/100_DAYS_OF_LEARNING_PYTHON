from bs4 import BeautifulSoup
import requests
from pprint import pprint
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from spotipy.exceptions import SpotifyException
import json
import traceback

load_dotenv()

#TODO_1: Prompt the user for a date
date = input("Enter the date you would like to travel to (YYYY-MM-DD): ")
year = date.strip()[:4]


#TODO_2: Construct the URL for the Billboard Hot 100 chart for the given date
url = f"https://www.billboard.com/charts/hot-100/{date}/"

#TODO_3: Fetch the webpage content
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve data. Please check the date format or try a different date.")
    exit(0)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

#TODO_4 CREATE A LIST OF TOP 100 SONG OF THAT WEEK
songs = soup.select("li h3", id='title-of-a-story') 
songs_list = [song.get_text(strip=True) for song in songs]


# #getting hold of spotify id and password
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_ID')
SPOTIFY_SECRET = os.getenv('SPOTIFY_SECRET')
SPOTIFY_USERID=os.getenv('SPOTIFY_USERID')

#TODO_6 VERYFYING THE  SPOTIFY_ID 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               redirect_uri='http://example.com',
                                               scope='user-read-private'))

user_id = sp.current_user()['id']

with open(r".cache","r") as file:
    contents= json.loads(file.read())
    
#Bearer Token:
SPOTIFY_TOKEN=f"Bearer {contents.get('access_token')}"

#TODO_7 SEARCHING THE FOR THE SONGS IN THE SPOTIFY AND CREATING  SONG LINKS LIST 

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIFY_CLIENT_ID, SPOTIFY_SECRET))
song_uris_list = []

for name in songs_list[:100:1]:
    try:
        query = f'track: {name} year: {year}'
        results = spotify.search(q=query, type='track', limit=1)
        tracks = results['tracks']['items']
        if tracks:
            song_uris_list.append(tracks[0]['uri'])
        else:
            print(f"Song '{name}' from year {year} not found on Spotify.")
    except Exception as e:
        print(f"An error occurred for '{name}' from year {year}: {e}")
        traceback.print_exc()
        
# pprint(song_uris_list)


#TODO_8 : CREATING A NEW PLAYLIST IN THE SPOTIFY
# Set up your credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_SECRET,
        redirect_uri='http://example.com',
        scope="playlist-modify-private"
    ))


try:
    # Retrieve the current user's ID
    user_id = sp.current_user()["id"]

    # Create a new private playlist
    playlist_name = f"{date} Billboard 100"
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

    # Retrieve the new playlist ID
    playlist_id = playlist['id']

    print(f"Playlist '{playlist_name}' created successfully! Playlist ID: {playlist_id}")

except SpotifyException as e:
    print(f"An error occurred: {e}")
    if e.http_status == 401:
        print("Authentication failed. Please check your credentials.")
    else:
        print("An unexpected error occurred while creating the playlist.")



#TODO_9 : ADDING TRACKS TO THE PLAYLIST
sp.user_playlist_add_tracks(user=SPOTIFY_USERID, playlist_id=playlist_id, tracks=song_uris_list)




