import pygame

from ctypes import windll

from exceptions.Exceptions import QuitException
from classes.gui_helpers.RollingAverageNumber import RollingAverageNumber

from General import Constants


class Resizer:

    window_adjust_multiplier = Constants.window_adjust_multiplier
    window_adjust_x_delta = Constants.window_adjust_x_delta
    window_adjust_y_delta = Constants.window_adjust_y_delta

    x_ran = RollingAverageNumber(Constants.rolling_average_number_x_average_count)
    y_ran = RollingAverageNumber(Constants.rolling_average_number_y_average_count)

    def __init__(self, hwnd, key_dict, system_type):

        self.width, self.height = pygame.display.get_surface().get_size()
        self.hwnd = hwnd
        self.key_dict = key_dict
        self.system_type = system_type
        self.x, self.y = self.get_x_and_y()
        self.clock = pygame.time.Clock()

    def get_x_and_y(self):
        import win32gui
        bbox = win32gui.GetWindowRect(self.hwnd)
        return bbox[0], bbox[1]

    def process_keys(self):

        for event in pygame.event.get():
            for key in self.key_dict.values():
                key.update(event)

        x_was_updated, y_was_updated = False, False
        if self.key_dict["ctrl"].is_pressed:
            if self.key_dict["w"].is_pressed:
                self.y_ran.add(-self.window_adjust_multiplier * self.window_adjust_y_delta)
                y_was_updated = True
            if self.key_dict["a"].is_pressed:
                self.x_ran.add(-self.window_adjust_multiplier * self.window_adjust_x_delta)
                x_was_updated = True
            if self.key_dict["s"].is_pressed:
                self.y_ran.add(self.window_adjust_multiplier * self.window_adjust_y_delta)
                y_was_updated = True
            if self.key_dict["d"].is_pressed:
                self.x_ran.add(self.window_adjust_multiplier * self.window_adjust_x_delta)
                x_was_updated = True
            if self.key_dict["q"].is_pressed:
                raise QuitException

        if not x_was_updated:
            self.x_ran.add(0)
        if not y_was_updated:
            self.y_ran.add(0)

        self.key_dict["mouse"].update_position()

        x_delta = 0 if not (mouse := self.key_dict["mouse"]).is_pressed else mouse.x - mouse.prev_x
        y_delta = 0 if not (mouse := self.key_dict["mouse"]).is_pressed else mouse.y - mouse.prev_y
        self.alter_window(
            x_delta=x_delta, y_delta=y_delta,
            width_delta=self.x_ran.value, height_delta=self.y_ran.value
        )

    @staticmethod
    def modify_int(some_int):
        """ Negative numbers are floored. Positive numbers are rounded. If -1 < number < 1, go to -1 or 1. """
        if some_int <= -1.0 or some_int >= 1.0:
            return round(some_int) if some_int > 0 else -round(-some_int)
        elif some_int == 0.0:
            return 0
        elif -1 < some_int < 0:
            return -1
        elif 0 < some_int < 1.0:
            return 1
        print(f"Could not catch resizer integer: {some_int}")

    def alter_window(self, x_delta=0, y_delta=0, width_delta=0, height_delta=0):

        self.x, self.y = self.x + x_delta, self.y + y_delta

        width_delta = self.modify_int(width_delta)
        height_delta = self.modify_int(height_delta)

        time_adjust = self.clock.tick(90)
        self.width = new_width if (new_width := self.width + width_delta) * time_adjust >= 10 else 10
        self.height = new_height if (new_height := self.height + height_delta) * time_adjust >= 10 else 10

        pygame.display.set_mode((int(self.width), int(self.height)), pygame.NOFRAME)
        windll.user32.MoveWindow(self.hwnd, self.x, self.y, int(self.width), int(self.height), False)
