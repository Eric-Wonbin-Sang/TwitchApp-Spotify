import time
import pygame
import datetime
import urllib.request

from lib import SpotifyLib
from PygameClasses import EasyText, EasyRect

from General import Functions, Constants


def main():

    spotify_credentials_dict = Functions.parse_json(Constants.spotify_credentials_file_path)
    scope = "user-read-currently-playing"
    redirect_uri = "http://localhost:44444/callback"

    spotipy_client = SpotifyLib.get_spotipy_client(
        client_id=spotify_credentials_dict["client_id"],
        client_secret=spotify_credentials_dict["secret"],
        scope=scope,
        redirect_uri=redirect_uri
    )

    pygame.init()
    pygame.font.init()
    display_height = 150
    display_width = 800
    song = SpotifyLib.get_currently_playing_song(spotipy_client)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([display_width, display_height], pygame.RESIZABLE, pygame.NOFRAME)

    image = None
    curr_image_rect = None
    song_name = None
    song_artists = None
    song_playback = None
    last_time_updated = datetime.datetime.now()

    while True:

        if (datetime.datetime.now() - last_time_updated).seconds > 1:
            song = SpotifyLib.get_currently_playing_song(spotipy_client)

            urllib.request.urlretrieve(song.image_list[1]["url"], "image.jpg")

            screen_height = screen.get_height()
            screen_width = screen.get_width()

            spacer_constant = 5

            image = pygame.image.load("image.jpg").convert()
            dimension = int(screen_height - screen_height/spacer_constant)
            image = pygame.transform.scale(image, (dimension, dimension))

            curr_image_rect = image.get_rect()
            curr_image_rect.center = (dimension/2 + screen_height/(spacer_constant * 2), screen.get_height()/2)

            song_name = EasyText.EasyText(
                text=song.name,
                x=dimension + screen_height/spacer_constant,
                y=screen_height/4,
                size=40,
                font_file="FontFolder/Product Sans Bold.ttf",
                color=(255, 255, 255),
                opacity=255,
                draw_center=False
            )
            song_artists = EasyText.EasyText(
                text=", ".join([x.name for x in song.artist_list]),
                x=dimension + screen_height / spacer_constant,
                y=screen_height - (screen_height / 2.5),
                size=30,
                font_file="FontFolder/Product Sans Regular.ttf",
                color=(255, 255, 255),
                opacity=140,
                draw_center=False
            )
            song_playback = EasyRect.EasyRect(
                x=0,
                y=0,
                width=screen_width * song.current_placement / song.duration,
                height=screen_height,
                color=(1, 130, 27),
                draw_center=False
            )
            last_time_updated = datetime.datetime.now()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        if curr_image_rect:
            screen.fill((23, 23, 23))
            song_playback.draw(screen)
            screen.blit(image, curr_image_rect)
            song_name.draw(screen)
            song_artists.draw(screen)

        pygame.display.update()
        clock.tick(30)


main()
