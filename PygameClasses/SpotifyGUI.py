import pygame

from classes.gui_helpers.Resizer import Resizer
from classes.keys.Key import Key
from classes.keys.ComboKey import ComboKey
from classes.keys.MouseKey import MouseKey
from classes.gui_helpers.SongElement import SongElement


class SpotifyGUI:

    """
    This is the main logic for the GUI.

    Note:
        The key_dict is basically code duplication for optimization's sake. Better to
        Create the dictionary dynamically. TODO
    """

    app_name = "Twitchy2"
    app_logo_path = "Twitchy Logo.png"

    display_width = 700
    display_height = 120

    key_dict = {
        "w": Key("w"),
        "a": Key("a"),
        "s": Key("s"),
        "d": Key("d"),
        "ctrl": ComboKey("ctrl", "left ctrl", "right ctrl"),
        "q": Key("q"),
        "mouse": MouseKey("mouse")
    }

    def __init__(self):

        pygame.init()
        pygame.display.set_caption(self.app_name)
        pygame.display.set_icon(pygame.image.load(self.app_logo_path))

        self.screen = pygame.display.set_mode([self.display_width, self.display_height], pygame.NOFRAME)
        self.hwnd = pygame.display.get_wm_info()["window"]

        self.resizer = Resizer(self.hwnd, self.key_dict)
        self.song_element = None

    def update_and_draw(self, song):
        if self.song_element is None or self.song_element.song != song:
            self.song_element = SongElement(song, self.screen)
        else:
            self.song_element.update(song, self.screen)
        self.screen.fill((23, 23, 23))
        self.song_element.draw_all()
