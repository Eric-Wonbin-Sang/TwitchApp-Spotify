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

        self.surface, self.rect = self.get_surface_and_rect()

    def update_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_surface_and_rect(self):
        text_surface, rect = self.render(self.text, self.color)
        return text_surface, rect

    def draw(self, screen):
        self.surface, self.rect = self.get_surface_and_rect()
        self.surface.set_alpha(self.opacity)

        x_offset = 0
        y_offset = 0

        if self.draw_center:
            screen.blit(self.surface,
                        (self.x + x_offset - self.rect.width / 2, self.y + y_offset - self.rect.height + self.size/2))
        else:
            screen.blit(self.surface, (self.x + x_offset, self.y + y_offset))
