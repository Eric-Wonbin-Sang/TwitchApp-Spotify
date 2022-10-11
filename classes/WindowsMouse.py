import win32gui


class WindowsMouse:

    def __init__(self):

        flags, h_cursor, (x, y) = win32gui.GetCursorInfo()

        self.x, self.y = x, y
        self.prev_x, self.prev_y = self.x, self.y

    def update(self):
        flags, h_cursor, (x, y) = win32gui.GetCursorInfo()

        self.prev_x, self.prev_y = self.x, self.y
        self.x, self.y = x, y

    def __str__(self):
        return "x: {}\ty: {}".format(
            self.x,
            self.y
        )
