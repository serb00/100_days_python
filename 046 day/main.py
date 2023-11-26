import datetime as dt
import os

from tqdm import tqdm
from bs4 import BeautifulSoup
import requests
from spotipy import oauth2, client
import calendar

REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-public"
CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")


def connect_to_spotify():
    connection = client.Spotify(auth_manager=oauth2.SpotifyOAuth(client_id=CLIENT_ID,
                                                                 client_secret=CLIENT_SECRET,
                                                                 redirect_uri=REDIRECT_URI,
                                                                 scope=SCOPE,
                                                                 show_dialog=True))
    return connection


def get_song_uri(connection, song_title, song_artist, year):
    search_query = f"track:{song_title} year:{year} artist:{song_artist}"

    search_result = connection.search(q=search_query, type='track')
    dict_of_songs = search_result['tracks']['items']
    if len(dict_of_songs) == 0:
        return None
    song_uri = dict_of_songs[0]['uri']
    return song_uri


def create_playlist(connection, playlist_name):
    user_id = connection.current_user()['id']
    playlist = connection.user_playlist_create(user=user_id, name=playlist_name, public=True)
    return playlist['id']


def add_songs_to_playlist(connection, p_id, list_uri):
    connection.playlist_add_items(playlist_id=p_id, items=list_uri)


def ask_for_date():
    while True:
        try:
            user_input = input('Please enter a date in the format YYYY-MM-DD: ')
            given_date = dt.datetime.strptime(user_input, '%Y-%m-%d')
            return given_date
        except ValueError:
            print('Please enter a valid date following the format YYYY-MM-DD:')
            continue


def scrape_music_titles_for_date(from_date):
    url = f"https://www.billboard.com/charts/hot-100/{from_date.date()}"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    all_song_titles = soup.select(selector='li .o-chart-results-list__item h3')

    all_song_artists = soup.select(selector='li .o-chart-results-list__item h3 + span')

    return [{'chart_no': chart_num + 1,
             'title': title.getText().strip(),
             'artist': artist.getText().strip()
             } for title, artist, chart_num in zip(all_song_titles, all_song_artists, range(100))]


def get_playlist_link(p_id):
    return f"https://open.spotify.com/playlist/{p_id}"


if __name__ == '__main__':
    date = ask_for_date()
    spotify_connection = connect_to_spotify()
    list_of_music_titles = scrape_music_titles_for_date(date)
    print(f"We found {len(list_of_music_titles)} best songs on {calendar.month_name[date.month]} {date.year}")
    playlist_id = create_playlist(spotify_connection, f"Top 100 Songs of {calendar.month_name[date.month]} {date.year}")
    added, skipped = 0, 0
    song_uris = []
    with tqdm(total=len(list_of_music_titles), desc="Searching songs", unit="song",
              ncols=100, colour="green") as pbar:
        for song in list_of_music_titles:
            uri = get_song_uri(connection=spotify_connection,
                               song_title=song['title'],
                               song_artist=song['artist'],
                               year=date.year)
            if uri is None:
                skipped += 1
                pbar.update(1)
                continue
            song_uris.append(uri)
            added += 1
            pbar.update(1)

    add_songs_to_playlist(spotify_connection, playlist_id, song_uris)

    print(f"Added {added} songs to the playlist. Skipped {skipped} songs.")
    print(f"Playlist link: {get_playlist_link(playlist_id)}")
