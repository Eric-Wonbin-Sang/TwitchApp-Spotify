import spotipy
import requests
import threading

from classes.spotify.Song import Song
from lib import SpotifyLib

from General import Functions, Constants


class SongInfoProducer(threading.Thread):

    def __init__(self, thread_id, name, queue):

        threading.Thread.__init__(self)

        self.thread_id = thread_id
        self.name = name
        self.queue = queue

        self.spotipy_client = self.get_spotipy_client()

    @staticmethod
    def get_spotipy_client():
        spotify_credentials_dict = Functions.parse_json(Constants.spotify_credentials_file_path)
        scope = "user-read-currently-playing"
        redirect_uri = "http://localhost:44444/callback"
        return SpotifyLib.get_spotipy_client(
            client_id=spotify_credentials_dict["client_id"],
            client_secret=spotify_credentials_dict["secret"],
            scope=scope,
            redirect_uri=redirect_uri
        )

    def get_currently_playing_song(self):
        try:
            if song := Song.get_song(self.spotipy_client):
                return song
        except spotipy.exceptions.SpotifyException:
            pass
        except requests.exceptions.ReadTimeout:
            pass
        except Exception as e:
            print("Exception occurred: {}".format(e))

    def run(self):
        while True:
            if song := self.get_currently_playing_song():
                self.queue.put(song)
