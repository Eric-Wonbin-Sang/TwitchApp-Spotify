import pprint

from General import Functions


class Song:

    def __init__(self, data_dict):

        self.data_dict = data_dict

        self.name = Functions.get_dict_data(self.data_dict, "item", "name")
        self.is_playing = self.data_dict.get("is_playing")
        self.curr_progress = self.data_dict.get("progress_ms")
        self.duration = Functions.get_dict_data(self.data_dict, "item", "duration_ms")
        self.artist_list = self.get_artist_list()
        self.image_url_list = self.get_image_url_list()

        # self.playlist_name
        # self.album_name

    def get_artist_list(self):
        artists_dict_list = Functions.get_dict_data(self.data_dict, "item", "album", "artists") or []
        return [artist_dict.get("name") for artist_dict in artists_dict_list]

    def get_image_url_list(self):
        return Functions.get_dict_data(self.data_dict, "item", "album", "images") or []

    @staticmethod
    def get_song(spotipy_client):
        if data_dict := spotipy_client.currently_playing():
            return Song(data_dict)

    def __str__(self):
        return f"Song(name={self.name}, is_playing={self.is_playing}, curr_progress={self.curr_progress}, " \
               f"duration={self.duration}, artist_list={self.artist_list}, image_url_list={self.image_url_list})"
