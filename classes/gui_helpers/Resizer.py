import pygame
import win32gui

from classes.gui_helpers.RollingAverageNumber import RollingAverageNumber

from General import Constants


class Resizer:

    window_adjust = Constants.window_adjust
    window_adjust_x_multiplier = Constants.window_adjust_x_multiplier
    window_adjust_y_multiplier = Constants.window_adjust_y_multiplier

    x_ran = RollingAverageNumber(10)
    y_ran = RollingAverageNumber(10)

    def __init__(self, hwnd, key_dict):
        self.width, self.height = pygame.display.get_surface().get_size()
        self.hwnd = hwnd
        self.key_dict = key_dict
        self.x, self.y = self.get_x_and_y()

    def get_x_and_y(self):
        bbox = win32gui.GetWindowRect(self.hwnd)
        return bbox[0], bbox[1]

    def change_dimensions(self, width_delta=0, height_delta=0):
        if self.width + width_delta > 10 and self.height + height_delta > 10:
            # walrus operator doesn't work here, why?
            pygame.display.set_mode((self.width + width_delta, self.height + height_delta), pygame.NOFRAME)
            self.width += width_delta
            self.height += height_delta

    def alter_window(self, x_delta=0, y_delta=0, width_delta=0, height_delta=0):

        self.x = self.x + x_delta
        self.y = self.y + y_delta
        self.width = new_width if (new_width := int(self.width + width_delta)) >= 10 else 10
        self.height = new_height if (new_height := int(self.height + height_delta)) >= 10 else 10

        win32gui.MoveWindow(self.hwnd, self.x, self.y, self.width, self.height, True)

    def move_window(self, x_delta=None, y_delta=None):
        self.alter_window(x_delta=x_delta, y_delta=y_delta)

    def resize_window(self, width_delta=None, height_delta=None):
        self.alter_window(width_delta=width_delta, height_delta=height_delta)

    def do_thing(self):

        if self.key_dict["ctrl"].is_pressed:
            if self.key_dict["w"].is_pressed:
                self.y_ran.add(-self.window_adjust * self.window_adjust_y_multiplier)
            if self.key_dict["a"].is_pressed:
                self.x_ran.add(-self.window_adjust * self.window_adjust_x_multiplier)
            if self.key_dict["s"].is_pressed:
                self.y_ran.add(self.window_adjust * self.window_adjust_y_multiplier)
            if self.key_dict["d"].is_pressed:
                self.x_ran.add(self.window_adjust * self.window_adjust_y_multiplier)
            if self.key_dict["q"].is_pressed:
                pygame.quit()

        self.x_ran.add(0)
        self.y_ran.add(0)

        self.change_dimensions(width_delta=self.x_ran.get_value(), height_delta=self.y_ran.get_value())

        if self.key_dict["mouse"].is_pressed:
            x_delta, y_delta = self.key_dict["mouse"].x - self.key_dict["mouse"].prev_x, \
                               self.key_dict["mouse"].y - self.key_dict["mouse"].prev_y
            print(x_delta, y_delta)
            self.alter_window(x_delta=x_delta, y_delta=y_delta)
