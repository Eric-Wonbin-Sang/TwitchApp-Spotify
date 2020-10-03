from pygame.freetype import Font


class EasyText(Font):

    def __init__(self, **kwargs):

        self.font_file = kwargs.get("font_file")
        self.size = kwargs.get("size")

        super().__init__(
            self.font_file,
            self.size
        )

        self.text = kwargs.get("text")

        self.x = kwargs.get("x", 0)
        self.y = kwargs.get("y", 0)
        self.color = kwargs.get("color", (0, 0, 0))
        self.opacity = kwargs.get("opacity", 100)
        self.draw_center = kwargs.get("draw_center", True)
        self.draw_from_bottom = kwargs.get("draw_from_bottom", False)

    def update_coordinates(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        text_surface, rect = self.render(self.text, self.color)
        text_surface.set_alpha(self.opacity)

        x_offset = 0
        y_offset = 0

        if self.draw_center:
            screen.blit(text_surface, (self.x + x_offset - rect.width / 2, self.y + y_offset - rect.height + self.size/2))
        else:
            screen.blit(text_surface, (self.x + x_offset, self.y + y_offset))
