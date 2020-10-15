from PygameClasses import EasyText, EasyRect


class RollingText:

    def __init__(self, screen, text, background_color):

        self.screen = screen
        self.spacer_constant = 5
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.dimension = int(self.screen_height - self.screen_height / self.spacer_constant)

        self.text = text
        self.background_color = background_color

        self.easy_text = self.get_easy_text()
        # self.background_surface = self.get_background_surface()

    def get_easy_text(self):
        return EasyText.EasyText(
            text=self.text,
            x=self.dimension + self.screen_height / self.spacer_constant,
            y=self.screen.get_height() / 4,
            size=self.screen.get_height() / 3.75,
            font_file="FontFolder/Product Sans Bold.ttf",
            color=(255, 255, 255),
            opacity=255,
            draw_center=False
        )

    def get_background_surface(self):
        return None

    def draw(self):
        self.screen.blit(self.transformed_song_image, self.song_image_rect)
