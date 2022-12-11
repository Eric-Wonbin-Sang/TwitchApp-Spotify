import pygame

from classes.keys.Key import Key


class MouseKey(Key):

    """
    Yeah... still not sure about this name. Or this class even existing.
    This feels illegal.

    There should probably be a Mouse class that contains 2 Key instances.

    """

    def __init__(self, mouse_event_type, system_type):

        super().__init__(mouse_event_type)

        self.system_type = system_type
        self.x, self.y = self.get_cursor_position()
        self.prev_x, self.prev_y = self.x, self.y

    def get_cursor_position(self):
        if self.system_type == "windows":
            import win32gui
            _, _, (x, y) = win32gui.GetCursorInfo()
            return x, y
        else:
            return 0, 0

    def update_position(self):
        x, y = self.get_cursor_position()
        self.prev_x, self.prev_y = self.x, self.y
        self.x, self.y = x, y

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.is_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.is_pressed = False
