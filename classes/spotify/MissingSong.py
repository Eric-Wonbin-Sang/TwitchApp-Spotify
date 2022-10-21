from classes.spotify.Song import Song


class MissingSong(Song):

    """
    A class to show no song.

    Note:
        I wish missing_song_path was here along with a custom get_image method,
        but it seems like I overestimated what method overriding does. It seems
        like methods used in the initializer don't override until the object is
        initialized. Might need to look more into this. TODO

    """

    def __init__(self):

        super().__init__({})

        self.name = "No song"
        self.is_playing = False
        self.curr_progress = 0
        self.duration = 100
        self.artist_list = ["No Artist"]
