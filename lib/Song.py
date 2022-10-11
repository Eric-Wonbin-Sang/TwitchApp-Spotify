import datetime

from lib import Artist

from General import Functions


class Song:

    def __init__(self, spotipy_client, **kwargs):

        self.spotipy_client = spotipy_client
        self.current_song_dict = kwargs.get("current_song_dict")
        self.last_time_updated = datetime.datetime.now()

        self.name = self.current_song_dict["item"]["name"] if self.current_song_dict["item"] else "No song playing"
        self.id = self.current_song_dict["item"]["id"] if self.current_song_dict else None
        self.artist_list = self.get_artist_list()
        self.image_list = self.get_image_list()
        self.is_playing = self.current_song_dict["is_playing"] if self.current_song_dict else None
        self.current_placement = self.current_song_dict["progress_ms"] if self.current_song_dict else 0
        self.duration = self.current_song_dict["item"]["duration_ms"] if self.current_song_dict else 1

        self.analysis = self.get_analysis()

    def get_artist_list(self):
        artist_list = []
        if self.current_song_dict:
            for artist_dict in self.current_song_dict["item"]["album"]["artists"]:
                artist_list.append(Artist.Artist(**artist_dict))
        return artist_list

    def get_image_list(self):
        image_list = []
        if self.current_song_dict:
            for x in self.current_song_dict["item"]["album"]["images"]:
                image_list.append(x)
        return image_list

    def get_analysis(self):
        # data_dict = self.spotipy_client.audio_analysis(self.id)
        # pp = pprint.PrettyPrinter(indent=4)
        # print(self.duration)
        # for key, value in data_dict.items():
        #     if type(value) == list:
        #         print(key, len(value))
        #     else:
        #         print(key, str(value)[:50])
        # # pp.pprint(data_dict)
        # exit()
        pass

    def simple_player_str(self):
        return Functions.str_to_length(
                "{} by {}".format(
                    self.name,
                    ", ".join([x.name for x in self.artist_list])
                ),
                30
            ) + \
            "[" + Functions.str_to_length(int((self.current_placement / self.duration) * 30) * "-", 30,
                                          do_dots=False) + "]"

    def __str__(self):
        return "{} by [{}] - {} out of {} ms".format(
            self.name,
            ", ".join([x.name for x in self.artist_list]),
            self.current_placement,
            self.duration
        )
