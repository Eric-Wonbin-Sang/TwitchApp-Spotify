import pygame

from classes.gui_helpers.Resizer import Resizer
from classes.gui_helpers.SongElement import SongElement

from General import Constants


class SpotifyGUI:

    """
    This is the main logic for the GUI.

    Note:
        The key_dict is basically code duplication for optimization's sake. Better to
        Create the dictionary dynamically. TODO
    """

    app_name = Constants.app_name
    app_logo_path = "Twitchy Logo.png"

    display_width = Constants.display_width
    display_height = Constants.display_height

    def __init__(self, system_type):

        self.system_type = system_type

        pygame.init()
        pygame.display.set_caption(self.app_name)
        pygame.display.set_icon(pygame.image.load(self.app_logo_path))

        self.screen = pygame.display.set_mode([self.display_width, self.display_height], pygame.NOFRAME)
        self.hwnd = pygame.display.get_wm_info()["window"]

        self.resizer = Resizer(self.hwnd, self.system_type)
        self.song_element = None

    def update_and_draw(self, song):
        if self.song_element is None or self.song_element.song != song:
            self.song_element = SongElement(song, self.screen)
        else:
            self.song_element.update(song, self.screen)
        self.screen.fill((23, 23, 23))
        self.song_element.draw_all()
