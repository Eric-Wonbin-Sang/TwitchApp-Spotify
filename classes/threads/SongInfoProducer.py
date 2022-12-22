import spotipy
import requests

from threading import Thread, Event

from classes.spotify.Song import Song
from classes.spotify.MissingSong import MissingSong

from General import Functions, Constants


class SongInfoProducer(Thread):

    song_save_count = 4
    missing_song = MissingSong()

    def __init__(self, thread_id, name, queue, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.thread_id = thread_id
        self.name = name
        self.queue = queue
        self.kill_event = Event()

        self.song_list = []

        self.spotipy_client = self.get_spotipy_client()

    @staticmethod
    def get_spotipy_client():
        spotify_credentials_dict = Functions.parse_json(Constants.spotify_credentials_file_path)
        auth_manager = spotipy.SpotifyOAuth(
            client_id=spotify_credentials_dict["client_id"],
            client_secret=spotify_credentials_dict["secret"],
            scope="user-read-currently-playing",    # user-read-playback-state
            redirect_uri="http://localhost:44444/callback")
        return spotipy.Spotify(auth_manager=auth_manager)

    def get_currently_playing_song(self):
        try:
            if song := Song.get_song(self.spotipy_client):
                self.song_list.append(song)
                return song
        except spotipy.exceptions.SpotifyException or requests.exceptions.ReadTimeout:
            return self.missing_song
        except Exception as e:
            print("Exception occurred: {}".format(e))
        return self.missing_song

    def run(self):
        while not self.kill_event.is_set():
            if song := self.get_currently_playing_song():
                self.queue.put(song)

    def stop(self):
        self.join()
