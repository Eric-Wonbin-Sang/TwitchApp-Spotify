import spotipy
import requests

from lib import Song


def get_spotipy_client(client_id, client_secret, scope, redirect_uri):
    auth_manager = spotipy.SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        scope=scope,
        redirect_uri=redirect_uri)
    return spotipy.Spotify(auth_manager=auth_manager)


def get_currently_playing_song(spotipy_client):
    try:
        current_song_dict = spotipy_client.currently_playing()
        return Song.Song(
            spotipy_client=spotipy_client,
            current_song_dict=current_song_dict
        )
    except spotipy.exceptions.SpotifyException:
        pass
    except requests.exceptions.ReadTimeout:
        pass
    except Exception as e:
        print("Exception occurred: {}".format(e))
