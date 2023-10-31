from bs4 import BeautifulSoup
import requests
from config import Config

config =Config()

SPOTIFY_CLIENT_ID = config.SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_SECRET = config.SPOTIFY_CLIENT_SECRET
REDIRECT_URI = config.REDIRECT_URI
OAUTH_AUTHORIZE_URL = config.OAUTH_AUTHORIZE_URL
OAUTH_TOKEN_URL = config.OAUTH_TOKEN_URL
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="xovt0v47ddcfzo7gs5v5k95cn",
    )
)
user_id = sp.current_user()["id"]
year = input("which year do you want to travel to? type date in 'YYYY-MM-DD' format.")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}/")
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")


song_tags = soup.findAll(name="h3", id="title-of-a-story", class_="a-no-trucate" )
artist_tags = soup.findAll(name="span", class_="a-no-trucate" )
song_list = []
artist_list = []
for song in song_tags:
    s = song.getText()
    s = s.strip()
    song_list.append(s)
for artist in artist_tags:
    s = artist.getText()
    s = s.strip()
    artist_list.append(s)


song_uris = []
for song in song_list:
    result = sp.search(q=f"track:{song}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except:
        print(f"{song} doesn't exist in Spotify. Skipped.")
print(f"Number of songs found: {len(song_uris)}")
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False, )
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"New playlist '{year} Billboard 100' successfully created on Spotify!")