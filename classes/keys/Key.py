import pygame


class Key:

    def __init__(self, target):

        self.target = target
        self.is_pressed = False

    @staticmethod
    def can_update(event):
        return event.type in [pygame.KEYDOWN, pygame.KEYUP]

    def update(self, event):
        if not self.can_update(event):
            return
        if pygame.key.key_code(self.target) == event.key:
            if event.type == pygame.KEYDOWN:
                self.is_pressed = True
            elif event.type == pygame.KEYUP:
                self.is_pressed = False

    @staticmethod
    def find_key(key_list, target):
        for key in key_list:
            if key.target == target:
                return key

    def __str__(self):
        return f"Key(target={self.target}, is_pressed={self.is_pressed})"
