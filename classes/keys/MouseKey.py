import pygame
import win32gui

from classes.keys.Key import Key


class MouseKey(Key):

    """
    Yeah... still not sure about this name. Or this class even existing.
    This feels illegal.

    """

    def __init__(self, mouse_event_type):

        super().__init__(mouse_event_type)

        flags, h_cursor, (x, y) = win32gui.GetCursorInfo()
        self.x, self.y = x, y
        self.prev_x, self.prev_y = self.x, self.y

    def update_position(self):
        flags, h_cursor, (x, y) = win32gui.GetCursorInfo()
        self.prev_x, self.prev_y = self.x, self.y
        self.x, self.y = x, y

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.is_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.is_pressed = False
