import os
import pygame
import datetime
import urllib.request

from lib import SpotifyLib
from PygameClasses import EasyRect, EasyText

from General import Constants


class SpotifyGUI:

    def __init__(self, song, screen):

        self.song = song
        self.screen = screen

        self.spacer_constant = 5

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.dimension = int(self.screen_height - self.screen_height / self.spacer_constant)

        self.song_image = self.get_song_image()
        self.transformed_song_image = self.get_transformed_song_image()
        self.song_image_rect = self.get_song_image_rect()
        self.song_name_rect = self.get_song_name_rect()
        self.song_artists_rect = self.get_song_artists_rect()
        self.song_playback_rect = self.get_song_playback_rect()

    def get_song_image(self):
        image_path = "song_image.jpg"
        if os.path.exists(image_path):
            os.remove(image_path)
        urllib.request.urlretrieve(self.song.image_list[1]["url"], image_path)
        return pygame.image.load(image_path)

    def get_transformed_song_image(self):
        return pygame.transform.scale(self.song_image, (self.dimension, self.dimension))

    def get_song_image_rect(self):
        curr_image_rect = self.transformed_song_image.get_rect()
        curr_image_rect.center = (self.dimension / 2 + self.screen_height / (self.spacer_constant * 2),
                                  self.screen_height / 2)
        return curr_image_rect

    def get_song_name_rect(self):
        return EasyText.EasyText(
            text=self.song.name,
            x=self.dimension + self.screen_height / self.spacer_constant,
            y=self.screen.get_height() / 4,
            size=self.screen.get_height() / 3.75,
            font_file="FontFolder/Product Sans Bold.ttf",
            color=(255, 255, 255),
            opacity=255,
            draw_center=False
        )

    def get_song_artists_rect(self):
        return EasyText.EasyText(
            text=", ".join([x.name for x in self.song.artist_list]),
            x=self.dimension + self.screen_height / self.spacer_constant,
            y=self.screen_height - (self.screen_height / 2.5),
            size=self.screen_height / 5,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(255, 255, 255),
            opacity=140,
            draw_center=False
        )

    def get_song_playback_rect(self):
        return EasyRect.EasyRect(
            x=0,
            y=0,
            width=self.screen_width * self.song.current_placement / self.song.duration,
            height=self.screen_height,
            color=(0, 175, 96 - 30),
            draw_center=False
        )

    def update_song(self):
        if (datetime.datetime.now() - self.song.last_time_updated).seconds > Constants.song_update_time:
            new_song = SpotifyLib.get_currently_playing_song(self.song.spotipy_client)
            if new_song.id != self.song.id:
                self.song = new_song
                self.song_image = self.get_song_image()
            else:
                self.song = new_song

    def update(self):

        self.update_song()

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.dimension = int(self.screen_height - self.screen_height / self.spacer_constant)

        self.transformed_song_image = self.get_transformed_song_image()
        self.song_image_rect = self.get_song_image_rect()
        self.song_name_rect = self.get_song_name_rect()
        self.song_artists_rect = self.get_song_artists_rect()
        self.song_playback_rect = self.get_song_playback_rect()

    def draw(self):
        self.song_playback_rect.draw(self.screen)
        self.screen.blit(self.transformed_song_image, self.song_image_rect)
        self.song_name_rect.draw(self.screen)
        self.song_artists_rect.draw(self.screen)
