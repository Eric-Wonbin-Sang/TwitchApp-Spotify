import pygame

from classes.gui_helpers.Resizer import Resizer
from classes.keys.Key import Key
from classes.keys.ComboKey import ComboKey
from classes.keys.MouseKey import MouseKey
from classes.gui_helpers.SongElement import SongElement
from classes.gui_helpers.RollingAverageNumber import RollingAverageNumber

from General import Functions, Constants


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

    window_adjust = Constants.window_adjust
    window_adjust_x_multiplier = Constants.window_adjust_x_multiplier
    window_adjust_y_multiplier = Constants.window_adjust_y_multiplier

    x_ran = RollingAverageNumber(10)
    y_ran = RollingAverageNumber(10)

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

    def process_keys(self):
        """ Only triggers when control is held. """

        self.key_dict["mouse"].update_position()

        # def change_dimensions(width_delta=0, height_delta=0):
        #     """ TODO: Optimize so w and h isn't called a bunch of times. """
        #     w, h = pygame.display.get_surface().get_size()
        #     if w + width_delta > 10 and h + height_delta > 10:
        #         pygame.display.set_mode((w + width_delta, h + height_delta), pygame.NOFRAME)
        #
        # if self.key_dict["ctrl"].is_pressed:
        #     if self.key_dict["w"].is_pressed:
        #         change_dimensions(height_delta=self.y_ran.add(-self.window_adjust * self.window_adjust_y_multiplier).get_value())
        #     if self.key_dict["a"].is_pressed:
        #         change_dimensions(width_delta=self.x_ran.add(-self.window_adjust * self.window_adjust_x_multiplier).get_value())
        #     if self.key_dict["s"].is_pressed:
        #         change_dimensions(height_delta=self.y_ran.add(self.window_adjust * self.window_adjust_y_multiplier).get_value())
        #     if self.key_dict["d"].is_pressed:
        #         change_dimensions(width_delta=self.x_ran.add(self.window_adjust * self.window_adjust_y_multiplier).get_value())
        #     if self.key_dict["q"].is_pressed:
        #         pygame.quit()
        # else:
        #     self.x_ran.add(0)
        #     self.y_ran.add(0)
        # if self.key_dict["mouse"].is_pressed:
        #     x_delta, y_delta = self.key_dict["mouse"].x - self.key_dict["mouse"].prev_x, \
        #                        self.key_dict["mouse"].y - self.key_dict["mouse"].prev_y
        #     width, height = pygame.display.get_surface().get_size()
        #     Functions.alter_window(self.hwnd, x_delta=x_delta, y_delta=y_delta, width=width, height=height)
        self.resizer.do_thing()

    def update_and_draw(self, song):
        song_element = SongElement(song, self.screen)

        self.screen.fill((23, 23, 23))
        song_element.draw_all()
