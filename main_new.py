import time
import queue

from classes.keys.ComboKey import ComboKey
from classes.keys.Key import Key
from classes.threads.SongInfoProducer import SongInfoProducer


import pygame

from lib import SpotifyLib
from PygameClasses import SpotifyGUI
from classes import WindowsMouse

from General import Functions, Constants


key_list = [
    Key("w"),
    Key("a"),
    Key("s"),
    Key("d"),
    ComboKey("ctrl", "left ctrl", "right ctrl")
]


def try_resize(key_list, window_adjust):
    """ Only triggers when control is held.

    TODO: Extremely inefficient. Like beyond acceptableness.
    """
    w, h = pygame.display.get_surface().get_size()
    if Key.find_key(key_list, "ctrl").is_pressed:
        if Key.find_key(key_list, "w").is_pressed:
            pygame.display.set_mode((w, h - window_adjust), pygame.NOFRAME)
        elif Key.find_key(key_list, "a").is_pressed:
            pygame.display.set_mode((w - window_adjust, h), pygame.NOFRAME)
        elif Key.find_key(key_list, "s").is_pressed:
            pygame.display.set_mode((w, h + window_adjust), pygame.NOFRAME)
        elif Key.find_key(key_list, "d").is_pressed:
            pygame.display.set_mode((w + window_adjust, h), pygame.NOFRAME)


def main():

    song_info_queue = queue.Queue(1)

    song_info_producer = SongInfoProducer(1, "spotify", song_info_queue)
    song_info_producer.start()

    pygame.init()
    display_width, display_height = 700, 120
    pygame.display.set_caption("Twitchy2")
    pygame.display.set_icon(pygame.image.load("Twitchy Logo.png"))
    screen = pygame.display.set_mode([display_width, display_height], pygame.NOFRAME)
    mouse = WindowsMouse.WindowsMouse()
    hwnd = pygame.display.get_wm_info()["window"]

    spotify_gui = None

    window_adjust = Constants.window_adjust
    drag = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.NOFRAME)
            if event.type == pygame.MOUSEBUTTONDOWN:
                drag = True
            if event.type == pygame.MOUSEBUTTONUP:
                drag = False

            for key in key_list:
                key.update(event)
            try_resize(key_list, window_adjust)

        try:
            mouse.update()
        except:
            pass

        if drag:
            x_delta, y_delta = mouse.x - mouse.prev_x, mouse.y - mouse.prev_y
            w, h = pygame.display.get_surface().get_size()
            Functions.alter_window(hwnd, x_delta=x_delta, y_delta=y_delta, width=w, height=h)

        try:
            song = song_info_queue.get(block=False)
            if not spotify_gui:
                spotify_gui = SpotifyGUI.SpotifyGUI(song=song, screen=screen)
            spotify_gui.update(new_song_info=song)
        except queue.Empty:
            ...

        screen.fill((23, 23, 23))
        if spotify_gui:
            spotify_gui.draw()

        pygame.display.update()


if __name__ == "__main__":
    main()
