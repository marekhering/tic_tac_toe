
import pygame as pg


class Screen:
    def __init__(self, width: int, height: int, background_color = None):
        self.pygame_screen = pg.display.set_mode((width, height))
        self.background_color = background_color

    def set_background_color(self, color):
        self.background_color = color

    def draw(self):
        if self.background_color:
            self.pygame_screen.fill(self)
