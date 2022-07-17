import requests
from bs4 import BeautifulSoup as bs
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to?Type the date in this format YYYY-MM-DD:")
URL = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(URL)
soup = bs(response.text,"html.parser")
# print(soup.prettify())
songs = soup.find_all(name = "h3", class_ = "a-no-trucate")
song_titles = [song.getText().strip() for song in songs]
print(song_titles)

# sp = spotipy.Spotify(
#     auth_manager = SpotifyOAuth(
#         scope = "playlist-modify-private",
#         redirect_uri = "http://127.0.0.1:5500/",
#         client_id = CLIENT_ID, 
#         client_secret = CLIENT_SECRET, 
#         show_dialog= True, 
#         cache_path = "token.txt"
#     )
# )

# user_id = sp.current_user()["id"]
# print(user_id)











# from bs4 import BeautifulSoup
# import requests
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# CLIENT_ID = "15ab52285b064b0dbaf14f954619a7ba"
# CLIENT_SECRET = "162f4576bb2a4640bfc53fa9590ef8c4"

# # Scraping Billboard 100
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.find_all("span", class_="chart-element__information__song")
# song_names = [song.getText() for song in song_names_spans]

# #Spotify Authentication
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="https://example.com",
#         client_id=CLIENT_ID,
#         client_secret=CLIENT_SECRET,
#         show_dialog=True,
#         cache_path="INTERMEDIATE/day46/token.txt"
#     )
# )
# user_id = sp.current_user()["id"]
# print(user_id)

# #Searching Spotify for songs by title
# song_uris = []
# year = date.split("-")[0]
# for song in song_names:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")

# #Creating a new private playlist in Spotify
# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

# #Adding songs found into the new playlist
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
