import pygame

from classes.spotify.Song import Song


class MissingSong(Song):

    missing_song_path = "missing_song.jpg"

    def __init__(self):

        super().__init__({})

        self.name = "No song"
        self.is_playing = False
        self.curr_progress = 0
        self.duration = 100
        self.artist_list = ["No Artist"]

    def get_song_image(self):
        return pygame.image.load(self.missing_song_path)
