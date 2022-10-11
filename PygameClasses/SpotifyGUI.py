import os
import pygame
import datetime
import urllib.request

from lib import SpotifyLib
from PygameClasses import EasyRect, EasyText

from General import Functions, Constants


class SpotifyGUI:

    def __init__(self, song, screen):

        self.song = song
        self.screen = screen

        self.spacer_constant = 5

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.dimension = int(self.screen_height - self.screen_height / self.spacer_constant)

        self.missing_song_path = "missing_song.jpg"
        self.song_image = self.get_song_image()
        self.transformed_song_image = self.get_transformed_song_image()
        self.song_image_rect = self.get_song_image_rect()
        self.song_name_rect = self.get_song_name_rect()
        self.song_artists_rect = self.get_song_artists_rect()
        self.song_playback_rect = self.get_song_playback_rect()

        self.song_time_text = self.get_song_time_text()

    def get_song_image(self):
        image_path = "song_image.jpg"
        if os.path.exists(image_path):
            os.remove(image_path)
        if self.song.image_url_list:
            urllib.request.urlretrieve(self.song.image_url_list[1]["url"], image_path)
            return pygame.image.load(image_path)
        return pygame.image.load(self.missing_song_path)

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
            text=", ".join([x for x in self.song.artist_list]),
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
            width=self.screen_width * self.song.curr_progress / self.song.duration,
            height=self.screen_height,
            color=(0, 175, 96 - 30),
            draw_center=False
        )

    def get_song_time_text(self):
        text = "{}/{}".format(Functions.milliseconds_to_minute_format(self.song.curr_progress),
                              Functions.milliseconds_to_minute_format(self.song.duration))
        return EasyText.EasyText(
            text=text,
            x=0,
            y=self.screen_height * .8,
            size=self.screen_height / 5,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(255, 255, 255),
            opacity=140,
            draw_center=False
        )

    def draw_song_time_text(self):
        self.song_time_text.x = self.screen_width - self.song_time_text.rect.width - self.spacer_constant
        self.song_time_text.draw(self.screen)

    def update_song(self):
        if (datetime.datetime.now() - self.song.last_time_updated).microseconds > Constants.song_update_time:

            temp_time = datetime.datetime.now()

            new_song = SpotifyLib.get_currently_playing_song(self.song.spotipy_client)
            if new_song.id != self.song.id:
                self.song = new_song
                self.song_image = self.get_song_image()
            else:
                self.song = new_song

            microsec = (datetime.datetime.now() - temp_time).microseconds
            if microsec > Constants.song_update_time:
                print("{} - Song refresh time: {} seconds".format(datetime.datetime.now(), microsec / 1000000))

    def update(self, new_song_info=None):

        if new_song_info:
            self.song = new_song_info

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.dimension = int(self.screen_height - self.screen_height / self.spacer_constant)

        self.transformed_song_image = self.get_transformed_song_image()
        self.song_image_rect = self.get_song_image_rect()
        self.song_name_rect = self.get_song_name_rect()
        self.song_artists_rect = self.get_song_artists_rect()
        self.song_playback_rect = self.get_song_playback_rect()
        self.song_time_text = self.get_song_time_text()

    def draw(self):
        self.song_playback_rect.draw(self.screen)
        self.screen.blit(self.transformed_song_image, self.song_image_rect)
        self.song_name_rect.draw(self.screen)
        self.song_artists_rect.draw(self.screen)
        self.draw_song_time_text()
