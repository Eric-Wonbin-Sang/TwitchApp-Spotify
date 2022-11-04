import io
import pygame
import requests

from General import Functions
from PygameClasses.EasyRect import EasyRect
from PygameClasses.EasyText import EasyText


class SongElement:

    missing_song_path = "resources/missing_song.jpg"
    spacer_constant = 5

    def __init__(self, song, screen):

        self.song = song
        self.screen = screen

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.dimension = self.screen_height - self.screen_height / self.spacer_constant

        # only generate if song changes
        self.image = self.get_image()
        self.transformed_image = self.get_transformed_image()
        self.image_rect = self.get_image_rect()
        self.name_rect = self.get_name_rect()
        self.artists_rect = self.get_artists_rect()
        self.playback_rect = self.get_playback_rect()
        self.time_text = self.get_time_text()

    def get_image(self):
        if self.song.image_url_list:
            r = requests.get(self.song.image_url_list[1]["url"])
            img = io.BytesIO(r.content)
            return pygame.image.load(img)
        return pygame.image.load(self.missing_song_path)

    def get_transformed_image(self):
        return pygame.transform.scale(self.image, (self.dimension, self.dimension))

    def get_image_rect(self):
        curr_image_rect = self.transformed_image.get_rect()
        curr_image_rect.center = (self.dimension / 2 + self.screen_height / (self.spacer_constant * 2),
                                  self.screen_height / 2)
        return curr_image_rect

    def get_name_rect(self):
        return EasyText(
            text=self.song.name,
            x=self.dimension + self.screen_height / self.spacer_constant,
            y=self.screen.get_height() / 4,
            size=self.screen.get_height() / 3.75,
            font_file="FontFolder/Product Sans Bold.ttf",
            color=(255, 255, 255),
            opacity=255,
            draw_center=False
        )

    def get_artists_rect(self):
        return EasyText(
            text=", ".join([x for x in self.song.artist_list]),
            x=self.dimension + self.screen_height / self.spacer_constant,
            y=self.screen_height - (self.screen_height / 2.5),
            size=self.screen_height / 5,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(255, 255, 255),
            opacity=140,
            draw_center=False
        )

    def get_playback_rect(self):
        return EasyRect(
            x=0,
            y=0,
            width=self.screen_width * self.song.curr_progress / self.song.duration,
            height=self.screen_height,
            color=(0, 175, 96 - 30),
            draw_center=False
        )

    def get_time_text(self):
        text = "{}/{}".format(Functions.milliseconds_to_minute_format(self.song.curr_progress),
                              Functions.milliseconds_to_minute_format(self.song.duration))
        return EasyText(
            text=text,
            x=0,
            y=self.screen_height * .8,
            size=self.screen_height / 5,
            font_file="FontFolder/Product Sans Regular.ttf",
            color=(255, 255, 255),
            opacity=140,
            draw_center=False
        )

    def update(self, song, screen):
        song.update(song)
        self.screen = screen
        self.song = song
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.dimension = int(self.screen_height - self.screen_height / self.spacer_constant)
        self.transformed_image = self.get_transformed_image()
        self.image_rect = self.get_image_rect()
        self.name_rect = self.get_name_rect()
        self.artists_rect = self.get_artists_rect()
        self.playback_rect = self.get_playback_rect()
        self.time_text = self.get_time_text()

    def draw_all(self):
        self.playback_rect.draw(self.screen)
        self.screen.blit(self.transformed_image, self.image_rect)
        self.name_rect.draw(self.screen)
        self.artists_rect.draw(self.screen)
        self.time_text.x = self.screen_width - self.time_text.rect.width - self.spacer_constant
        self.time_text.draw(self.screen)
