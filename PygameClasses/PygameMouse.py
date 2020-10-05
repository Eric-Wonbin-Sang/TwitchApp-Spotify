import pygame


class Mouse:

    def __init__(self):

        self.x, self.y = pygame.mouse.get_pos()
        self.prev_x, self.prev_y = pygame.mouse.get_pos()
        self.click_list = pygame.mouse.get_pressed()

        self.left_click, self.middle_click, self.right_click = self.get_click_info()

    def get_click_info(self):
        return (bool(x) for x in pygame.mouse.get_pressed())

    def update(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.left_click, self.middle_click, self.right_click = self.get_click_info()

    def __str__(self):
        return "x: {}\ty: {}\tleft: {}\tmiddle: {}\tright: {}".format(
            self.x,
            self.y,
            self.left_click,
            self.middle_click,
            self.right_click
        )
